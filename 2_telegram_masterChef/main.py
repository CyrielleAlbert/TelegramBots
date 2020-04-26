import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
import json
import spoonacular as sp

global recipes, bot_token, apikey, api
recipes = None

def start(update,context):
    username = update.message.from_user.first_name
    text = 'Hi ' + username +' ! 😊 \n ' \
                             'I am the masterChef Bot \n' \
                             'Try /randomRecipe if you want some random recipe. \n ' \
                             'Try /searchByName if you are looking for a special recipe.'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def get_random_recipes(update,context):
    response = api.get_random_recipes(number=5)
    #print(response)
    recipes = response.json()['recipes']
    print(recipes)
    text = "5 ideas for your meal prep  :\n\n"
    for i in range(len(recipes)):
        text += "{0}. {1} (link: {2})\n".format(i+1,recipes[i]['title'],recipes[i]['sourceUrl'])   
    text += '\n Which recipe would you like to have info on ? \n'
    buttons = [[InlineKeyboardButton("Recipe number 1", callback_data='1')],
               [InlineKeyboardButton("Recipe number 2", callback_data='2')],
               [InlineKeyboardButton("Recipe number 3", callback_data='3')],
               [InlineKeyboardButton("Recipe number 4", callback_data='4')],
               [InlineKeyboardButton("Recipe number 5", callback_data='5')]]
    reply_markup = InlineKeyboardMarkup(buttons)

    update.message.reply_text(text, reply_markup= reply_markup)
    
def buttonHandler(update, context):
    print("button pressed")
    query = update.callback_query
    print(query.data)
    query.answer()
    print(query.data)
    print(recipes[int(query.data)-1]['title'])
    text = "Selected recipe: "+ recipes[int(query.data)-1]['title']
    print(text)
    query.edit_message_text(text=text)
    message = 'Here is the link to the recipe :\n'+ recipes[int(query.data)-1]["sourceUrl"]
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message, disable_web_page_preview=False)

def main():
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('randomRecipe', get_random_recipes))
    #dp.add_handler(CommandHandler('searchByName'))
    #dp.add_handler(MessageHandler(Filters.text, get_news_with_keyword))
    dp.add_handler(CallbackQueryHandler(buttonHandler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    api = sp.API("1ad42e955fd3498aa44b7e9861cb717c")
    with open('tokens.txt','r') as tokens_file :
        tokens = json.load(tokens_file)
        bot_token = tokens["Bot Token"]
        apikey = tokens["Recipe API key"]
    main()