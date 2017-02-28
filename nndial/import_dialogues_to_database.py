import configparser
import csv

import pymongo

import nndial.corpora_names as cn
from nndial import persistence
from nndial.util import dict as du



def get_rows(file_path):
    data_file = open(file_path, 'r')
    data_reader = csv.DictReader(data_file, delimiter=';')

    read_rows = []
    for row in data_reader:
        read_rows.append(row)

    data_file.close()

    return read_rows

# read configuration
config = configparser.ConfigParser()
config.read('local_config.ini')

coll_dialogues = persistence.get_collection(persistence.Collection.dialogues)

data_directory = config.get('environment', 'data_directory')

file_experiment = data_directory + '/data/annotatedData_corrected.csv'


corpora_files = {
    cn.REAL_USER: file_experiment
}

SUCCESS = ["S", "SCs", "SN", "SCu", "SCuCs"]
NO_SUCCESS = ["FS", "FU"]

# create unique index for corpus, iteration and exchange_no in order to prevent
# multiple insertions of the same dialogue
coll_dialogues.create_index([("corpus", pymongo.ASCENDING), ("iteration", pymongo.ASCENDING),
                             ("exchange_no", pymongo.ASCENDING)], unique=True)

for corpus in corpora_files.keys():
    print("Corpus: " + str(corpus))
    print("Read rows")
    rows = get_rows(corpora_files[corpus])

    for r in rows:
        du.replace_dots_in_keys(r)
        du.convert_string_to_integer(r, ["iteration", "exchange_no"])
        r.update({"corpus": corpus.name})

    print("Write rows to collection '{0}'".format(coll_dialogues))

    coll_dialogues.insert(rows)

# create index for corpora and iteration
coll_dialogues.create_index([("corpus", pymongo.ASCENDING), ("iteration", pymongo.ASCENDING)])
# create index for iteration
coll_dialogues.create_index([("iteration", pymongo.ASCENDING)])


persistence.close()

