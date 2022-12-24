import requests
import telegram
import time

# Replace TOKEN with the API token for your bot, which you can get from the BotFather
bot = telegram.Bot(token='5918737230:AAFkh98WdqYIo0mAAsZyK54d1kgsHgiDU18')

# Replace API_KEY with your Nanopool API key
API_KEY = 'RJse7jdq4WfSgcJozssAec4Kio4cbhsNdz'

def handle_message(message):
  # Check if the message is a command to get the miner's status
  if message.text.lower() == '/status':
    # Make an HTTP GET request to the Nanopool API to get the miner's status
    #response = requests.get(f'https://api.nanopool.org/v1/eth/status?apikey={API_KEY}')
    response = requests.get(f'https://api.nanopool.org/v1/rvn/user/{API_KEY}') 

    data = response.json()

    # Extract the relevant information from the API response and format it into a message
    message_text = f'Miner status: {data["status"]}\n'
    message_text2 = f'Hashrate: {data["data"]["hashrate"]} MH/s\n'
    #message_text += f'Hashrate: {data["hashrate"]} MH/s\n'
    message_text3 = f'Unpaid balance: {data["data"]["unconfirmed_balance"]} RVN\n'
    message_text4 = f'Balance: {data["data"]["balance"]}'

    # Use the Telegram API to send the message back to the user
    bot.send_message(chat_id=message.chat_id, text=message_text + message_text2 + message_text3 + message_text4)

#def check_status():
  # Make an HTTP GET request to the Nanopool API to get the miner's status
 #3 response = requests.get(f'https://api.nanopool.org/v1/rvn/user/{API_KEY}')
  #data = response.json()

  # Check if the status is "false"
  #if data["status"] == "false":
    # Send a notification to the user
   # bot.send_message(text='The miner is not running!')

# Set up a loop to check the status every 15 minutes
#while True:
  
 # check_status()
 # time.sleep(900)  # pause for 15 minutes (900 seconds)
 # updates = bot.get_updates(offset=update_id, timeout=10)
 # for update in updates:
  #  update_id = update.update_id + 1
   # handle_message(update.message)

# Set up a loop to continuously listen for incoming messages
update_id = None
while True:
  updates = bot.get_updates(offset=update_id, timeout=10)
  for update in updates:
    update_id = update.update_id + 1
    handle_message(update.message)