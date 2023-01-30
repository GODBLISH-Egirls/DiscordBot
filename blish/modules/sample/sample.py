from discord.ext.commands import Bot, Cog, command, Context
from discord.ext import tasks
from discord import Embed, Member
from modules.sample.player import Player
from constants import ColorConfig

class Testing(Cog):
    def __init__(self, bot: Bot, *args, **kwargs):
        super(*args, **kwargs)
        self.bot = bot
        self.runtime = 0

    @command()
    # !test
    async def test(self, context: Context, member: Member = None) -> None:
        '''test function'''
        await context.send(
            f'''\
                Author: {context.author}
                Channel: #{context.channel.name}
                Command: {context.command}\
            ''')

    @command(alias=('sample1',))
    # !sample, !sample1
    async def sample(self, context: Context) -> None:
        user = Player(context.author)
        profile = user.getProfile()
        if profile is not None:
            await context.message.reply(embed=profile)
        else:
            print('wtf3')
            await context.message.reply('You must register first!')

    @tasks.loop(minutes= 1.0)
    async def runtime(self):
        self.runtime += 1
        print(f'The program has been running for {self.runtime} minute(s)!')