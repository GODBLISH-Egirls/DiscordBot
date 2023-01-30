from discord.ext import commands
from discord import Intents
from blish.constants import COMMAND_PREFIX

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(
        command_prefix=COMMAND_PREFIX,
        case_insensitive='True',
        intents=intents
)

@bot.event
async def on_ready():
    print('the bot is ready to go!')

import blish.commands.test