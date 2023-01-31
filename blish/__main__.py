import asyncio
from time import sleep

from discord import Intents

import blish
from blish.blish import Blish
from blish.constants import BotConfig

intents = Intents.default()
intents.message_content = True
intents.presences = False
intents.dm_typing = False
intents.dm_reactions = False
intents.invites = False
intents.webhooks = False
intents.integrations = False

blish.instance = Blish(
        command_prefix=BotConfig.prefix,
        case_insensitive='True',
        intents=intents
)


@blish.instance.event
async def on_connect():
    print(f'Cogs: {list(blish.instance.cogs.keys())}')
    print('the client successfully established connection with the Discord server')


@blish.instance.event
async def on_disconnect():
    print('the client connection has been lost')


@blish.instance.event
async def on_ready():
    print('the bot is ready to go!')


async def main() -> None:
    async with blish.instance as server:
        await server.start(BotConfig.token)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as e:
        print("ayaya something happened :<")
        print(str(e))
        exit(69)
    except KeyboardInterrupt:
        print("See you next time!")
        sleep(1)
        exit(0)
