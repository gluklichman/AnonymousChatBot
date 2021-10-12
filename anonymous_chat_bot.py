import telebot
import sys

users=[]
messages=[]

def try_add_user(userId):
    if userId not in users :
        users.append(userId)
        print("User ", userId, "added to list")
        print(users)


print("Configuring bot...")
with open ("token", "r") as tokenfile:
    token = tokenfile.read().replace('\n', '')

bot = telebot.TeleBot(token, parse_mode=None)
print("Configuring bot complete")

#message hanlers
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try_add_user(message.from_user.id)

@bot.message_handler(func = lambda m: True)
def echo_all(message):
    print("Message from user: ", message.from_user.id)
    print("Message chat: ", message.chat.id)
    try_add_user(message.from_user.id)
    bot.send_message(message.chat.id, message.text)
    bot.delete_message(message.chat.id, message.id)

print("Start listening...")
bot.infinity_polling()
