import discord
from discord.ext.commands import Cog, Context, command

from blish.blish import Blish
from blish.modules.anilist.api_queries import AniListApiQueries
from blish.modules.anilist.response_builders import AniListResponseBuilder
from blish.utils.helpers import generate_embed_message


class AniList(Cog):
    """
    The AniList class is a custom class designed to incorporate AniList's GraphQL API into the discord bot.
    This class contains methods that allow the bot to respond to messages and commands that contains data retrieved from AniList.
    """

    def __init__(self, bot: Blish, *args, **kwargs) -> None:
        super(*args, **kwargs)
        self.bot = bot
        self.ani_list_api = AniListApiQueries()
        self.ani_list_response_builder = AniListResponseBuilder()

    @command(name="fanime")
    async def get_anime(self, context: Context):
        if context.message.content:
            prompt = context.message.content.split(' ', 1)[1]
            print(prompt)
            try:
                anilist_response = self.ani_list_api.get_anime(media_name=prompt)
                if anilist_response:
                    media_info = anilist_response.get("data").get("Media")
                    embed_response = self.ani_list_response_builder.build_embed_anilist_info(media_info=media_info,
                                                                                             media_type="ANIME")
                    await context.send(embed=embed_response)
                else:
                    await context.send(embed=generate_embed_message(title="404 Not Found",
                                                                    message="Ayaya :< Anime Not Found",
                                                                    color=discord.Color.red()))
            except Exception as e:
                print("Error Occurred when generating text from model. An exception was raised:", e)
        else:
            await context.send(embed=generate_embed_message(title="Need Anime Name",
                                                            message="What anime would you like me to find?"
                                                                    " Please add anime name after !fanime command",
                                                            color=discord.Color.purple()))


async def setup(bot: Blish) -> None:
    """Load the OpenAi cog."""
    await bot.add_cog(AniList(bot))
