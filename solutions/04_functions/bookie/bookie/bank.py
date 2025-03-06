# Create datatypes for these elements:

# * Horse (name, owner, rating)
# * Race (name, horses, status, winner)
# * Race status (planned, bet-able, started, finish, cancelled)
# * Bet (race, horse, amount, redeemed)
# * Player (name, balance, bets)
# * Bank (balance, players, races)

import typing as t

from .race import Horse, Race, RaceStatus, add_horse, find_horse


class Bet(t.NamedTuple):
    race: Race
    horse: Horse
    amount: int
    redeemed: dict[str, bool]


class Player(t.NamedTuple):
    name: str
    balance: dict[str, int]
    bets: list[Bet]


class Bank(t.NamedTuple):
    balance: dict[str, int]
    players: list[Player]
    races: list[Race]


def add_race(bank: Bank, race_name: str):
    bank.races.append(
        Race(
            name=race_name,
            horses=[],
            status={"status": RaceStatus.PLANNED},
            winner={"winner": None},
        )
    )


def find_race(bank: Bank, race_name: str):
    for race in bank.races:
        if race.name == race_name:
            return race
    return None


def add_player(bank: Bank, player_name: str, deposit: int):
    bank.players.append(Player(name=player_name, balance={"amount": deposit}, bets=[]))


def find_player(bank: Bank, player_name: str):
    for player in bank.players:
        if player.name == player_name:
            return player
    return None


def add_bet(
    bank: Bank, player_name: str, race_name: Race, horse_name: str, amount: int
):
    player = find_player(bank, player_name)
    race = find_race(bank, race_name)
    horse = find_horse(race, horse_name)
    player.bets.append(
        Bet(race=race, horse=horse, amount=amount, redeemed={"redeemed": False})
    )
    player.balance["amount"] -= amount
    bank.balance["amount"] += amount


def pay_out(bank: Bank):
    for player in bank.players:
        for bet in player.bets:
            print(f"{bet.race.status['status']} {bet.horse} {bet.race.winner['winner']}")
            if (
                bet.race.status["status"] == RaceStatus.FINISH
                and bet.horse == bet.race.winner["winner"]
            ):
                player.balance["amount"] += bet.amount * bet.horse.rating
                bank.balance["amount"] -= bet.amount * bet.horse.rating
            bet.redeemed["redeemed"] = True
