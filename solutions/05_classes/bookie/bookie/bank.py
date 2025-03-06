from dataclasses import dataclass, field

from .race import Horse, Race, RaceStatus


@dataclass
class Bet:
    race: Race
    horse: Horse
    amount: int
    redeemed: bool = False


@dataclass
class Player:
    name: str
    balance: int = 0
    bets: list[Bet] = field(default_factory=list)


@dataclass
class Bank:
    balance: int = 0
    players: list[Player] = field(default_factory=list)
    races: list[Race] = field(default_factory=list)

    def add_race(self, race_name: str) -> None:
        self.races.append(Race(name=race_name))

    def find_race(self, race_name: str) -> Race | None:
        for race in self.races:
            if race.name == race_name:
                return race
        return None

    def add_player(self, player_name: str, deposit: int):
        self.players.append(Player(name=player_name, balance=deposit))

    def find_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def add_bet(self, player_name: str, race_name: str, horse_name: str, amount: int):
        player = self.find_player(player_name)
        race = self.find_race(race_name)
        horse = race.find_horse(horse_name)
        player.bets.append(Bet(race=race, horse=horse, amount=amount))
        player.balance -= amount
        self.balance += amount

    def pay_out(self):
        for player in self.players:
            for bet in player.bets:
                if (
                    bet.race.status == RaceStatus.FINISH
                    and bet.horse == bet.race.winner
                ):
                    player.balance += bet.amount * bet.horse.rating
                    self.balance -= bet.amount * bet.horse.rating
                bet.redeemed = True
