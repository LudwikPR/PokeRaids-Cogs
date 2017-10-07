import discord
from discord.ext import commands
import os
import sys
client = discord.Client()

def sshgo(cmd):
        cmds = {
            'alarm': 'service pr restart',
            'riki': 'service riki restart',
            'stl': 'service stl restart',
            'mj': 'service mj restart',
        }
        theCmd = cmds[cmd]
        os.system(theCmd)

class kanaBot:
    """Allow kanaNagu to have basic control"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @commands.has_role("PokeRaids.Staff")
    async def pr(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Commande innexistante!')

    @pr.command(pass_context=True)
    async def riki(self, ctx):
       sshgo("tallinn")
       await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Rimouski Redémarré")

    @pr.command(pass_context=True)
    async def stl(self, ctx):
        sshgo("stl")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Sainte-Luce Redémarré")

    @pr.command(pass_context=True)
    async def mj(self, ctx):
        sshgo("mj")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Mont-Joli Redémarré")

    @pr.command(pass_context=True)
    async def alarm(self, ctx):
        sshgo("alarm")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" PokéAlarms Redémaré")


def setup(bot):
    bot.add_cog(kanaBot(bot))
