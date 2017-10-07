import discord
import paramiko
from discord.ext import commands
import configargparse
import os
import sys
client = discord.Client()

def get_args():
        # Get full dir and default config file path
        configfile = []
        if '-cf' not in sys.argv and '--config' not in sys.argv:
            configfile = [os.getenv('CONFIG', os.path.join(
                os.path.dirname(__file__), 'config.ini'))]
        parser = configargparse.ArgParser(
            default_config_files=configfile)

        # arrrgs, also available in config/config.ini

        parser.add_argument(
            '-cf',
            '--config', is_config_file=True,
            help='path to config file (config.ini by default)')

        parser.add_argument(
            '-h',
            '--host',
            help='host for scanserver'
        )

        parser.add_argument(
            '-u',
            '--user',
            help='username for scanserver'
        )

        parser.add_argument(
            '-p',
            '--password',
            help='password for scanserver'
        )

        return parser.parse_args()

def sshgo(cmd):
        cmds = {
            'alarm': 'sudo service pr restart',
            'riki': 'sudo service riki restart',
            'stl': 'sudo service stl restart',
            'mj': 'sudo service mj restart',
        }

        args = get_args()
        theCmd = cmds[cmd]
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(args.scanhost, username=args.user,
                        password=args.password)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(theCmd)


class kanaBot:
    """Allow kanaNagu to have basic control"""

    def __init__(self, bot):
        self.bot = bot


    @commands.group(pass_context=True)
    @commands.has_role("Pokeraids.Bot")
    async def kana(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid :chicken:')

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
