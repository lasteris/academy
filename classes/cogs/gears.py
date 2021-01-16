from constants import *
from discord.ext import commands

class UpgradesCog(commands.Cog):
    def __init__(self, db_service):
        self.db_service = db_service

    @commands.command(name='gear-cost')
    async def gear_cost(self, ctx, *args):
        if len(args) == 1:
            await self.get_cost_up_to(ctx, args[0])
        elif len(args) == 2:
            try:
                lower_num = int(args[0])
                upper_num = int(args[1])
                await self.get_cost_between(ctx, lower_num, upper_num)
            except ValueError:
                await ctx.send(GEAR_COST_WHOLE_NUM)
        else:
            await ctx.send(INVALID_NUMBER_ARGUMENTS)


    def get_cost(self, *levels):
        dict_gc = self.db_service.get_collection("dict_gc")
        total_cost = 0
        if len(levels) == 1:
            rows = dict_gc.find(
                {"level": {"$lt": levels[0]}})
            for row in rows:
                total_cost += row['cost']  # adding on the cost to total_cost
        else:
            rows = dict_gc.find(
                {"level": {"$gte": levels[0], "$lt": levels[1]}})
            for row in rows:
                total_cost += row['cost']
        return total_cost

    async def get_cost_up_to(self, ctx, level):
        gear_number = int(level)
        try:
            if 70 >= gear_number >= 1:
                cost = self.get_cost(gear_number)
                await ctx.send(GEAR_COST.format(gear_number, cost, cost*5))
            else:
                await ctx.send(GEAR_COST_OUT_RANGE)
        except ValueError:
                await ctx.send(GEAR_COST_WHOLE_NUM)

    async def get_cost_between(self, ctx, lower_num, upper_num):
        if 70 >= lower_num >= 1 and 70 >= upper_num >= 1:
            if lower_num < upper_num:
                cost = self.get_cost(lower_num, upper_num)
                await ctx.send(GEAR_COST_MULTI.format(lower_num, upper_num, cost, cost * 5))
            else:
                await ctx.send(GEAR_SECOND_LESS_THAN_FIRST.format(lower_num, upper_num))
        else:
            await ctx.send(GEAR_COST_OUT_RANGE)
