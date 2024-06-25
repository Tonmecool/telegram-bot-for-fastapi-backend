from telegram.ext import ApplicationBuilder, CommandHandler

from handlers.chats import get_all_chats_handler
from settings import get_settings

from handlers.base import start_handler


def get_app():
    settings = get_settings()
    application = ApplicationBuilder().token(settings.TG_BOT_TOKEN).build()

    start_command_handler = CommandHandler('start', start_handler)
    get_all_chats_command_handler = CommandHandler(
        'chats',
        get_all_chats_handler
    )
    application.add_handler(start_command_handler)
    application.add_handler(get_all_chats_command_handler)

    return application


if __name__ == "__main__":
    get_app().run_polling()
