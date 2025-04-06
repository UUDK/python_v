from dataclasses import dataclass, field

from .race import Horse, Race, RaceStatus


@dataclass
class Bet:
    ...

@dataclass
class Player:
    ...

@dataclass
class Bank:
    ...

    def add_race(self, race_name: str) -> None:
        ...

    def find_race(self, race_name: str) -> Race | None:
        ...

    def add_player(self, player_name: str, deposit: int):
        ...

    def find_player(self, player_name: str):
        ...

    def add_bet(self, player_name: str, race_name: str, horse_name: str, amount: int):
        ...

    def pay_out(self):
        ...