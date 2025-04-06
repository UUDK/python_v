# Restructure the script `bookie.py` into a package with modules for each functionality.
# Make the remaining of the script into a `main()` function called from a `if __name__ == "__main__":` block.

import pickle
from pprint import pprint

from bookie.bank import Bank
from bookie.cli import parse
from bookie.race import RaceStatus


class ParamError(Exception):
    """Exception raised for errors in the cli parameters."""


def main():
    args = parse()

    try:
        with open("bank.pkl", "rb") as f:
            the_bank: Bank = pickle.load(f)
    except FileNotFoundError:
        the_bank = Bank(balance=0, players=[], races=[])

    try:
        if args.init:
            if args.initial_asset is None:
                raise ParamError("--init must be used with --initial-asset")
            print(f"Initializing the bookie system with asset: {args.initial_asset}")
            the_bank = Bank(balance=args.initial_asset, players=[], races=[])

        elif args.new_race:
            if args.race_name is None:
                raise ParamError("--new-race must be used with --race-name")
            print(f"Adding a new race called {args.race_name}")
            the_bank.add_race(args.race_name)

        elif args.add_horse:
            if args.race_name is None or args.horse is None or args.odds is None:
                raise ParamError(
                    "--add-horse must be used with --race-name, --horse and --odds"
                )
            print(f"Adding a horse {args.horse} with odds {args.odds}")
            race = the_bank.find_race(args.race_name)
            if race is None:
                raise ParamError(f"Race {args.race_name} not found")
            race.add_horse(args.horse, args.odds)

        elif args.add_player:
            if args.player_name is None or args.deposit is None:
                raise ParamError(
                    "--add-player must be used with --player-name and --deposit"
                )
            print(f"Adding a player {args.player_name} with deposit {args.deposit}")
            the_bank.add_player(args.player_name, args.deposit)

        elif args.add_bet:
            if (
                args.player_name is None
                or args.race_name is None
                or args.horse is None
                or args.amount is None
            ):
                raise ParamError(
                    "--add-bet must be used with --player-name, --race-name, --horse and --amount"
                )
            print(
                f"Adding a bet for player {args.player_name} on horse {args.horse} with amount {args.amount}"
            )
            player = the_bank.find_player(args.player_name)
            if player is None:
                raise ParamError(f"Player {args.player_name} not found")
            race = the_bank.find_race(args.race_name)
            if race is None:
                raise ParamError(f"Race {args.race_name} not found")
            horse = race.find_horse(horse_name=args.horse)
            if horse is None:
                raise ParamError(f"Horse {args.horse} not found")
            the_bank.add_bet(player, race, horse, args.amount)

        elif args.race_result:
            if args.race_name is None or args.horse is None:
                raise ParamError(
                    "--race-result must be used with --race-name and --horse"
                )
            print(
                f"Declaring winner of the race {args.race_name} as horse {args.horse}"
            )
            race = the_bank.find_race(args.race_name)
            if race is None:
                raise ParamError(f"Race {args.race_name} not found")
            horse = race.find_horse(horse_name=args.horse)
            if horse is None:
                raise ParamError(f"Horse {args.horse} not found")
            race.winner = horse
            race.status = RaceStatus.FINISH
            the_bank.pay_out()

        elif args.print_status:
            print("Printing the status of the bookie system")
            print(f"Bank balance: {the_bank.balance}")
            print("Players:")
            for player in the_bank.players:
                print(f"  Player: {player.name}, Balance: {player.balance}")
                for bet in player.bets:
                    won = (
                        bet.amount * bet.horse.rating
                        if bet.race.winner == bet.horse
                        else 0
                    )
                    print(f"    Bet: {bet.amount} on {bet.horse.name} Won: {won}")
            print()
            pprint(the_bank)
        else:
            print("No valid command provided")
    except ParamError as e:
        print(f"Bad argument(s): {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    with open("bank.pkl", "wb") as f:
        pickle.dump(the_bank, f)


if __name__ == "__main__":
    main()
