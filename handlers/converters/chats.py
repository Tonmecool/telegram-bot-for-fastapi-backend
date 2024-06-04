from dtos.messages import ChatListItemDTO


def convert_chats_dtos_to_message(chats: list[ChatListItemDTO]) -> str:
    return '\n'.join(
        (
            'Список всех доступных чатов:\n', '\n'.join(
                (
                    f'ChatOID: {chat.oid}. '
                    f'\nПроблема: {chat.title}\n'
                    for chat in chats
                )
            )
        )
    )
