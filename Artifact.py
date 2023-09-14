import datetime
from datetime import datetime


def check_values(types):
    id, name, artist, year, value = types
    if type(name) is not str:
        raise ValueError("Name needs to be string")
    if type(artist) is not str:
        raise ValueError("Artist needs to be string")
    if type(year) is not int:
        raise ValueError("Year needs to be integer")
    if type(value) is not float:
        raise ValueError("Value needs to be float")
    if type(id) is not int:
        raise ValueError("Id needs to be int")


class Artifact:

    def __init__(self, id, name, artist, year, value):
        types = (id, name, artist, year, value)
        check_values(types)
        self.id = id
        self.name = name
        self.artist = artist
        self.year = year
        self.value = value

    def __str__(self):
        return "ID:{} ,Name:{}, Artist:{}, Year:{}, Value:{} .".format(self.id, self.name
                                                                     , self.artist, self.year, self.value)

    def set_value(self, new_value):
        if type(new_value) is not float:
            raise ValueError("Value needs to be float")
        self.value = new_value

    def get_age(self):
        return datetime.now().year - self.year

    @classmethod
    def new_item(cls, id, name, artist, year, value):
        return Artifact(id, name,artist,year,value)

