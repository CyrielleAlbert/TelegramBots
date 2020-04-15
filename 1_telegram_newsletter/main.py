import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import json
import News.news as news

global pays, articles, bot_token, apikey
pays = ['France','UK','Norway','Spain','USA']

def start(update,context):
    username = update.message.from_user.first_name
    text = 'Hi ' + username +' ! 😊 \n ' \
                             'Try /country if you want to receive the news of a country \n' \
                             'Try /keyword if you want to search with keyword.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def get_news_per_country(update,context):
    text = 'Of which country do you want the news today ? \n Please choose :'
    buttons = [[InlineKeyboardButton("France", callback_data='1')],
               [InlineKeyboardButton("UK", callback_data='2')],
               #[InlineKeyboardButton("Norway", callback_data='3')],
               #[InlineKeyboardButton("Spain", callback_data='4')],
               [InlineKeyboardButton("USA", callback_data='5')]]
    reply_markup = InlineKeyboardMarkup(buttons)

    update.message.reply_text(text, reply_markup= reply_markup)

def buttonHandler(update, context):
    print("button pressed")

    query = update.callback_query
    print(query.data)
    query.answer()
    print(query.data)
    print(query.data)

    if int(query.data) < 10 :
        text = "Selected country: "+ pays[int(query.data)-1]
        print(text)
        query.edit_message_text(text=text)
        articles = get_news(query.data)
        text = " Here are the 10 lasts news from "+ pays[int(query.data)-1]+ " : \n"
        print(text)
        for i in range(len(articles)):
            num = i+1
            title = articles[i]['title']
            url = articles[i]['url']
            text = text + "{}. ".format(num) + str(title) + " (Link: "+ str(url)+ ")\n"
        print(text)
        buttons = [[InlineKeyboardButton("France", callback_data='1')],
                   [InlineKeyboardButton("UK", callback_data='2')],
                   #[InlineKeyboardButton("Norway", callback_data='3')],
                   #[InlineKeyboardButton("Spain", callback_data='4')],
                   [InlineKeyboardButton("USA", callback_data='5')],
                   [InlineKeyboardButton("I am done ! :) ", callback_data='100')],]
        reply_markup = InlineKeyboardMarkup(buttons)
        context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True)
        update.message.reply_text("Do you need anything else ?", reply_markup=reply_markup)

    elif query.data == 100:
        chat_id = update.message.chat_id
        context.bot.send_message(chat_id, "See you soon ! :) ")


def get_news(data):
    data = int(data)
    if data == 1:
        articles = news.get_news_from_france(apikey)
    elif data == 2:
        articles = news.get_news_from_uk(apikey)
    elif data == 3:
        articles = news.get_news_from_norway(apikey)
    elif data == 4:
        articles = news.get_news_from_spain(apikey)
    elif data == 5:
        articles = news.get_news_from_usa(apikey)
    return articles

def keyword(update,context):
    text = 'Please write a keyword you want to include in the research.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def get_news_with_keyword(update,context):
    print("hello")
    keyword = update.effective_message.text
    articles = news.get_news_from_keyword(apikey, keyword)
    text = " Here are the 10 lasts news: \n"
    for i in range(len(articles)):
        num = i + 1
        title = articles[i]['title']
        url = articles[i]['url']
        text = text + "{}. ".format(num) + str(title) + " (Link: " + str(url) + ")\n"
    print(text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, disable_web_page_preview=True)


def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('country', get_news_per_country))
    dp.add_handler(CommandHandler('keyword', keyword))
    dp.add_handler(MessageHandler(Filters.text, get_news_with_keyword))
    dp.add_handler(CallbackQueryHandler(buttonHandler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    with open('tokens.txt','r') as tokens_file :
        tokens = json.load(tokens_file)
        bot_token = tokens["Bot Token"]
        apikey = tokens["News API key"]
    main()