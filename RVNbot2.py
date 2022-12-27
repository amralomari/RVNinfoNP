import configparser
import requests
import telegram

# Read the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the API token from the configuration file
api_token = config['DEFAULT']['API_TOKEN']

# Initialize the bot using the API token
bot = telegram.Bot(token=api_token)

# Replace API_KEY with your Nanopool API key
API_KEY = 'RJse7jdq4WfSgcJozssAec4Kio4cbhsNdz'

def handle_message(update_id, message):
  # Check if the message is a command to get the miner's status
  if message.text.lower() == '/status':
    # Send a message asking the user for their address
    bot.send_message(chat_id=message.chat_id, text='Please enter your Nanopool address:')

    # Wait for the user to respond with their address
    address = None
    while address is None:
      updates = bot.get_updates(offset=update_id, timeout=10)
      for update in updates:
        update_id = update.update_id + 1
        if update.message.text.startswith('0x'):
          address = update.message.text
          break

    # Make an HTTP GET request to the Nanopool API to get the miner's status
    response = requests.get(f'https://api.nanopool.org/v1/rvn/user/{address}') 

    data = response.json()

    # Extract the relevant information from the API response and format it into a message
    message_text = f'Miner status: {data["status"]}\n'
    message_text2 = f'Hashrate: {data["data"]["hashrate"]} MH/s\n'
    message_text3 = f'Unpaid balance: {data["data"]["unconfirmed_balance"]} RVN\n'
    message_text4 = f'Balance: {data["data"]["balance"]}'

    # Use the Telegram API to send the message back to the user
    bot.send_message(chat_id=message.chat_id, text=message_text + message_text2 + message_text3 + message_text4)

# Set up a loop to continuously listen for incoming messages
update_id = None
while True:
  updates = bot.get_updates(offset=update_id, timeout=10)
  for update in updates:
    update_id = update.update_
