# Restructure the script `bookie.py` into a package with modules for each functionality.
# Make the remaining of the script into a `main()` function called from a `if __name__ == "__main__":` block.


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

def parse():
    parser = argparse.ArgumentParser(description='Bookie system')
    parser.add_argument('--init', action='store_true', help='Initialize the bookie system')
    parser.add_argument('--initial-asset', type=int, help='Initial asset for the bookie system')

    parser.add_argument('--new-race', action='store_true', help='Add a race')
    parser.add_argument('--race-name', type=str, help='Name of the race')

    parser.add_argument('--add-horse', action='store_true', help='Add a horse')
    parser.add_argument('--horse', type=str, help='Horse name')
    parser.add_argument('--odds', type=float, help='Odds for the horse')

    parser.add_argument('--add-player', action='store_true', help='Add a player')
    parser.add_argument('--player-name', type=str, help='Name of the player')
    parser.add_argument('--deposit', type=int, help='Deposit amount for the player')

    parser.add_argument('--add-bet', action='store_true', help='Add a bet')
    parser.add_argument('--amount', type=int, help='Amount to bet')

    parser.add_argument('--race-result', action='store_true', help='Declare winner of the race')

    parser.add_argument('--print-status', action='store_true', help='Print the status of the bookie system')
    args = parser.parse_args()
    return args

