import discord
from discord import embeds

from blish.modules.anilist.constants import AniListConstants
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
            media_type (str): Type of media as defined by AniList (ex. ANIME, MANGA)

        Returns: Discord Embed

        """
        return self._get_embed_media_info(media_info, media_type=media_type)

    def _get_embed_media_info(self, media_info: dict, media_type: str) -> embeds.Embed:
        """
        Generates the Discord embed response for when retrieving Anime Information.

        Args:
            media_info (dict): Dictionary of anime information retrieved from AniList GQL Api
            media_type (str): Type of media as defined by AniList (ex. ANIME, MANGA)

        Returns: Discord Embed

        """
        eng_title = media_info.get("title").get("english")
        romaji_title = media_info.get("title").get("romaji")
        native_title = media_info.get("title").get("native")
        media_format = media_info.get("format")
        avg_score = ("\U00002B50 " + self._score_to_percent_formatter(media_info.get("averageScore"), 10)) \
            if media_info.get("averageScore") != "UNKNOWN" else media_info.get("averageScore")
        release_season = media_info.get("season")
        status = media_info.get("status")
        release_year = media_info.get("startDate").get("year")
        end_year = media_info.get("endDate").get("year")
        end_month = media_info.get("endDate").get("month")
        cover_image = clean_url(media_info.get("coverImage").get("large"))
        anilist_url = clean_url(media_info.get("siteUrl"))
        description = self._truncate_description(description=clean_html_tags(media_info.get("description")),
                                                 word_count=self.DESCRIPTION_WORD_COUNT)
        rank = self._get_media_all_time_ranking(media_info.get("rankings"))
        stats = media_info.get("stats").get("statusDistribution")

        if media_type == AniListConstants.ANIME:
            color = discord.Color.purple()
        elif media_type == AniListConstants.MANGA:
            color = discord.Color.yellow()
        else:
            color = discord.Color.red()

        embed = embeds.Embed(
            title=romaji_title,
            url=anilist_url,
            description=description,
            color=color
        )

        embed.set_image(url=cover_image)
        embed.add_field(name="English Title", value=eng_title, inline=True)
        embed.add_field(name="Native Title", value=native_title, inline=True)
        embed.add_field(name="Type", value=media_format, inline=True)

        embed.add_field(name="Average Score", value=avg_score, inline=True)
        embed.add_field(name="Rank", value=rank, inline=True)

        if media_type == AniListConstants.ANIME:
            episodes = media_info.get("episodes")
            embed.add_field(name="Episodes", value=episodes, inline=True)
            embed.add_field(name="Season", value=self._get_season(start_season=release_season, start_year=release_year,
                                                                  end_year=end_year, end_month=end_month), inline=True)

        if media_type == AniListConstants.MANGA:
            chapters = media_info.get("chapters")
            embed.add_field(name="Chapters", value=chapters, inline=True)
            embed.add_field(name="Release Year", inline=True,
                            value="```ml\n{release_year}```".format(release_year=release_year))

        embed.add_field(name="Status", value="```\n{status}```".format(status=status), inline=True)
        embed.add_field(name="Stats", value=self._build_media_stats(stats), inline=False)

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
        return str(score / total) + "/" + str(total)

    @staticmethod
    def _get_media_all_time_ranking(rankings: list) -> str:
        for ranking in rankings:
            if ranking.get("context") == "most popular all time" and ranking.get("allTime"):
                return str(ranking.get("rank"))
        else:
            return "N/A"

    @staticmethod
    def _get_season(start_season: str, start_year: int, end_year: int, end_month: int) -> str:
        end_season = AniListConstants().get_season_by_month(end_month)
        end_year = "" if end_season == "UNKNOWN" else end_year
        if start_year == end_year and start_season == end_season:
            return "```ml\n" \
                   "{start_season} {start_year}" \
                   "```".format(start_season=start_season, start_year=start_year)
        else:
            return "```ml\n" \
                   "{start_season} {start_year} - {end_season} {end_year}" \
                   "```".format(start_season=start_season, start_year=start_year,
                                end_season=end_season, end_year=end_year)

    @staticmethod
    def _build_media_stats(stats: list) -> str:
        embed_str = ""
        for stat in stats:
            embed_str += "```ml\n{stat_name} - {value}```".format(stat_name=stat["status"], value=stat["amount"])

        return embed_str
