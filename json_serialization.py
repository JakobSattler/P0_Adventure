import json
import os

jsonClasses = []

def json_class(klass):
    jsonClasses.append(klass)
    return klass

class CustomDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if '__class__' not in obj:
            return obj
        type = obj['__class__']

        for klass in jsonClasses:
            if type == klass.__name__:
                return klass(**obj)
        return obj

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        for klass in jsonClasses:
            if isinstance(obj, klass):
                cpy = obj.__dict__.copy()
                cpy["__class__"] = obj.__class__.__name__
                return cpy
        return json.JSONEncoder.default(self, obj)


# Looked up how to use relative path
# https://stackoverflow.com/questions/40416072/reading-file-using-relative-path-in-python-project/40416154
def load_file(savefile):
    with open(savefile, "r") as f:
        return json.load(f, cls=CustomDecoder)

def save_file(gamedata, savefile):
    with open(savefile, "w") as f:
        json.dump(gamedata, f, cls=CustomEncoder, indent=2)