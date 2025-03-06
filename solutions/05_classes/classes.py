from dataclasses import dataclass, field
from pprint import pprint
import random

FIXED_WINNER = None


@dataclass
class Horse:
    name: str


@dataclass
class Odds:
    odds: float


@dataclass
class RacePos:
    horse: Horse
    pos: int
    odds: Odds


@dataclass
class Race:
    name: str
    horses: dict[int, RacePos] = field(default_factory=dict)
    winner: RacePos | None = None

    def add_horse(self, horse, pos, odds):
        rp = RacePos(horse, pos, odds)
        self.horses[pos] = rp

    def run(self):
        if FIXED_WINNER is not None:
            self.winner = self.horses[FIXED_WINNER]
        else:
            # pass # FIXME
            self.winner = self.horses[random.choice(list(self.horses.keys()))]

    def get_winner(self):
        return self.winner


@dataclass
class Venue:
    name: str
    races: list = field(default_factory=list)

    def add_race(self, race: Race):
        self.races.append(race)


@dataclass
class Bet:
    race: Race
    pos: int
    amount: float

    def get_pos(self):
        return self.pos


@dataclass
class Account:
    balance: float = 0.0
    bets: list = field(default_factory=list)

    def deposit(self, amount):
        self.balance += amount

    def place_bet(self, bet: Bet):
        self.bets.append(bet)
        self.balance -= bet.amount

    def claim_win(self, bet: Bet):
        if bet not in self.bets:
            return None
        if bet.get_pos() != bet.race.get_winner().pos:
            return None
        # Add win to balance
        self.balance += bet.amount * bet.race.winner.odds.odds


@dataclass
class Bank:
    name: str
    accounts: list = field(default_factory=list)

    def add_account(self, account):
        self.accounts.append(account)


if __name__ == "__main__":
    the_venue = Venue("Galopbanen")
    race1 = Race("Første løb")
    the_venue.add_race(race1)
    horse1 = Horse("Lotte")
    horse2 = Horse("Raket")
    horse3 = Horse("Ibrahim")
    horse4 = Horse("Tarzan")
    horse5 = Horse("Tarok")
    horse6 = Horse("Rasmus")
    race1.add_horse(horse1, pos=1, odds=Odds(4.1))
    race1.add_horse(horse2, pos=2, odds=Odds(6.2))
    race1.add_horse(horse3, pos=3, odds=Odds(3.8))
    race1.add_horse(horse4, pos=4, odds=Odds(5.4))
    race1.add_horse(horse5, pos=5, odds=Odds(13.7))
    race1.add_horse(horse6, pos=6, odds=Odds(8.2))

    the_bank = Bank("Totalisator")
    account1 = Account()
    the_bank.add_account(account1)
    account1.deposit(1000)

    bet1 = Bet(race1, 4, 100)
    account1.place_bet(bet1)

    race1.run()
    winner = race1.get_winner().pos
    if bet1.get_pos() == winner:
        account1.claim_win(bet1)

    pprint(account1)
    pprint(bet1)
    pprint(race1)
