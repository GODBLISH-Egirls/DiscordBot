from blish.blish import bot
from dotenv import load_dotenv
import os

load_dotenv()

if __name__=='__main__':
    TOKEN = os.getenv('DISCORD_TOKEN')
    bot.run(TOKEN)