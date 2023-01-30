from discord import Client, Embed, User
from typing import Optional

class Player:
    '''TODO: Type out better descriptions'''

    def __init__(self, user: User, client: Client):
        '''Discord Client ID the User is interacting with'''
        self.client = client

        '''Discord user ID'''
        self.id = user.id

        '''Discord user name'''
        self.name = user.name

    def getProfile(message) -> Optional[Embed]:
        return
