import json
from typing import Callable, Generic, Iterable, List, Union

from .generics import ProtocolT, TypeT


class DjangoArrayDecodingException(Exception):
    """
        Exception raised inside djangoarrayfield.DjangoArrayDecoder
    """
    def __init__(self, obj: str, message: Union[str, None] = None,  _type: TypeT = TypeT):
        if message is None:
            self.message: str = f"Error when decoding array of {TypeT} type objects.\nSource representation:\n{obj}"
        else:
            self.message = message
        self._type: TypeT = TypeT
        super().__init__(self.message)


class DjangoArrayEncodingException(Exception):
    """
        Exception raised inside djangoarrayfield.DjangoArrayEncoder
    """
    def __init__(self, obj: Iterable[ProtocolT], message: Union[str, None] = None, _type: TypeT = TypeT):
        if message is None:
            self.message: str = f"Error when encoding array of {TypeT} type objects\nInput container: {list(obj)}"
        else:
            self.message: str = message
        self._type: TypeT = TypeT
        super().__init__(self.message)


class DjangoArrayEncoder(Generic[TypeT], json.JSONEncoder):
    """
        Generic array decoder for Django, built on top of json.JSONDecoder
    """
    def __init__(self):
        super().__init__()

    def default(self, obj: Iterable[ProtocolT]):
        """
            Returns deserialized array of objects of generic type TypeT
        """
        try:
            ret: Iterable[dict] = [o.__dict__() for o in obj]
        except TypeError as e:
            raise DjangoArrayEncodingException(obj=obj, _type=TypeT) from e
        return ret


class DjangoArrayDecoder(Generic[TypeT], json.JSONDecoder):
    """
        Generic array decoder for Django, built on top of json.JSONEncoder
    """
    def __init__(self):
        super().__init__()

    def decode(self, s: str, _w: Callable[..., TypeT] = ...) -> List[TypeT]:
        # method's signature differs from docs: https://docs.python.org/3/library/json.html,
        # TODO figure out what _w does

        json_obj = json.loads(s)
        return [TypeT.__init__(o) for o in json_obj]
