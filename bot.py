import asyncio
from aiogram.filters import Command
from commands import *
from aiogram.types import Message
from aiogram import Bot,  Dispatcher
from config import TOKEN


dp = Dispatcher()
@dp.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer(
        f"Вітаю, {message.from_user.username}!\nЯ музичний бот, із жанром металу"
    )



async def main() -> None:
    print('Бот почав працювати')
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)
    print('Бот закінчив працювати')

if __name__ == '__main__':
    asyncio.run(main())
    print('работает')
    


@dp.message(MUSIC_COMMAND)
async def musics(message: Message)->None:
    """
    Команда для отримання усіх наявних фільмів
    """
    await message.answer(
        "All musics",reply_markup=musics_keyboard_markup(get_music())
    )

@dp.callback_query(MusicCallback.filter())
async def callb_film(callback: CallbackQuery, callback_data: MusicCallback) -> None:
    music_id = callback_data.id
    music_data = get_music(music_id=music_id)
    music = Music(**music_data) #  
    text =  f"Музика: {music.name}\n" \
            f"Автор: {', '.join(music.authors)}\n"
            f"вік: {music.year}\n" \
   
    await callback.message.answer_photo(
        caption=text,
        photo=URLInputFile(
            music.poster
        )
    )