# Restructure the script `bookie.py` into a package with modules for each functionality.
# Make the remaining of the script into a `main()` function called from a `if __name__ == "__main__":` block.

import pickle
from pprint import pprint

from bookie.bank import Bank
from bookie.cli import parse
from bookie.race import RaceStatus


def main():
    args = parse()

    the_bank = Bank(balance=0, players=[], races=[])

    if args.init:
        print(f"Initializing the bookie system with asset: {args.initial_asset}")
        the_bank = Bank(balance=args.initial_asset, players=[], races=[])
        with open("bank.pkl", "wb") as f:
            pickle.dump(the_bank, f)
    else:
        with open("bank.pkl", "rb") as f:
            the_bank: Bank = pickle.load(f)

        if args.new_race:
            print(f"Adding a new race called {args.race_name}")
            the_bank.add_race(args.race_name)

        elif args.add_horse:
            print(f"Adding a horse {args.horse} with odds {args.odds}")
            race = the_bank.find_race(args.race_name)
            race.add_horse(args.horse, args.odds)

        elif args.add_player:
            print(f"Adding a player {args.player_name} with deposit {args.deposit}")
            the_bank.add_player(args.player_name, args.deposit)

        elif args.add_bet:
            print(
                f"Adding a bet for player {args.player_name} on horse {args.horse} with amount {args.amount}"
            )
            the_bank.add_bet(args.player_name, args.race_name, args.horse, args.amount)

        elif args.race_result:
            print(
                f"Declaring winner of the race {args.race_name} as horse {args.horse}"
            )
            race = the_bank.find_race(args.race_name)
            horse = race.find_horse(horse_name=args.horse)
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
                    won = bet.amount * bet.horse.rating if bet.race.winner == bet.horse else 0
                    print(f"    Bet: {bet.amount} on {bet.horse.name} Won: {won}")
            print()
            pprint(the_bank)
        else:
            print("No valid command provided")

        with open("bank.pkl", "wb") as f:
            pickle.dump(the_bank, f)


if __name__ == "__main__":
    main()
