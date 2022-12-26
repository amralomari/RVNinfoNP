import requests
import configparser
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
address_handler = None

def get_miner_stats(address):
    # Set the API endpoint URL
    API_URL = "https://api.nanopool.org/v1/rvn/user/address"

    # Make the API request
    response = requests.get(API_URL, params={"address": address})

    # Check the status code of the response
    if response.status_code == 200:
        # The request was successful, so parse the response
        data = response.json()
        # Return the miner's stats
        return data['data']
    else:
        # The request was not successful, so return an error message
        return "An error occurred while retrieving the miner's stats"

def start(update, context):
    global address_handler
    # Send a message asking the user for their address
    update.message.reply_text("Please enter your address:")

    # Set the handler to wait for the user's response
    address_handler = MessageHandler(Filters.text, address_received)
    context.dispatcher.add_handler(address_handler)

def address_received(update, context):
    # Remove the handler for the address
    context.dispatcher.remove_handler(address_handler)

    # Get the user's address
    address = update.message.text

    # Get the miner's stats
    stats = get_miner_stats(address)

    # Send the miner's stats to the user
    update.message.reply_text(f"Miner balance: {status['balance']} RVN\nReported hashrate: {status['hashrate']} MH/s")

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
