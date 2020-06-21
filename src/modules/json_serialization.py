from json import JSONEncoder, JSONDecoder
from modules.models import Tenet


class TenetEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class TenetDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        JSONDecoder.__init__(self, object_hook=self.dict_to_object, *args, **kwargs)

    def dict_to_object(self, data):
        if "__type__" not in data:
            return data

        type = data.pop("__type__")

        try:
            tenet_obj = Tenet(**data)
            return tenet_obj
        except:
            data["__type__"] = type
            return data
