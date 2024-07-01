import re
from telegram import Update
from telegram.ext import ContextTypes

from containers.factories import get_container
from handlers.constants import SEND_MESSAGE_STATE
from handlers.converters.chats import convert_chats_dtos_to_message
from services.web import BaseChatWebService


async def get_all_chats_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    container = get_container()

    async with container() as request_container:
        service = await request_container.get(BaseChatWebService)
        chats = await service.get_all_chats()

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=convert_chats_dtos_to_message(chats=chats),
            parse_mode='MarkdownV2',
        )


async def set_chat_listener_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    container = get_container()

    async with container() as request_container:
        service = await request_container.get(BaseChatWebService)
        await service.add_listener(
            telegram_chat_id=update.effective_chat.id,
            chat_oid=context.args[0],
        )

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You connect in chat successfully',
            parse_mode='MarkdownV2',
        )


async def start_dialog_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='You are currently in a conversation. Reply to the message and the user will see it',    # noqa
        )

    return SEND_MESSAGE_STATE


async def quit_chat_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Quit chat successfully',
        parse_mode='MarkdownV2',
    )


async def send_message_to_chat_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):
    if update.message.reply_to_message is None:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Error! Reply to the message you are responding to',
        )
        return

    try:
        chat_oid = re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', update.message.reply_to_message.text).group(0)   # noqa
    except IndexError:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='It is necessary to reply specifically to the user`s message',
        )
        return
    print(chat_oid)
