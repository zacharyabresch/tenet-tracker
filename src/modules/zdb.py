import os
import json

from modules.json_serialization import TenetDecoder, TenetEncoder


class Client(object):
    def __init__(self, location):
        self.database = {}
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()

    def _load(self):
        with open(self.location, "r") as filehandle:
            self.database = json.load(filehandle, cls=TenetDecoder)

    def dumpdb(self):
        try:
            with open(self.location, "w", encoding="utf-8") as filehandle:
                json.dump(self.database, filehandle, cls=TenetEncoder)
                return True
        except IOError:
            return False

    def resetdb(self):
        self.database = {}
        self.dumpdb()
        return True

    def set(self, key, value):
        try:
            self.database[key] = value
            self.dumpdb()
            return True
        except Exception as e:
            print(f"Error saving values to database: {e}")
            return False

    def get(self, key):
        try:
            return self.database[key]
        except KeyError:
            print(f"No value found for key: {key}")
            return False

    def delete(self, key):
        if not key in self.database:
            return False
        del self.database[key]
        self.dumpdb()
        return True
