import uuid
import datetime

class Event:
    def __init__(self, name:str, stream:uuid.UUID, version:int, data:dict, headers:dict, created:datetime.datetime=None):
        pass

