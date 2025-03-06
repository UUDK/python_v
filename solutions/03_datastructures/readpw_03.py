# Read the file and place the data in two dictionaries of named tuples,
# one dictionary with login as key, the other with uid as key

import typing as t
from pprint import pprint


class PwTuple(t.NamedTuple):
    login: str
    pw: str
    uid: int
    gid: int
    gecos: str
    homedir: str
    shell: str


with open("passwd.txt", "r", encoding="utf-8") as f:
    data_list = []
    data_by_login = {}
    data_by_uid = {}
    for line in f:
        line = line.rstrip()
        # print(line)
        record = tuple(line.split(":"))
        pw_record = PwTuple(
            login=record[0],
            pw=record[1],
            uid=int(record[2]),
            gid=int(record[3]),
            gecos=record[4],
            homedir=record[5],
            shell=record[6],
        )
        data_list.append(record)
        data_by_login[pw_record.login] = pw_record
        data_by_uid[pw_record.uid] = pw_record

pprint(data_list, width=120)
pprint(data_by_login, width=120)
pprint(data_by_uid, width=120)
