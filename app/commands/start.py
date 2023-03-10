from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""Hello!\n\nI\'m ready to take note of your options\n\nUse <code>/help</code> for instructions""",
        parse_mode='HTML'
    )
