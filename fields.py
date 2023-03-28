from django.db.models import JSONField
from typing import Generic

from .fields import DjangoArrayField
from .generics import ProtocolT, TypeT
from .serializers import DjangoArrayDecoder, DjangoArrayEncoder


class DjangoArrayField(Generic[TypeT], JSONField):
    def __init__(self):
        self.array_field: JSONField = JSONField(encoder=DjangoArrayEncoder[TypeT], decoder=DjangoArrayDecoder[TypeT])
        super().__init__(verbose_name=f"ArrayField[{TypeT}]", encoder=DjangoArrayEncoder, decoder=DjangoArrayDecoder)
