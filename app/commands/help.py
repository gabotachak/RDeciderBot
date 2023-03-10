from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="""&#8226; Just use <code>/add 'new option'</code> to add an option into the list\n\n&#8226; When you're ready use <code>/choose</code> or <code>/decide</code> to pick one\n\n&#8226; Wanna see the list?\n\t\t\t\tUse <code>/list</code>\n\n&#8226; Wanna clear the list?\n\t\t\t\tUse <code>/clear</code>\n\n&#8226; Wanna delete a specific option?\n\t\t\t\tUse <code>/delete 'option to delete'</code>, please be specific""",
        parse_mode='HTML'
    )
