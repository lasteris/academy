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


    @commands.command(name='cd', aliases=['jump-cd'])
    async def cooldown(self, ctx, *args):
        cds = self.db_service.get_collection('cooldowns')

        if not args:
            await ctx.send(CD_INFO)
        elif args[0] == 'status':
            await self.show(cds, ctx)
        elif args[0] == 'start':
            await self.create(cds, ctx)
        elif args[0] == 'stop':
            await self.stop(cds, ctx)


    async def create(self, cds, ctx):
        """ Create cooldown record """
        start = datetime.datetime.now(datetime.timezone.utc)
        end = start + timedelta(days=DAYS)
        cds.update_one(
                filter={'memberId': ctx.author.id},
                update={
                    "$set": {
                        'memberId': ctx.author.id,
                        'start': start.strftime(DATE_TIME_FORMAT),
                        'end': end.strftime(DATE_TIME_FORMAT),
                        'name': ctx.author.name,
                        'warned': False
                    }
                },
                upsert=True)
        await ctx.send(CD_START_MESSAGE.format(ctx.author, start, end))


    async def show(self, cds, ctx):
        """ Status of cooldown """
        jumper = cds.find_one({'memberId': ctx.author.id})

        if not jumper:
            await ctx.send(NO_CD.format(ctx.author))
        else:
            now = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
            end = datetime.datetime.strptime(jumper['end'], DATE_TIME_FORMAT)
            diff = end - now
            days = diff.days
            hours = diff.seconds//3600
            minutes = (diff.seconds//60)%60
            if now > end:
                await ctx.send(CD_EXPIRED.format(ctx.author))
            else:
                await ctx.send(CD_STATUS.format(ctx.author, days, hours, minutes))


    async def stop(self, cds, ctx):
        """ Stop existed cooldown"""
        jumper = cds.find_one({'memberId': ctx.author.id})

        if not jumper:
            await ctx.send(NO_CD.format(ctx.author))
        else:
            cds.delete_one(jumper)
            await ctx.send(CD_DELETED.format(ctx.author))


    @tasks.loop(hours=8)
    async def countdown(self):
        cds = self.db_service.get_collection('cooldowns')
        now_time = datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        for jumper in cds.find({'warned': False}):
            member = await self.bot.fetch_user(int(jumper["memberId"]))
            end_time = datetime.datetime.strptime(jumper['end'], DATE_TIME_FORMAT)
            if end_time <= now_time:
                try:
                    await member.send(CD_EXPIRED)
                except Exception:
                    pass
                cds.update_one(
                    filter=jumper,
                    update={"$set": {'warned': True}})