from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class ChatListRequestError(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return 'Chat list request error'


class ListenerListRequestError(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return 'Listener list request error'
