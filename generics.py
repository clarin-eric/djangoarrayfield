import json
from json import JSONDecoder, JSONEncoder
from django.db.models import JSONField
from typing import Generic, Iterable, List, Protocol, Union, Type, TypeVar


class ProtocolT(Protocol):
    def __init__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass

    def __dict__(self):
        pass


TypeT = TypeVar('TypeT', bound=ProtocolT)
