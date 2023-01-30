from discord.ext.commands import Bot, Cog, command, Context
from discord import Member

class Testing(Cog):
    def __init__(self, bot: Bot, *args, **kwargs):
        super(*args, **kwargs)
        self.bot = bot

    @command()
    async def test(self, context: Context, member: Member = None):
        '''test function'''
        await context.send(
            f'Author: {context.author}, Command: {context.command}, ')
