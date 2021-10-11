import telebot
import sys

print("Configuring bot...")
with open ("token", "r") as tokenfile:
    token = tokenfile.read().replace('\n', '')

bot = telebot.TeleBot(token, parse_mode=None)
print("Configuring bot complete")

#message hanlers
@bot.message_handler(func = lambda m: True)
def echo_all(message):
    print("Message from user: ", message.from_user.id)
    print("Message chat: ", message.chat.id)
    bot.reply_to(message, message.text)

print("Start listening...")
bot.infinity_polling()
