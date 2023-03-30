from typing import Protocol, TypeVar


class ProtocolT(Protocol):
    def __init__(self, *args, **kwargs):
        pass


TypeT = TypeVar('TypeT', bound=ProtocolT)
