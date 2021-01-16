import discord
from constants import *
from discord.ext import commands

def lookup_role(ctx, name):
    return discord.utils.get(ctx.guild.roles, name = name)

def lookup_predefined_roles(ctx):
    return [role for role in [lookup_role(ctx, name) for name in ["Predators", "Stars", "Vipers", "Jumpers", "Eternals", "Among", "Rebels", "Reapers"]] if role]

class RolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx, *, arg):

        if len(arg) < 4:
            await ctx.send(AT_LEAST_4)
            return

        roles = lookup_predefined_roles(ctx)

        found = False

        league = arg.lower()

        for role in roles:
            lower_role = role.name.lower()
            if lower_role in league or league in lower_role:
                found = True
                if role not in ctx.author.roles:
                    await ctx.author.add_roles(role)
                    await ctx.send(ROLE_ADDED_SUCCESSFULLY.format(ctx.author, role))
                else:
                    await ctx.send(ROLE_ALREADY_ADDED.format(ctx.author, role))

        if not found:
            await ctx.send(ERROR_ON_ROLES_INTERACTION)

    @commands.command()
    async def remove(self, ctx, *, arg):

        if len(arg) < 4:
            await ctx.send(AT_LEAST_4)
            return

        roles = lookup_predefined_roles(ctx)

        found = False

        league = arg.lower()

        for role in roles:
            lower_role = role.name.lower()
            if lower_role in league or league in lower_role:
                found = True
                if role in ctx.author.roles:
                    await ctx.author.remove_roles(role)
                    await ctx.send(ROLE_REMOVED_SUCCESSFULLY.format(ctx.author, role))
                else:
                    await ctx.send(ROLE_ALREADY_REMOVED.format(ctx.author, role))

        if not found:
            await ctx.send(ERROR_ON_ROLES_INTERACTION)