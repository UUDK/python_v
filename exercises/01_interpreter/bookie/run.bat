python bookie.py --init --initial-asset 100000
python bookie.py --new-race --race-name "Big Darby"
python bookie.py --add-horse --race-name "Big Darby" --horse Xerxes --odds 3.1
python bookie.py --add-horse --race-name "Big Darby" --horse Troudeau --odds 2.6
python bookie.py --add-horse --race-name "Big Darby" --horse Frederix --odds 4.7
python bookie.py --add-horse --race-name "Big Darby" --horse Equinox --odds 11.0
python bookie.py --add-player --player-name "Jack Norman" --deposit 1000
python bookie.py --add-bet --player-name "Jack Norman" --race-name "Big Darby" --horse Xerxes --amount 75
python bookie.py --race-result --race-name "Big Darby" --horse Xerxes
python bookie.py --print-status

