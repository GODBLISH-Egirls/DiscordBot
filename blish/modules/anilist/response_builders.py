import discord
from discord import embeds

from blish.utils.helpers import clean_html_tags, clean_url


class AniListResponseBuilder:
    """
    The AniListResponseBuilder class contains methods that is used to build responses from the AniList GQL
    API to formatted Discord Embeds.
    """

    DESCRIPTION_WORD_COUNT = 100

    def build_embed_anilist_info(self, media_info: dict, media_type: str) -> embeds.Embed:
        """
        Builds the respective Discord Embed with the AniList information.

        Args:
            media_info (dict): Dictionary of anime information retrieved from AniList GQL Api
            media_type (str): Type of media as defined by AniList (ex. ANIME, MANGA, etc.)

        Returns: Discord Embed

        """
        if media_type == "ANIME":
            return self._get_embed_anime_info(media_info)

    def _get_embed_anime_info(self, media_info: dict) -> embeds.Embed:
        """
        Generates the Discord embed response for when retrieving Anime Information.

        Args:
            media_info (dict): Dictionary of anime information retrieved from AniList GQL Api

        Returns: Discord Embed

        """
        eng_title = media_info.get("title").get("english")
        romaji_title = media_info.get("title").get("romaji")
        native_title = media_info.get("title").get("native")
        media_type = media_info.get("type")
        avg_score = "\U00002B50 " + self._score_to_percent_formatter(media_info.get("averageScore"), 10)
        popularity = media_info.get("popularity")
        release_year = media_info.get("startDate").get("year")
        end_year = media_info.get("endDate").get("year")
        cover_image = clean_url(media_info.get("coverImage").get("large"))
        anilist_url = clean_url(media_info.get("siteUrl"))
        episodes = media_info.get("episodes")
        description = self._truncate_description(description=clean_html_tags(media_info.get("description")),
                                                 word_count=self.DESCRIPTION_WORD_COUNT)
        rank = self._get_media_all_time_ranking(media_info.get("rankings"))

        embed = embeds.Embed(
            title=romaji_title,
            url=anilist_url,
            description=description,
            color=discord.Color.purple()
        )

        embed.set_image(url=cover_image)
        embed.add_field(name="English Title", value=eng_title, inline=True)
        embed.add_field(name="Native Title", value=native_title, inline=True)
        embed.add_field(name="Type", value=media_type, inline=True)
        embed.add_field(name="Release Year", value=release_year, inline=True)
        embed.add_field(name="End Year", value=end_year, inline=True)
        embed.add_field(name="Episodes", value=episodes, inline=True)
        embed.add_field(name="Average Score", value=avg_score, inline=True)
        embed.add_field(name="Popularity", value=popularity, inline=True)
        embed.add_field(name="Rank", value=rank, inline=True)

        return embed

    @staticmethod
    def _truncate_description(description: str, word_count: int) -> str:
        if description.count(" ") + 1 > word_count:
            description_as_list = description.split()[0: word_count]
            description_as_list.append("...")
            return " ".join(description_as_list)

        return description

    @staticmethod
    def _score_to_percent_formatter(score: int, total: int) -> str:
        return str(score/total) + "/" + str(total)

    @staticmethod
    def _get_media_all_time_ranking(rankings: list) -> str:
        for ranking in rankings:
            if ranking.get("context") == "highest rated all time" and ranking.get("allTime"):
                return str(ranking.get("rank"))
        else:
            return "N/A"
