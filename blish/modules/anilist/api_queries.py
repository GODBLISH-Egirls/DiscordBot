import ast

import requests

from blish.modules.anilist.constants import AniListConstants


class AniListApiQueries:
    """The AniListApiQueries class contains methods to invoke the AniList GQL Api and retrieve the respective information."""

    API_URL = 'https://graphql.anilist.co'

    def get_anime(self, media_name: str, media_type: str) -> dict:
        """
            Queries the AniList GQL query to search for the given input anime name info.

        Args:
            media_type (str): Type of media (ANIME or MANGA)
            media_name (str): Anime Name to be searched

        Returns:
            dict: Python Dict with the anime searched anime info.

        """
        variables = {
            'search': media_name
        }

        try:
            # Make the HTTP Api request
            resp = requests.post(self.API_URL, json={'query': self._get_query(media_type=media_type),
                                                     'variables': variables})
        except Exception as e:
            print("Unable to retrieve information from HTTP post request. Return with error ", e)
            return {}

        print(resp.status_code)
        if resp.status_code == 200:
            print(self._clean_response(resp.text))
            return self._response_str_to_dict(self._clean_response(resp.text))

        else:
            print("Unable to retrieve information from HTTP post request. Return with non-200 message")
            print(resp.reason)
            return {}

    @staticmethod
    def _get_query(media_type: str) -> str:

        if media_type == AniListConstants.ANIME:
            chapter_episodes = "episodes"
        elif media_type == AniListConstants.MANGA:
            chapter_episodes = "chapters"
        else:
            return ""

        query = """
            query ($search: String) {
                Media (search: $search, type: %s) {
                    id
                    title {
                        romaji
                        english
                        native
                    }
                    format
                    description
                    status
                    season
                    seasonYear
                    startDate {
                        year
                    }
                    endDate {
                        year
                        month
                    }
                    %s
                    coverImage {
                        large
                    }
                    averageScore
                    popularity
                    stats {
                        statusDistribution {
                            status
                            amount
                        }
                    }
                    rankings {
                        rank
                        allTime
                        context
                    }
                    siteUrl
                }
            }
        """ % (media_type, chapter_episodes)
        return query

    @staticmethod
    def _response_str_to_dict(resp_string: str) -> dict:
        try:
            resp_dict = ast.literal_eval(resp_string)
            return resp_dict
        except Exception as e:
            print("Unable to safely transform response dict string object to python dict")
            print(str(e))
            return {}

    @staticmethod
    def _clean_response(response_text: str) -> str:
        return response_text.replace("null", "\"UNKNOWN\"").replace("false", "False").replace("true", "True")
