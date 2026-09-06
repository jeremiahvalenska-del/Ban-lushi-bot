import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler

TOKEN = os.getenv("TOKEN")

PRODUITS = {
    "ban1": {"nom": "Ban Classique Lushi", "prix": "15$"},
    "ban2": {"nom": "Ban Premium Lushi", "prix": "25$"}
}

async def start(update, context):
    kb = [[InlineKeyboardButton("🛒 Voir produits", callback_data="produits")],
          [InlineKeyboardButton("📞 Contact", callback_data="contact")]]
    await update.message.reply_text("Bienvenue chez Ban Lushi 2026 🇨🇩", reply_markup=InlineKeyboardMarkup(kb))

async def buttons(update, context):
    q = update.callback_query
    await q.answer()
    if q.data == "produits":
        kb = [[InlineKeyboardButton(f"{v['nom']} - {v['prix']}", callback_data=k)] for k,v in PRODUITS.items()]
        await q.edit_message_text("Nos produits:", reply_markup=InlineKeyboardMarkup(kb))
    elif q.data in PRODUITS:
        await q.edit_message_text(f"{PRODUITS[q.data]['nom']} - {PRODUITS[q.data]['prix']}\nCommande WhatsApp: +243...")
    else:
        await q.edit_message_text("Contact: Lubumbashi, WhatsApp +243...")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
app.run_polling()
