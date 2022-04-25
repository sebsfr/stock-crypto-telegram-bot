import telegram.ext
import pandas_datareader as web
from telegram.ext import *


def start(update, context):
    update.message.reply_text('Hello! If you need guide how to check prices of different assets type /help.')


def help(update, context):
    update.message.reply_text('''
    -> Type /price + ticker symbol
    
    /price FB
    /price AAPL
    /price BTC-USD
    
    ''')


def stock(update, context):
    ticker = context.args[0]
    data = web.DataReader(ticker, 'yahoo')
    price = data.iloc[-1]['Close']
    update.message.reply_text(f'The current price of {ticker} is {price:.2f}$!')


def handle_message(update, context):
    update.message.reply_text(f'Did you really mean {update.message.text}?')


updater = Updater('TELEGRAM TOKEN HERE', use_context=True)

updater.dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
updater.dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
updater.dispatcher.add_handler(telegram.ext.CommandHandler('price', stock))
updater.dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
