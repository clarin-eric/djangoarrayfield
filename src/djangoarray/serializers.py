import json
from typing import Callable, Generic, Iterable, List, Union

from .generics import ProtocolT, TypeT
from .utils import is_primitive


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
    def __init__(self, objs: Iterable[TypeT], message: Union[str, None] = None, _type: TypeT = TypeT):
        if message is None:
            self.message: str = f"Error when encoding array of {TypeT} type objects\nInput container: {list(objs)}"
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

    def default(self, objs: Iterable[TypeT]):
        """
            Returns deserialized array of objects of generic type TypeT
        """
        try:
            if not isinstance(objs, Iterable):
                raise TypeError("Input parameter objs is {type(objs)} and is not Iterable")
            if all([is_primitive(obj) for obj in objs]):
                ret: Iterable[str] = [obj.__str__() for obj in objs]
            elif all([hasattr(obj, "__dict__") for obj in objs]):
                ret: Iterable[dict] = [dict(obj) for obj in objs]
            else:
                raise TypeError("Members of input objs: Iterable do not to support neither __str__ nor __dict__")
        except TypeError as e:
            raise DjangoArrayEncodingException(objs=objs, _type=TypeT) from e
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
