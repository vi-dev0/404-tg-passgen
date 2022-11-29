# Telegram Bot Password Generator

import telebot
from password_generator import PasswordGenerator
import config

pwo = PasswordGenerator()
bot = telebot.TeleBot(config.token)
