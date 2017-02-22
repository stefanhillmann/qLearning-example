"""
Created on Tue Feb 22 15:52:10 2017

@author: Stefan Hillmann (stefan.hillmann@tu-berlin.de)
"""
from pymongo import MongoClient
import configparser
from enum import Enum

config = configparser.ConfigParser()
config.read('local_config.ini')


class Collection(Enum):
    dialogues = 1


COLLECTION_NAMES = {
    Collection.dialogues: "dialogues"
}


class Database(Enum):
    production = 1
    unit_testing = 2


DATABASE_NAMES = {
    Database.production: "nn_on_dialogues",
    Database.unit_testing: "UNITTEST_nn_on_dialogues"
}

current_database = Database.production


class DbClient(object):
    __state = {}

    def __init__(self, host, port):
        self.__dict__ = self.__state
        self.host = host
        self.port = port

    def connect(self):
        try:
            # does client exist?
            self.client
        except AttributeError:
            # no! Create it!
            print("Create MongoClient.")
            self.client = MongoClient(self.host, self.port, connect=False)

    def get_connection(self, database):
        self.connect()
        if type(database) is not Database:
            raise TypeError(
                "Parameter database has to be from type Database (see persistence.py). Current type and value: {0} ({1}".format(
                    type(database), str(database)
                ))

        return self.client[DATABASE_NAMES[database]]

    def close(self):
        self.client.close()

    def reset(self):
        self.close()
        self.client = MongoClient(self.host, self.port, connect=False)

host = "host"
port = 0
if config.has_section('database'):
    host = config.get('database', 'host')
    port = config.getint('database', 'port')
else:
    print('Could not load database configuration. Empty values are used.')

db_client = DbClient(host, port)


def close():
    db_client.close()


def reset():
    db_client.reset()


def get_collection(collection):
    if type(collection) is not Collection:
        raise TypeError("Parameter collection has to be from type Collection (see persistence.py.")

    db_connection = db_client.get_connection(current_database)
    collection_name = COLLECTION_NAMES[collection]
    return db_connection[collection_name]


def get_collection_name(collection):
    if type(collection) is not Collection:
        raise TypeError("Parameter collection has to be from type Collection (see persistence.py.")
    return COLLECTION_NAMES[collection]



