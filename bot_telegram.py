from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup
import requests
import logging

API_URL_quest = 'https://7012.deeppavlov.ai/model'
API_URL_mood = 'https://7015.deeppavlov.ai/model'

bot = Bot(token='5743255868:AAGMmjvKI9FTkGQdpCYyFcPG1Y4thvzUPkk')
dp = Dispatcher(bot)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def on_startup(_):
    print('Bot is online')
    await handler_user(dp)

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    reply_keyboard = [['/Rational_number_operation', '/Complex_number_operation', '/Artificial_intelligence']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.from_user.id, 'Добро пожаловать! Выберите необходимое действие!', reply_markup=markup_key)

#@dp.message_handler(commands=['Rational_number_operation'])
async def real_operation(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    reply_keyboard = [['/Sum', '/Difference', '/Multy', '/Division']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.from_user.id, 'Выберите необходимое действие!', reply_markup=markup_key)
    await handler_user_ration(dp)
    
#@dp.message_handler(commands=['Complex_number_operation'])
async def comp_operation(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    reply_keyboard = [['/Sum_compl', '/Difference_compl', '/Multy_compl']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.from_user.id, 'Выберите необходимое действие!', reply_markup=markup_key)
    await handler_user_complex(dp)

#@dp.message_handler(commands=['Artificial_intelligence'])
async def i_intellect(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    reply_keyboard = [['/Mood', '/Question']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
    await bot.send_message(message.from_user.id, 'Выберите необходимое действие!', reply_markup=markup_key)
    await handler_user_ii(dp)

async def handler_user(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(real_operation, commands=['Rational_number_operation'])
    dp.register_message_handler(comp_operation, commands=['Complex_number_operation'])
    dp.register_message_handler(i_intellect, commands=['Artificial_intelligence'])

async def handler_user_ration(dp : Dispatcher):
    dp.register_message_handler(sum_command, commands=['Sum'])
    dp.register_message_handler(diff_command, commands=['Difference'])
    dp.register_message_handler(mult_command, commands=['Multy'])
    dp.register_message_handler(div_command, commands=['Division'])

async def handler_user_complex(dp : Dispatcher):
    dp.register_message_handler(sumc_command, commands=['Sum_compl'])
    dp.register_message_handler(diffc_command, commands=['Difference_compl'])
    dp.register_message_handler(multc_command, commands=['Multy_compl'])

async def handler_user_ii(dp : Dispatcher):
    dp.register_message_handler(mood_command, commands=['Mood'])
    dp.register_message_handler(question_command, commands=['Question'])
    
async def sum_rat(message : types.Message):
    logger.info('Пользователь ввел два числа: %s: %s', message.from_user.full_name, message.text)
    items = message.text.split()
    x = float(items[0])
    y = float(items[1])
    if y > 0: znak ='+'
    else: znak ='-'
    sumrat = round(x+y, 3)
    await bot.send_message(message.from_user.id, f'{x} {znak} {abs(y)} = {sumrat}')
    await command_start(message)
    
async def sum_compl(message : types.Message):
    logger.info('Пользователь ввел четыре числа: %s: %s', message.from_user.full_name, message.text)
    items = message.text.split()
    x1 = float(items[0])
    y1 = float(items[1])
    x2 = float(items[2])
    y2 = float(items[3])
    x = round(x1 + x2, 3)
    y = round(y1 + y2, 3)
    if y1 > 0: znaky1 = '+'
    else: znaky1 = '-'
    if y2 > 0: znaky2 = '+'
    else: znaky2 = '-'
    if y > 0: znaky = '+'
    else: znaky = '-'
    await bot.send_message(message.from_user.id, f'({x1} {znaky1}{abs(y1)}i) + ({x2} {znaky2}{abs(y2)}i) = {x} {znaky}{abs(y)}i')
    await command_start(message)

async def diff_compl(message : types.Message):
    logger.info('Пользователь ввел четыре числа: %s: %s', message.from_user.full_name, message.text)
    items = message.text.split()  
    x1 = float(items[0])
    y1 = float(items[1])
    x2 = float(items[2])
    y2 = float(items[3])
    x = round(x1 - x2, 3)
    y = round(y1 - y2, 3)
    if y1 > 0: znaky1 = '+'
    else: znaky1 = '-'
    if y2 > 0: znaky2 = '+'
    else: znaky2 = '-'
    if y > 0: znaky = '+'
    else: znaky = '-'
    await bot.send_message(message.from_user.id, f'({x1} {znaky1}{abs(y1)}i) - ({x2} {znaky2}{abs(y2)}i) = {x} {znaky}{abs(y)}i')
    await command_start(message)
 
async def diff_rat(message : types.Message):
    logger.info('Пользователь ввел два числа: %s: %s', message.from_user.full_name, message.text)
    items = message.text.split()  
    x = float(items[0])
    y = float(items[1])
    diff = round(x-y, 3)
    if y > 0: znak ='-'
    else: znak ='+'
    await bot.send_message(message.from_user.id, f'{x} {znak} {abs(y)} = {diff}')
    await command_start(message)

async def mult_rat(message : types.Message):
    logger.info('Пользователь ввел два числа: %s: %s', message.from_user.full_name, message.text)
    items = message.text.split()
    x = float(items[0])
    y = float(items[1])
    await bot.send_message(message.from_user.id, f'{x} * {y} = {x*y}')
    await command_start(message)

async def mult_compl(message : types.Message):
    logger.info('Пользователь ввел четыре числа: %s: %s', message.from_user.full_name, message.text)
    items = message.text.split()  
    x1 = float(items[0])
    y1 = float(items[1])
    x2 = float(items[2])
    y2 = float(items[3])
    x = round(x1 * x2 - y1 * y2, 3)
    y = round(x1 * y2 + x2 * y1, 3)
    if y1 > 0: znaky1 = '+'
    else: znaky1 = '-'
    if y2 > 0: znaky2 = '+'
    else: znaky2 = '-'
    if y > 0: znaky = '+'
    else: znaky = '-'
    await bot.send_message(message.from_user.id, f'({x1} {znaky1}{abs(y1)}i) * ({x2} {znaky2}{abs(y2)}i) = {x} {znaky}{abs(y)}i')
    await command_start(message)
     
async def div_rat(message : types.Message):
    logger.info('Пользователь ввел два числа: %s: %s', message.from_user.full_name, message.text)
    items = message.text.split()
    x = float(items[0])
    y = float(items[1])
    if y == 0: await bot.send_message(message.from_user.id,'Делить на ноль нельзя!')
    else: 
        div = round(x / y, 3)
        await bot.send_message(message.from_user.id, f'{x} : {y} = {div}')
    await command_start(message)

async def sum_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите два числа через пробел')
    dp.register_message_handler(sum_rat)
    
async def sumc_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите Re и Im первого и Re и Im второго числа через пробел')
    dp.register_message_handler(sum_compl)

async def diff_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите два числа через пробел')
    dp.register_message_handler(diff_rat)

async def diffc_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите Re и Im первого и Re и Im второго числа через пробел')
    dp.register_message_handler(diff_compl)

async def mult_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите два числа через пробел')
    dp.register_message_handler(mult_rat)

async def multc_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите Re и Im первого и Re и Im второго числа через пробел')
    dp.register_message_handler(mult_compl)

async def div_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите два числа через пробел')
    dp.register_message_handler(div_rat)

async def mood_command(message : types.Message):
    logger.info('Пользователь выбрал из предложенного меню: %s: %s', message.from_user.full_name, message.text)
    await bot.send_message(message.from_user.id, 'Введите любое слово')
    dp.register_message_handler(mood)
     
async def mood(message : types.Message):
    data = {'x': [message.text]}
    res = requests.post(API_URL_mood, json=data).json()
    await bot.send_message(message.from_user.id, res[0][0])
    await command_start(message)

async def question_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Введите любое слово')
    dp.register_message_handler(question)

async def question(message : types.Message):
    data = {'question_raw': [message.text]}
    res = requests.post(API_URL_quest, json=data, verify=False).json()
    await bot.send_message(message.from_user.id, res[0][0])
    await command_start(message)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)