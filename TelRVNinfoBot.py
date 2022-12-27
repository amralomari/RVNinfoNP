import requests
import telegram

# Replace TOKEN with the API token for your bot, which you can get from the BotFather
bot = telegram.Bot(token='5918737230:AAFkh98WdqYIo0mAAsZyK54d1kgsHgiDU18')

# Replace API_KEY with your Nanopool API key
API_KEY = 'RJse7jdq4WfSgcJozssAec4Kio4cbhsNdz'

def handle_message(message):
  # Check if the message is a command to get the miner's status
  if message.text.lower() == '/status':
    # Make an HTTP GET request to the Nanopool API to get the miner's status
    response = requests.get(f'https://api.nanopool.org/v1/rvn/user/{API_KEY}') 

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
    update_id = update.update_id + 1
    handle_message(update.message)