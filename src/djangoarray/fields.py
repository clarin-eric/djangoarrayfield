from django.db.models import JSONField
from json import JSONDecoder, JSONEncoder
from typing import Generic

from .generics import TypeT
from .serializers import DjangoArrayDecoder, DjangoArrayEncoder


class DjangoArrayField(Generic[TypeT], JSONField):
    def __init__(self, name: str, verbose_name: str,
                 encoder: JSONEncoder = DjangoArrayEncoder[TypeT],
                 decoder: JSONDecoder = DjangoArrayDecoder[TypeT]):
        self.array_field: JSONField = JSONField(encoder=encoder, decoder=decoder)
        super().__init__(name=name, verbose_name=verbose_name, encoder=DjangoArrayEncoder, decoder=DjangoArrayDecoder)
