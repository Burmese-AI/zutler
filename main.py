TOKEN = '7263588792:AAHFDosZxU0sNb0fH43dX-MLEvrWgiXVVwM'

"""necessities"""
import asyncio
from aiogram import Dispatcher, Bot, Router, types
from aiogram.client.default import DefaultBotProperties

"""utilities"""
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold, hitalic

""""sherlock"""
import subprocess

bot = Bot(token=TOKEN, default= DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher(bot=bot)

@dp.message(Command("add_special_day"))
async def command_help(message: types.Message):
    """Echoes whatever you say until you say stop"""
    await message.answer(
    )

@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    """Processes the start command"""

    start=f"""
Hello, {hbold(message.from_user.full_name)}!
This is your personal butler app built with love.
Please use {hitalic("/help")} to see a list of available commands.
Contact me {hitalic("@dummyemail@dummy.com")} to request new features.
"""

    await message.answer(
        text=start
    )

@dp.message(Command("help"))
async def command_help(message: types.Message):
    """Processes the help command; shows a list of possible commands"""

    help=f"""
{hbold('Available commands')}:
/start - Introduces the bot
/find {hitalic("username")} - Hunts down social media of a given username using sherlock-project(e.g. /find john)
"""
    await message.answer(
        text=help
    )

@dp.message(Command("find"))
async def test(message: types.Message):
    """Processes huntng of social media of a given username with the help of subprocess and sherlock"""
    username = message.text.split()
    if len(username) <= 2:
        username = username[1]
        await message.answer(f"{hbold(username)} captured!\nIt will be processed, please wait about 1-3 minutes")
        #while True:
            #try:
                #await message.answer("Please specify ")
        result = subprocess.run(["sherlock", username, "--timeout", "30", "--nsfw"], capture_output=True, text=True, check=True)
        result = result.stdout.splitlines()
        result = [result[i: i+30] for i in range(0, len(result), 30)]
        for i in result:
            await message.answer('\n'.join(str(j) for j in i))
    else:
        await message.answer(f"The app is still in development, so let's keep it simple and search one user at a time.")
    



async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    print("It's running now")
    asyncio.run(main())