from discord.ext.commands import Bot, Cog, Context, errors


class ErrorHandler(Cog):
    """Handles errors emitted from commands."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, context: Context, e: errors.CommandError) -> None:
        if isinstance(e, errors.CheckFailure):
            await self.handle_check_failure(context, e)

    @staticmethod
    async def handle_check_failure(context: Context, e: errors.CheckFailure) -> None:
        if isinstance(e, errors.NoPrivateMessage):
            await context.send(e)


async def setup(bot: Bot) -> None:
    """Load the Testing cog."""
    await bot.add_cog(ErrorHandler(bot))
