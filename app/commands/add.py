import logging

from telegram import Update
from telegram.ext import ContextTypes

import app


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    to_add = ' '.join(context.args)
    if not to_add:
        logging.error('No argument passed to add')
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please write something to add')
        return

    if to_add in app.options:
        logging.warning(f'{to_add} is already on the list')
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{to_add} is already on the list')
        return

    app.options.append(to_add)
    logging.info(f'Added {to_add} to the list')
    logging.info(f'List is now: {app.options}')

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{to_add} added!')
