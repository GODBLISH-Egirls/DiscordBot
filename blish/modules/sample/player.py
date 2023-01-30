from typing import Optional, Union

from discord import Embed, Member, User

from blish.constants import ColorConfig


class Player:
    """TODO: Type out better descriptions."""

    def __init__(self, user: Union[Member, User]):
        """Discord user ID."""
        self.id = user.id

        """Discord user name."""
        self.name = user.name

        """Registered status."""
        self.registered = True

    def getProfile(self) -> Optional[Embed]:
        if not self.registered:
            return None
        embed = Embed(
            title='sampleembed',
            color=ColorConfig.aqua,
            description='Sample body text'
        )
        embed.add_field(name="Command List", value="Here are all commands", inline=False)
        embed.add_field(name="!test", value="testing function\n for testing", inline=True)
        embed.add_field(name="!sample", value="sample embed command\n this command", inline=True)
        return embed
