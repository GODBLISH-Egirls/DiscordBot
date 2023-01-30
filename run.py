import asyncio

from blish.blish import bot
from blish.modules.test import Testing
from blish.constants import BotConfig

async def main() -> None:
    await bot.add_cog(Testing(bot))
    await bot.start(BotConfig.token)

if __name__=='__main__':
    try:
        asyncio.run(main())
    except:
        print("ayaya something happened :<")
        exit(69)
