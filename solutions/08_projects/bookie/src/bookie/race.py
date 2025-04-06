# * Rewrite the bookmaker system as object oriented
# * The datatypes should be made into classes
# * The functions should be made into methods


from dataclasses import dataclass, field
from enum import Enum

@dataclass
class Horse:
    name: str
    owner: str
    rating: float

class RaceStatus(Enum):
    PLANNED = 'planned'
    BET_ABLE = 'bet_able'
    STARTED = 'started'
    FINISH = 'finish'
    CANCELLED = 'cancelled'

@dataclass
class Race:
    name: str
    horses: list[Horse] = field(default_factory=list)
    status: RaceStatus = RaceStatus.PLANNED
    winner: Horse | None = None

    def add_horse(self, horse_name: str, odds: float):
        self.horses.append(Horse(name=horse_name, owner="", rating=odds))

    def find_horse(self, horse_name: str) -> Horse | None:
        for horse in self.horses:
            if horse.name == horse_name:
                return horse
        return None
