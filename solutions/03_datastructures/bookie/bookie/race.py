# Create datatypes for these elements:

# * Horse (name, owner, rating)
# * Race (name, horses, status, winner)
# * Race status (planned, bet-able, started, finish, cancelled)
# * Bet (race, horse, amount, redeemed)
# * Player (name, balance, bets)
# * Bank (balance, players, races)

import typing as t
from enum import Enum

class Horse(t.NamedTuple):
    name: str
    owner: str
    rating: float

class RaceStatus(Enum):
    PLANNED = 'planned'
    BET_ABLE = 'bet_able'
    STARTED = 'started'
    FINISH = 'finish'
    CANCELLED = 'cancelled'

class Race(t.NamedTuple):
    name: str
    horses: list[Horse]
    status: RaceStatus
    winner: Horse | None

