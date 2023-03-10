import logging

from telegram import Update
from telegram.ext import ContextTypes

import app


async def see(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not app.options:
        logging.warning("There's nothing to see")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="There's nothing to see!, please add something first"
        )
        return

    list_string = '\n'.join([f'&#8226; {option}' for option in app.options])
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'<b>List:</b>\n\n{list_string}',
        parse_mode='HTML'
    )
