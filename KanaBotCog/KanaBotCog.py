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
        os.exec_command(theCmd)

class kanaBot:
    """Allow kanaNagu to have basic control"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    @commands.has_role("Pokeraids.Bot")
    async def kana(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Nope!')

    @kana.command(pass_context=True)
    async def riki(self, ctx):
       sshgo("tallinn")
       await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Rimouski Redémarré")

    @kana.command(pass_context=True)
    async def stl(self, ctx):
        sshgo("stl")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Sainte-Luce Redémarré")

    @kana.command(pass_context=True)
    async def mj(self, ctx):
        sshgo("mj")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" Mont-Joli Redémarré")

    @kana.command(pass_context=True)
    async def alarm(self, ctx):
        sshgo("alarm")
        await self.bot.say(":white_check_mark: "+ (ctx.message.author).mention +" PokéAlarms Redémaré")


def setup(bot):
    bot.add_cog(kanaBot(bot))
