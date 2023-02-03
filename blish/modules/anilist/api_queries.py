import ast

import requests


class AniListApiQueries:
    """The AniListApiQueries class contains methods to invoke the AniList GQL Api and retrieve the respective information."""

    API_URL = 'https://graphql.anilist.co'

    def get_anime(self, media_name: str) -> dict:
        """
            Queries the AniList GQL query to search for the given input anime name info.

        Args:
            media_name (str): Anime Name to be searched

        Returns:
            dict: Python Dict with the anime searched anime info.

        """
        query = """
            query ($search: String) {
                Media (search: $search, type: ANIME) {
                    id
                    title {
                        romaji
                        english
                        native
                    }
                    type
                    description
                    startDate {
                        year
                    }
                    endDate {
                        year
                    }
                    episodes
                    coverImage {
                        large
                    }
                    averageScore
                    popularity
                    rankings {
                        rank
                        allTime
                        context
                    }
                    siteUrl
                }
            }
        """

        variables = {
            'search': media_name
        }

        # Make the HTTP Api request
        resp = requests.post(self.API_URL, json={'query': query, 'variables': variables})
        if resp.status_code == 200:
            print(self._clean_response(resp.text))
            return self._response_str_to_dict(self._clean_response(resp.text))

        else:
            return {}

    def get_manga(self, media_name: str) -> dict:
        pass

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
