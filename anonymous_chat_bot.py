import telebot

print("Configuring bot...")
bot = telebot.TeleBot("", parse_mode=None)
print("Configuring bot complete")

#message hanlers
@bot.message_handler(func = lambda m: True)
def echo_all(message):
    print("Message from user: ", message.from_user.id)
    print("Message chat: ", message.chat.id)
    bot.reply_to(message, message.text)

print("Start listening...")
bot.infinity_polling()
