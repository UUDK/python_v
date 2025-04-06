python main.py --init --initial-asset 100000
python main.py --new-race --race-name 'Big Darby'
python main.py --add-horse --race-name 'Big Darby' --horse 'Xerxes' --odds 3.1
python main.py --add-horse --race-name 'Big Darby' --odds 2.6
python main.py --add-horse --race-name 'Big Darby' --horse 'Frederix'
python main.py --add-horse --race-name 'Big Darby' --horse 'Equinox' --odds 11.0
python main.py --add-player --player-name 'Jack Norman' --deposit 1000
python main.py --add-bet --player-name 'Jack Norman' --race-name 'Big Darby' --horse 'XXX' --amount 75
python main.py --race-result --race-name 'Big Darby' --horse 'Xerxes'
python main.py --print-status

