from dataclasses import dataclass
import json

from exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class BaseWebException(ApplicationException):
    status_code: int
    response_content: str

    @property
    def response_json(self) -> dict:
        return json.loads(self.response_content)

    @property
    def error_text(self) -> str:
        return self.response_json.get('detail', {}).get('error', '')


@dataclass(frozen=True, eq=False)
class ChatListRequestError(BaseWebException):
    @property
    def message(self):
        return 'Chat list request error'


@dataclass(frozen=True, eq=False)
class ListenerListRequestError(BaseWebException):
    @property
    def message(self):
        return 'Listener list request error'


@dataclass(frozen=True, eq=False)
class ListenerAddRequestError(BaseWebException):
    @property
    def message(self):
        return 'Listener add request error'


@dataclass(frozen=True, eq=False)
class ChatInfoRequestError(BaseWebException):
    @property
    def message(self):
        return 'Chat info request error'
