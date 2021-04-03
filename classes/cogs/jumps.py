from constants import *
from discord.ext import commands, tasks
from datetime import timedelta
import datetime

class JumpCog(commands.Cog):
    def __init__(self, bot, db_service):
        self.bot = bot
        self.db_service = db_service
        self.countdown.start()

    @commands.command(name='jump-watch')
    async def start_watching(self, ctx, *args):
        if not args or len(args) > 1:
            await ctx.send(JUMP_WATCH_USAGE)
            return

        if(args[0] == "status"):
            if(self.countdown.is_running()):
                await ctx.send(NEXT_WATCH_CHECK_AT
                .format(self.countdown.next_iteration.strftime("%d %B %Y %H:%M:%S")))
            else:
                await ctx.send(WATCH_INACTIVE)
        elif(args[0] == "start"):
            self.countdown.start()
            await ctx.send(WATCH_STARTED)
        elif(args[0] == "stop"):
            self.countdown.cancel()
            await ctx.send(WATCH_CANCELLED)
        else:
            await ctx.send(PARAMETER_NOT_RECOGNIZED)


    @commands.command(name='jump-cd')
    async def cooldown(self, ctx, *args):
        cur_time = datetime.datetime.now(datetime.timezone.utc)
        end_time = cur_time + timedelta(days=21)

        cds = self.db_service.get_collection('cooldowns')

        jumper_id_str = str(ctx.author.id)
        cur_str = cur_time.strftime(DATE_TIME_FORMAT)
        end_str = end_time.strftime(DATE_TIME_FORMAT)

        if not args:
            cds.update_one(
                filter={'memberId': jumper_id_str},
                update={
                    "$set": {
                        'memberId': jumper_id_str,
                        'start': cur_str,
                        'end': end_str,
                        'name': ctx.author.display_name,
                        'warned': False
                    }
                },
                upsert=True)

            await ctx.send(CD_START_MESSAGE.format(ctx.author, cur_str, end_str))

        elif args[0] == 'status':
            jumper = cds.find_one({'memberId': jumper_id_str})
            if jumper:
                end_time = datetime.datetime.strptime(jumper['end'], DATE_TIME_FORMAT)
                now_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
                diff = end_time - now_time
                days = diff.days
                hours = diff.seconds//3600
                minutes = (diff.seconds//60)%60
                if now_time > end_time:
                    await ctx.send(CD_EXPIRED.format(ctx.author))
                else:
                    await ctx.send(CD_STATUS.format(ctx.author, days, hours, minutes))



    @tasks.loop(hours=8)
    async def countdown(self):
        cds = self.db_service.get_collection('cooldowns')
        now_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        for jumper in cds.find({'warned': False}):
            member = await self.bot.fetch_user(int(jumper["memberId"]))
            end_time = datetime.datetime.strptime(jumper['end'], DATE_TIME_FORMAT)
            if end_time <= now_time:
                try:
                    await member.send("Your jump cooldown has expired.\n**Have fun!**")
                except Exception:
                    pass
                cds.update_one(
                    filter=jumper,
                    update={"$set": {'warned': True}})