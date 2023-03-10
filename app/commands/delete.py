import logging

from telegram import Update
from telegram.ext import ContextTypes

import app


async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    to_delete = ' '.join(context.args)
    if not to_delete:
        logging.error('No argument passed to delete')
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Please write something to delete')
        return

    if to_delete not in app.options:
        logging.warning(f'{to_delete} is not on the list')
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{to_delete} is not on the list')
        return

    app.options.remove(to_delete)
    logging.info(f'Deleted {to_delete} from the list')
    logging.info(f'List is now: {app.options}')

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{to_delete} deleted!')
