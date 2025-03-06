# Make an Enum with
#  1 being bash,
#  2 being ksh,
#  3 being tcsh,
#  4 being zsh.
# Use it in the data structure

import typing as t
from pprint import pprint
from enum import Enum


class ShellTypes(Enum):
    BASH = 1
    KSH = 2
    TCSH = 3
    ZSH = 4
    UNKNOWN = 0


conv_shell = {
    "/bin/bash": ShellTypes.BASH,
    "/bin/ksh": ShellTypes.KSH,
    "/bin/tcsh": ShellTypes.TCSH,
    "/bin/zsh": ShellTypes.ZSH,
}


class PwTuple(t.NamedTuple):
    login: str
    pw: str
    uid: int
    gid: int
    gecos: str
    homedir: str
    shell: ShellTypes


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
            shell=conv_shell.get(record[6], ShellTypes.UNKNOWN),
        )
        data_list.append(record)
        data_by_login[pw_record.login] = pw_record
        data_by_uid[pw_record.uid] = pw_record

pprint(data_list, width=120)
pprint(data_by_login, width=120)
pprint(data_by_uid, width=120)
