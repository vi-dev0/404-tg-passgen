# Telegram Bot Password Generator
#
# *** IMPORTS ***
import telebot
from password_generator import PasswordGenerator
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import config
from random import choice
import time

# *** PARAMS ***
pg = PasswordGenerator()
bot = telebot.TeleBot(config.token)

# *** BOT ***

keys = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
symbols = ["!","@","#","$","%","^","&","*","(",")","\'","\"","/","\\",",",".",";",":"]
numbers = "1234567890"
pins = ["4 digit\nPIN","5 digit\nPIN","6 digit\nPIN","7 digit\nPIN","8 digit\nPIN","9 digit\nPIN","10 digit\nPIN"]

def keyboard(key_type="Normal"):
    markup = ReplyKeyboardMarkup(True, row_width=10)
    if key_type == "Normal":
        row = KeyboardButton("Random password"), KeyboardButton("PIN"), KeyboardButton("Memorable password"),KeyboardButton("❗ Help/Info")
        markup.add(*row)
    elif key_type == "PIN":
        row = [KeyboardButton(x) for x in pins]
        markup.add(*row)
        markup.add(KeyboardButton("Menu"),KeyboardButton("❗ Help/Info"))
    else:
        row = [KeyboardButton(x.upper()) for x in keys[:10]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[10:20]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[20:29]]
        markup.add(*row)
        row = [KeyboardButton(x.upper()) for x in keys[29:]]
        markup.add(*row)
        markup.add(KeyboardButton("Normal"),KeyboardButton("Symbols"),KeyboardButton("🔙Delete"),KeyboardButton("✅Done"))
    return markup

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Hi👋,[ ](https://github.com/b4dcat404/b4dcat404/raw/main/images/header.png)"
                                    "I can create many random passwords for you\n\n"
                                    "🟢 *Random Password* \- creates 10 random passwords\n"
                                    "🟢 *PIN* \- creates random PINs certain length\n"
                                    "🔴 *Memorable Password* \- create random password from the dictionary of words\n\n"
                                    "*POWERED BY: @B4DCAT404*", parse_mode="MarkdownV2", reply_markup=keyboard())

@bot.message_handler(commands=["help"])
def info_message(message):
    bot.send_message(message.chat.id, "*How to use bot?*\n\n"
                                      "Click on __Any Password type__ to generate random passwords\n\n"
                                      "__Random password__ \- contain upper/lower digits,"
                                      "numbers and special chars\n"
                                      "__PIN__ \- contain only numbers\n"
                                      "__Memorable password__ \- contain word from dictionary", parse_mode="MarkdownV2")
    bot.send_message(message.chat.id, "*Powered by\:*\n\n"
                                      "@B4DCAT404 \- 🇷🇺 telegram chanel for developers, students and freelancers\n\n"
                                      "View source code on [GitHub](https://github.com/vi-dev0/404-tg-passgen), "
                                      "feel free to contribute\n", parse_mode="MarkdownV2")
@bot.message_handler(func=lambda message:True)
def all_messages(message):
    if message.text == "Random password":
        # markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.from_user.id,
                    '0\.\ `' + pg.generate() + '`\n' +
                    '1\.\ `' + pg.generate() + '`\n' +
                    '2\.\ `' + pg.generate() + '`\n' +
                    '3\.\ `' + pg.generate() + '`\n' +
                    '4\.\ `' + pg.generate() + '`\n' +
                    '5\.\ `' + pg.generate() + '`\n' +
                    '6\.\ `' + pg.generate() + '`\n' +
                    '7\.\ `' + pg.generate() + '`\n' +
                    '8\.\ `' + pg.generate() + '`\n' +
                    '9\.\ `' + pg.generate() + '`', parse_mode="MarkdownV2")
    elif message.text == "❗ Help/Info":
        bot.send_message(message.chat.id, "*How to use bot?*\n\n"
                                          "Click on __Any Password type__ to generate random passwords\n\n"
                                          "__Random password__ \- contain upper/lower digits,"
                                          "numbers and special chars\n"
                                          "__PIN__ \- contain only numbers\n"
                                          "__Memorable password__ \- contain word from dictionary",
                         parse_mode="MarkdownV2")
        bot.send_message(message.chat.id, "*Powered by\:*\n\n"
                                          "@B4DCAT404 \- 🇷🇺 telegram chanel for developers, students and freelancers\n\n"
                                          "View source code on [GitHub](https://github.com/vi-dev0/404-tg-passgen), "
                                          "feel free to contribute\n", parse_mode="MarkdownV2")
    elif message.text == "PIN":
        bot.send_message(message.from_user.id,"Chose PIN length",reply_markup=keyboard("PIN"))
    elif message.text == "Memorable password":
        bot.send_message(message.from_user.id,"This feature is not ready yet",reply_markup=keyboard("Normal"))
    elif message.text == "🔙Delete":
        bot.delete_message(message.from_user.id,message.message_id)
    elif message.text == "Menu":
        bot.send_message(message.chat.id, "Back to menu", reply_markup=keyboard("Normal"))
    elif message.text == "4 digit\nPIN":
        pin = ''
        for i in range(4):
            pin += choice(numbers)
        bot.send_message(message.from_user.id, "`" + pin + "`", parse_mode="MarkdownV2")
    elif message.text == "5 digit\nPIN":
        pin = ''
        for i in range(5):
            pin += choice(numbers)
        bot.send_message(message.from_user.id, "`" + pin + "`", parse_mode="MarkdownV2")
    elif message.text == "6 digit\nPIN":
        pin = ''
        for i in range(6):
            pin += choice(numbers)
        bot.send_message(message.from_user.id, "`" + pin + "`", parse_mode="MarkdownV2")
    elif message.text == "7 digit\nPIN":
        pin = ''
        for i in range(7):
            pin += choice(numbers)
        bot.send_message(message.from_user.id, "`" + pin + "`", parse_mode="MarkdownV2")
    elif message.text == "8 digit\nPIN":
        pin = ''
        for i in range(8):
            pin += choice(numbers)
        bot.send_message(message.from_user.id, "`" + pin + "`", parse_mode="MarkdownV2")
    elif message.text == "9 digit\nPIN":
        pin = ''
        for i in range(9):
            pin += choice(numbers)
        bot.send_message(message.from_user.id, "`" + pin + "`", parse_mode="MarkdownV2")
    elif message.text == "10 digit\nPIN":
        pin = ''
        for i in range(10):
            pin += choice(numbers)
        bot.send_message(message.from_user.id, "`" + pin + "`", parse_mode="MarkdownV2")
    else:
        bot.send_message(message.chat.id,"I understand only command on keyboard")

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue