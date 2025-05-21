import telebot
from telebot import types
import os
import TOKEN

BOT_TOKEN = TOKEN.BOT_TOKEN
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="искать крутышек", callback_data="button_pressed")
    kb.add(btn1)
    bot.reply_to(message, "каких крутышов посмотрим сегодня?💕", reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "button_pressed":
        bot.send_photo(call.message.chat.id, 'https://cdn.discordapp.com/attachments/993582152375607367/1370503418531151872/susRender.png?ex=681fbc45&is=681e6ac5&hm=3bcd3922b30e499695a92a5c184a926e270eb355cd1c49757e1602473535a6e0&')
        kb = types.InlineKeyboardMarkup(row_width=1)
        btnn1 = types.InlineKeyboardButton(text="ещё каво та", callback_data="button_pressed2")
        btnn2 = types.InlineKeyboardButton(text="написать зайке", callback_data="DoNothing")
        kb.add(btnn1, btnn2)
        bot.send_message(call.message.chat.id, "ищу парня пол не важен, люблю макарошки кста UWU", reply_markup=kb)
    elif call.data == "button_pressed2":
        bot.send_photo(call.message.chat.id, "https://cdn.discordapp.com/attachments/993582152375607367/1370505725607936153/Untitled.png?ex=681fbe6b&is=681e6ceb&hm=0bacb6f3d37282c1b3a439188750471373f43124107f83d0407baa1c5a74965f&")
        kb = types.InlineKeyboardMarkup(row_width=1)
        btnn1 = types.InlineKeyboardButton(text="дальшее, фу бош нищ какой то", callback_data="button_pressed3")
        kb.add(btnn1)
        bot.send_message(call.message.chat.id, "люблю вайб седьмой винды и в майнкрафтик покатать, а ты?💖", reply_markup=kb)
    elif call.data == "DoNothing":
        bot.send_message(call.message.chat.id, "я не знаю что делать с этой кнопкой, но ты можешь написать мне в лс, если хочешь💖")
    elif call.data == "button_pressed3":
        bot.send_photo(call.message.chat.id, 'https://cdn.discordapp.com/attachments/993582152375607367/1370514544719302796/129eba52d364e926b24ca4dcc0500a3c.jpg?ex=681fc6a2&is=681e7522&hm=d155089a2f155651a9ee9161ef1e45186d5d89cad2260a2aadf7852603e95548&')
    # Acknowledge the callback query
    bot.answer_callback_query(call.id)

bot.infinity_polling()