from discord.ext.commands import Cog, Context, command

from blish.blish import Blish
from blish.modules.sample.player import Player


class Testing(Cog):
    """Testing sample class of how to implement discord commands."""

    def __init__(self, bot: Blish, *args, **kwargs):
        super(*args, **kwargs)
        self.bot = bot
        self.runtime = 0

    @command()
    # !test
    async def test(self, context: Context) -> None:
        """Test function."""
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
            await context.message.reply('You must register first!')

    @command()
    # !colored_text_sample
    # https://gist.github.com/kkrypt0nn/a02506f3712ff2d1c8ca7c9e0aed7c06#file-ansi-colors-showcase-md
    async def colored_text(self, context: Context) -> None:
        await context.send('''
```ansi
Text coloring example!

\u001b[0;30mGray\u001b[0;0m
\u001b[0;31mRed\u001b[0;0m
\u001b[0;32mGreen\u001b[0;0m
\u001b[0;33mYellow\u001b[0;0m
\u001b[0;34mBlue\u001b[0;0m
\u001b[0;35mPink\u001b[0;0m
\u001b[0;36mCyan\u001b[0;0m
\u001b[0;37mWhite\u001b[0;0m
\u001b[0;40mFirefly dark blue background\u001b[0;0m
\u001b[0;41mOrange background\u001b[0;0m
\u001b[0;42mMarble blue background\u001b[0;0m
\u001b[0;43mGreyish turquoise background\u001b[0;0m
\u001b[0;44mGray background\u001b[0;0m
\u001b[0;45mIndigo background\u001b[0;0m
\u001b[0;46mLight gray background\u001b[0;0m
\u001b[0;47mWhite background\u001b[0;0m
```
        ''')


async def setup(bot: Blish) -> None:
    """Load the Testing cog."""
    await bot.add_cog(Testing(bot))
