import asyncio

from blish import bot
from modules.sample.sample import Testing
from modules.openai.open_ai_test import OpenAi
from constants import BotConfig
from time import sleep

async def main() -> None:
    await bot.add_cog(Testing(bot))
    await bot.add_cog(OpenAi(bot))
    await bot.start(BotConfig.token)

if __name__=='__main__':
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
