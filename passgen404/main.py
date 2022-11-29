# Telegram Bot Password Generator
#
# *** IMPORTS ***
import telebot
import passgen
import config

# *** PARAMS ***
pwo = passgen.PasswordGenerator()
bot = telebot.TeleBot(config.token)

# *** BOT ***
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hi, I can create many random passwords for you.\nType /gen to create 3 random "
                                      "passwords.")

@bot.message_handler(commands=["gen"])
def gen(message):
    bot.send_message(message.chat.id, '`' + pwo.generate() + '`' + '\n' + '`' + pwo.generate() + '`' + '\n' + '`' + pwo.generate() + '`' + '\n', parse_mode="MarkdownV2")



bot.polling(none_stop=True, interval=0)