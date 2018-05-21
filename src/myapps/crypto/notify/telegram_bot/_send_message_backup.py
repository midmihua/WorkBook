# -*- coding: utf-8 -*-
from telegram.ext import Updater
from myapps.crypto.notify.telegram_bot._conf import TOKEN, CHAT_ID


def get_message():
    pass


def send(token, chat_id, text):
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=token)

    # Start the Bot
    # updater.start_polling()

    # Send message
    updater.bot.send_message(chat_id=chat_id, text=text)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    # updater.idle()


def run():
    print('1. Send message process is started')
    send(TOKEN, CHAT_ID, 'test message -)')
    print('2. Send message process is completed')
