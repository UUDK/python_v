# Restructure the script `bookie.py` into a package with modules for each functionality.
# Make the remaining of the script into a `main()` function called from a `if __name__ == "__main__":` block.


from bookie.cli import parse


def main():
    args = parse()

    if args.init:
        print(f'Initializing the bookie system with asset: {args.initial_asset}')
    elif args.new_race:
        print(f'Adding a new race called {args.race_name}')
    elif args.add_horse:
        print(f'Adding a horse {args.horse} with odds {args.odds}')
    elif args.add_player:
        print(f'Adding a player {args.player_name} with deposit {args.deposit}')
    elif args.add_bet:
        print(f'Adding a bet for player {args.player_name} on horse {args.horse} with amount {args.amount}')
    elif args.race_result:
        print(f'Declaring winner of the race {args.race_name} as horse {args.horse}')
    elif args.print_status:
        print('Printing the status of the bookie system')
    else:
        print('No valid command provided')

if __name__ == '__main__':
    main()
