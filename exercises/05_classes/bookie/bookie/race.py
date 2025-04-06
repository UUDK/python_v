# * Rewrite the bookmaker system as object oriented
# * The datatypes should be made into classes
# * The functions should be made into methods


from dataclasses import dataclass, field
from enum import Enum

@dataclass
class Horse:
    ...

class RaceStatus(Enum):
    PLANNED = 'planned'
    BET_ABLE = 'bet_able'
    STARTED = 'started'
    FINISH = 'finish'
    CANCELLED = 'cancelled'

@dataclass
class Race:
    ...

    def add_horse(self, horse_name: str, odds: float):
        ...

    def find_horse(self, horse_name: str) -> Horse | None:
        ...
