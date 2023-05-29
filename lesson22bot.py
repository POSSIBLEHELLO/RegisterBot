import logging 
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from keyboards import start_menu_btn, info_yes_or_no_btn
# from btn import*
from aiogram.dispatcher import FSMContext 


BOT_TOKEN = "6082663790:AAEqFqwLSIl3kqEZ12d0SFMCqEuIZBoDBs4"


logging.basicConfig(level=logging.INFO)

# bot = Bot(token=BOT_TOKEN, parse_mode='html') 
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

info = {
    'name': "",
    'age': 0,
    'adress': "",
}



class MeningStatlarim(StatesGroup):
    ism = State()
    age = State()
    adress = State()

@dp.message_handler(commands=['start'])
async def send_well(message: types.Message):
    btn = await start_menu_btn()
    await message.answer("<b>Hi!</b>", reply_markup=btn)
    # await message.answer("<strong>Hi!</strong>")
    # await message.answer("<i>Hi!</i>")
    # await message.answer("<em>Hi!</em>")
    # await message.answer("<a href='t.me/POSSIBLE'>Hello</a>", disable_web_page_preview= True)
    # await message.answer("<u>Hi!</u>")
    # await message.answer("<ins>Hi!</ins>")
    # await message.answer("<s>Hi!</s>")
    # await message.answer("<strike>Hi!</strike>")
    # await message.answer("<del>Hi!</del>")
    # await message.answer("<span class='tg-spoiler'>Hi!</span>")
    # await message.answer("<b>bold <i>italic bold <s>italic bold strikethrough <span class='tg-spoiler'>italic bold strikethrough spoiler</span></s> <u>underline italic bold</u></i> bold</b>")
    # await message.answer("<a href='tg://user?id=123456789'>inline mention of a user</a>")
    # await message.answer("<tg-emoji emoji-id='5368324170671202286'>👍</tg-emoji>")
    # await message.answer("<pre>pre-formatted fixed-width code block</pre>")
    # await message.answer("<pre><code class='language-python'>pre-formatted fixed-width code block written in the Python programming language</code></pre>")




@dp.message_handler(text="👤 Admin bilan aloqa")
async def support_handler2(message: types.Message):
    await message.answer("Bot admini: @winchestor_dev")

@dp.message_handler(text="🖇 Ro'yxatdan o'tish")
async def user_register_handler(message: types.Message):
    await message.answer("Ismingizni kiriting: ")
    await MeningStatlarim.ism.set()


@dp.message_handler(state=MeningStatlarim.ism)
async def ism_state(message: types.Message):
    info['name'] = message.text

    await message.answer("Yoshingizni kiriting: ")
    await MeningStatlarim.age.set()


@dp.message_handler(state=MeningStatlarim.age)
async def yosh_state(message: types.Message):
    info['age'] = message.text

    await message.answer("Adress kiriting: ")
    await MeningStatlarim.adress.set()

@dp.message_handler(state=MeningStatlarim.adress)
async def adress_state(message: types.Message, state: FSMContext):
    info['adress'] = message.text

    print(info)
    btn = await info_yes_or_no_btn()
    await message.answer(f"ISM: {info['name']}\n YOSH: {info['age']}\n Manzil: {info['adress']}", reply_markup=btn)

    await state.finish()

@dp.callback_query_handler(text = 'yes',)
async def answer_yes_callback(call: types.CallbackQuery):
    #  await call.answer("You are agree", show_alert=True)
     await call.message.answer("siz otiz", show_alert=True)
     await call.message.delete()    
     

@dp.callback_query_handler(text = 'no')
async def answer_no_callback(call: types.CallbackQuery):
    #  await call.answer("You are disagree", show_alert=True)
     await call.message.answer("You are disagree", show_alert=True)
     await call.message.answer(chat_id=call.from_user.id, message_id=call.message.message_id)

if __name__=="__main__":
    executor.start_polling(dp)

