# Create datatypes for these elements:

# * Horse (name, owner, rating)
# * Race (name, horses, status, winner)
# * Race status (planned, bet-able, started, finish, cancelled)
# * Bet (race, horse, amount, redeemed)
# * Player (name, balance, bets)
# * Bank (balance, players, races)

import typing as t

from .race import Horse, Race


class Bet(t.NamedTuple):
    race: Race
    horse: Horse
    amount: int
    redeemed: bool

class Player(t.NamedTuple):
    name: str
    balance: int
    bets: list[Bet]

class Bank(t.NamedTuple):
    balance: int
    players: list[Player]
    races: list[Race]
