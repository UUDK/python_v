# We will make a bookmaker system. First step is to construct the commandline interface. The usecases are:

# * `python bookie.py --init --initial-asset 100000`
# * `python bookie.py --new-race --race-name 'Big Darby'`
# * `python bookie.py --add-horse --race-name 'Big Darby' --horse '1:Xerxes' --odds 3.1`
# * `python bookie.py --add-horse --race-name 'Big Darby' --horse '2:Troudeau' --odds 2.6`
# * `python bookie.py --add-horse --race-name 'Big Darby' --horse '3:Frederix' --odds 4.7`
# * `python bookie.py --add-horse --race-name 'Big Darby' --horse '4:Equinox' --odds 11.0`
# * `python bookie.py --add-player --player-name 'Jack Norman' --deposit 1000`
# * `python bookie.py --add-bet --player-name 'Jack Norman' --race-name 'Big Darby' --horse 1 --amount 75`
# * `python bookie.py --race-result --race-name 'Big Darby' --horse 1`
# * `python bookie.py --print-status`

# Use argparse to handle commandline arguments

import argparse

def cli():
    parser = argparse.ArgumentParser(description='Bookie system')
    parser.add_argument('--init', action='store_true', help='Initialize the bookie system')
    parser.add_argument('--initial-asset', type=int, help='Initial asset for the bookie system')

    #--new-race ... store_true ... 'Add a race'
    #--race-name ... 'Name of the race'

    #--add-horse ... store_true ... 'Add a horse'
    #--horse ... 'Horse name'
    #--odds' ... 'Odds for the horse'

    #--add-player ... store_true ... 'Add a player'
    #--player-name ... 'Name of the player'
    #--deposit' ... 'Deposit amount for the player'

    #--add-bet ... store_true ... 'Add a bet'
    #--amount' ... 'Amount to bet'

    #--race-result ... store_true ... 'Declare winner of the race'

    #--print-status ... store_true ... 'Print the status of the bookie system'

    args = parser.parse_args()
    return args

def main():
    args = cli()

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
