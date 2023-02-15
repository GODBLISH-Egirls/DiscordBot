class AniListConstants:

    ANIME = "ANIME"
    MANGA = "MANGA"

    SEASON_FOR_MONTH = {
        1: "WINTER",
        2: "WINTER",
        3: "WINTER",
        4: "SPRING",
        5: "SPRING",
        6: "SPRING",
        7: "SUMMER",
        8: "SUMMER",
        9: "SUMMER",
        10: "FALL",
        11: "FALL",
        12: "FALL",
        "UNKNOWN": "UNKNOWN"
    }

    def get_season_by_month(self, month: int) -> str:
        return self.SEASON_FOR_MONTH.get(month)
