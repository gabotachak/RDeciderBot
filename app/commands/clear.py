import logging

from telegram import Update
from telegram.ext import ContextTypes

import app


async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not app.options:
        logging.warning("There's nothing to clear")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="There's nothing to clear!")
        return

    app.options.clear()
    logging.info('Cleared the list')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='List cleared!')
