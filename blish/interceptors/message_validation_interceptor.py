from discord.ext.commands import Cog, Context, NoPrivateMessage

from blish.blish import Blish


class MessageValidationInterceptor(Cog):
    """A global interceptor that checks and validates messages."""

    def __init__(self, bot: Blish):
        self.bot = bot
        self.bot.check(self.check_if_bot)
        self.bot.check(self.check_if_guild)

    def check_if_bot(self, context: Context) -> bool:
        """Check if the context is invoked by a bot user."""
        return not context.author.bot

    def check_if_guild(self, context: Context) -> bool:
        """Check if the context is invoked in a guild."""
        if context.guild is None:
            raise NoPrivateMessage("DMs are currently disabled!")
        return True


async def setup(bot: Blish) -> None:
    """Load the MessageValidationInterceptor cog."""
    await bot.add_cog(MessageValidationInterceptor(bot))
