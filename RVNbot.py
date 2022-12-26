import requests
import telegram
import time
import configparser
import requests
from telegram.ext import Updater, CommandHandler

def get_miner_status(api_key):
    # Set the API endpoint URL
    API_URL = "https://api.nanopool.org/v1/rvn/user/{API_KEY}"

    # Make the API request
    response = requests.get(API_URL, params={"api_key": api_key})

    # Check the status code of the response
    if response.status_code == 200:
        # The request was successful, so parse the response
        data = response.json()
        # Return the miner's status
        return data['status']
    else:
        # The request was not successful, so return an error message
        return "An error occurred while retrieving the miner's status"

def start(update, context):
    # Prompt the user for their API key
    api_key = input("Please enter your API key: ")

    # Prompt the user for the hash of their miner
   #miner_hash = input("Please enter the hash of your miner: ")

    # Get the miner's status
    miner_status = get_miner_status(api_key)

    # Send the miner's status to the user
    update.message.reply_text("Miner status: {}".format(miner_status))

def main():
    # Read the bot token from the configuration file
    config = configparser.ConfigParser()
    config.read("config.ini")
    bot_token = config["DEFAULT"]["bot_token"]
 
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(bot_token, use_context=True)
   
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add the start command handler
    dp.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

