from telegram.ext import ApplicationBuilder, CommandHandler

from app.commands.add import add
from app.commands.choose import choose
from app.commands.clear import clear
from app.commands.delete import delete
from app.commands.help import help_command
from app.commands.see import see
from app.commands.start import start
from app.config import R_DECIDER_BOT_TOKEN

COMMAND_HANDLERS = {
    'add': add,
    'choose': choose,
    'clear': clear,
    'delete': delete,
    'decide': choose,
    'help': help_command,
    'list': see,
    'start': start,
}

options = []


def create_app():
    """ Create Telegram Bot """
    application = ApplicationBuilder().token(R_DECIDER_BOT_TOKEN).build()

    for name, handler in COMMAND_HANDLERS.items():
        application.add_handler(CommandHandler(name, handler))

    return application
