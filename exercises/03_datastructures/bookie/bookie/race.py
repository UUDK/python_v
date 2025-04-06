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
    ...

class RaceStatus(Enum):
    ...

class Race(t.NamedTuple):
    ...
