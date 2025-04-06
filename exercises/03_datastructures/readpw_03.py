# Read the file and place the data in two dictionaries of named tuples,
# one dictionary with login as key, the other with uid as key

# login, pw, uid, gid, gecos, homedir, shell

import typing as t
from pprint import pprint


class PwTuple(t.NamedTuple):
    ...

with open("passwd.txt", "r", encoding="utf-8") as f:
    data_list = []
    data_by_login = ...
    data_by_uid = ...
    for line in f:
        line = line.rstrip()
        record = tuple(line.split(":"))
        pw_record = PwTuple(
            ...
        )
        data_list.append(record)
        data_by_login # ...
        data_by_uid # ...

pprint(data_list, width=120)
pprint(data_by_login, width=120)
pprint(data_by_uid, width=120)
