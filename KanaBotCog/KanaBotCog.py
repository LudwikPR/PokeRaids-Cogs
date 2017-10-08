import discord
from discord.ext import commands
import os
import sys

client = discord.Client()

def sshgo(cmd):
        cmds = {
            'pokealarm': 'service pr restart',
            'rimouski': 'service riki restart',
            'luceville': 'service stl restart',
            'montjoli': 'service mj restart',
        }
        theCmd = cmds[cmd]
        os.system(theCmd)

class kanaBot:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @commands.has_role("PokeRaids.Staff")
    async def pr(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Commande innexistante!')

    @pr.command(pass_context=True)
    async def rimouski(self, ctx):
       sshgo("rimouski")
       await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Rimouski Redémarré")

    @pr.command(pass_context=True)
    async def luceville(self, ctx):
        sshgo("stl")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Sainte-Luce Redémarré")

    @pr.command(pass_context=True)
    async def montjoli(self, ctx):
        sshgo("montjoli")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Mont-Joli Redémarré")

    @pr.command(pass_context=True)
    async def pokealarm(self, ctx):
        sshgo("pokealarm")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" PokéAlarms Redémaré")

def setup(bot):
    bot.add_cog(kanaBot(bot))
