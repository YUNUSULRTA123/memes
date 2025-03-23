import telebot
import os
import random
API_TOKEN = os.getenv(<api_token_of_your_telegramm_bot>)
bot = telebot.TeleBot(API_TOKEN)
@bot.message_handler(commands=['mem'])
def send_mem(message):
    print(os.listdir('images'))
    memes_folder = 'images'
    img_name = random.choice(memes_folder)
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
@bot.message_handler(commands=['memes_about_python'])
def send_mem_py(message):
    print(os.listdir('memes_about_python'))
    py_memes_folder = 'memes_about_python'
    img_name2 = random.choice(py_memes_folder)
    with open(f'images/{img_name2}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
@bot.message_handler(commands=['memes_about_minecraft'])
def send_mem_mcraft(message):
    print(os.listdir('memes_about_mcraft'))
    minecraft_memes_folder = 'memes_about_mcraft'
    img_name3 = random.choice(minecraft_memes_folder)
    with open(f'images/{img_name3}', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 
bot.polling()
