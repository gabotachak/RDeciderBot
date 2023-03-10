import logging
from random import choice

from telegram import Update
from telegram.ext import ContextTypes

import app


async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not app.options:
        logging.warning("There's nothing to choose from")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="There's nothing to choose from!")
        return

    chosen = choice(app.options)
    logging.info(f'Chose {chosen}')
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Congrats, {chosen} won!')
