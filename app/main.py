from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from handlers.constants import SEND_MESSAGE_STATE
from handlers.errors import error_handler
from handlers.chats import (
    get_all_chats_handler, quit_chat_handler,
    send_message_to_chat_handler,
    set_chat_listener_handler, start_dialog_handler
)
from settings import get_settings

from handlers.base import start_handler


def get_app():
    settings = get_settings()
    application = ApplicationBuilder().token(settings.TG_BOT_TOKEN).build()

    start_command_handler = CommandHandler('start', start_handler)
    get_all_chats_command_handler = CommandHandler(
        'chats',
        get_all_chats_handler,
    )
    set_chat_listener_command_handler = CommandHandler(
        'listen_chat',
        set_chat_listener_handler,
    )
    start_dialog_command_handler = CommandHandler(
        'start_dialog',
        start_dialog_handler
    )
    quit_chat_command_handler = CommandHandler('quit', quit_chat_handler)
    send_chat_messages_conversation_handler = ConversationHandler(
        entry_points=[start_dialog_command_handler],
        states={
            SEND_MESSAGE_STATE: [
                MessageHandler(
                    filters=filters.TEXT & ~ filters.COMMAND,
                    callback=send_message_to_chat_handler,
                )
            ]
        },
        fallbacks=(quit_chat_command_handler, )
    )

    application.add_handler(start_command_handler)
    application.add_handler(get_all_chats_command_handler)
    application.add_handler(set_chat_listener_command_handler)
    application.add_handler(send_chat_messages_conversation_handler)

    application.add_error_handler(error_handler, block=True)

    return application


if __name__ == "__main__":
    get_app().run_polling()
