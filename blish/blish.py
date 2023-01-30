from discord import Intents
from discord.ext import commands

from blish.constants import BotConfig

intents = Intents.default()
intents.message_content = True
intents.presences = False
intents.dm_typing = False
intents.dm_reactions = False
intents.invites = False
intents.webhooks = False
intents.integrations = False

bot = commands.Bot(
        command_prefix=BotConfig.prefix,
        case_insensitive='True',
        intents=intents
)


@bot.event
async def on_connect():
    print('the client successfully established connection with the Discord server')


@bot.event
async def on_disconnect():
    print('the client connection has been lost')


@bot.event
async def on_ready():
    print('the bot is ready to go!')
