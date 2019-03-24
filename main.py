from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler
from selenium import webdriver
from pyvirtualdisplay import Display
import requests
import re
import os


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text='Yo hey')

def kopek(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)


def sinemakentpark(bot, update):
    # driver = webdriver.Firefox(executable_path='//usr//bin//firefox')
    # driver.get('biletinial.com//mekan//ankara-kentpark-prestige')
    # driver.save_screenshot('sample_screenshot_1.png')
    os.system("cutycapt --url=https://biletinial.com/mekan/ankara-kentpark-prestige --out=screenshot_kentpark.png --zoom-factor=3")
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=open("screenshot_kentpark.png", 'rb'))
    # driver.close()

def sinemagordion(bot, update):
    # driver = webdriver.Firefox(executable_path='//usr//bin//firefox')
    # driver.get('biletinial.com//mekan//ankara-kentpark-prestige')
    # driver.save_screenshot('sample_screenshot_1.png')
    os.system("cutycapt --url=https:///www.cinemaximum.com.tr//gordion-sinema-salonu --out=screenshot_cepa.png")
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=open("screenshot_cepa.png", 'rb'))
    # driver.close()



def main():
    updater = Updater('827906624:AAFfx8fc8DiTbj5GQklxlExboxFVYJSe6cs')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('kopek',kopek))
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('sinemakentpark',sinemakentpark))
    dp.add_handler(CommandHandler('sinemagordion',sinemagordion))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()