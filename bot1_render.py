
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Tokeningiz endi yashirin saqlanadi
TOKEN = os.getenv("TOKEN")

# /start komandasi uchun
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✅ Ha", callback_data='yes')],
        [InlineKeyboardButton("❌ Yo‘q", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Salom! Davom etamizmi?", reply_markup=reply_markup)

# Inline tugma bosilgandagi javob
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'yes':
        await query.edit_message_text("Zo‘r! Davom etamiz 💪")
    elif query.data == 'no':
        await query.edit_message_text("Mayli, keyinroq ko‘rishamiz 👋")

# /menu komandasi uchun menyu
async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🍳 Nonushta", callback_data='breakfast')],
        [InlineKeyboardButton("🍛 Tushlik", callback_data='lunch')],
        [InlineKeyboardButton("🍲 Kechki ovqat", callback_data='dinner')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🍽 Menyudan tanlang:", reply_markup=reply_markup)

# Menyu tugmalari bosilganda
async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'breakfast':
        await query.edit_message_text("🍳 Nonushta: tuxum, non, choy")
    elif query.data == 'lunch':
        await query.edit_message_text("🍛 Tushlik: palov, salat, kompot")
    elif query.data == 'dinner':
        await query.edit_message_text("🍲 Kechki ovqat: sho‘rva, non, qatiq")
    else:
        await query.edit_message_text("Nomaʼlum tanlov!")

# Asosiy ishga tushurish funksiyasi
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", show_menu))
    app.add_handler(CallbackQueryHandler(menu_handler))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == '__main__':
    main()
