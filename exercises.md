# Chapter 1

* Create a script that can find all lines in the file pythonbeginners.txt that has the word "python" in it
* Change the script so it can get the search word and filename from commandline
* Use argparse to handle commandline arguments

# Chapter 2

* Create a module that can convert between Celsius and Fahreheit, inches and milimeters, and gallon and liters
* Create a script that uses the functions in the module
* Create a directory called e.g. C:\pythonmodules and add that to the search path through PYTHONPATH
* Convert the module to a package with the three conversions in separate files

# Chapter 3

* Read in the file passwd.txt and print the lines
* Read the file and place the data in a list of tuples
* Read the file and place the data in two dictionaries of named tuples, one dictionary with login as key, the other with uid as key
* Make an Enum with 1 being bash, 2 being ksh, 3 being tcsh, 4 being zsh. Use it in the data structure

# Chapter 4

* Create a function that can calculate numeric integration. It should take four parameters: the function, lower limit, upper limit, and the width of the segments
* Create a list comprehension to calculate the leap years from 1588 to 2024. Take the hundred years rule and four hundred years rule into account

# Chapter 5

* Make model of a bookmaker of a darby race. The following must be represented
  * A race of horses
  * The odds of each horse
  * The bank
  * The player
  * The bet
  * Win or lose

# Chapter 6

* Create a function that reads the `numbers.txt` file, adds the numbers, and returns the sum of the numbers.
* Add error handling so that the lines that are not numbers are ignored.
* Create a main part that asks for the filename and handles if the filename does not exist.

# Chapter 7

For the exercise these data can be used:

```python
data = [
    {'name': 'Anders', 'age': 34, 'height': 1.82},
    {'name': 'Benny', 'age': 51, 'height': 1.81},
    {'name': 'Charlie', 'age': 72, 'height': 1.84},
    {'name': 'Dennis', 'age': 31, 'height': 1.78},
    {'name': 'Eric', 'age': 45, 'height': 1.83},
]
```

* Create a script that dumps the above data to the file named `data.json`
* Create a script that reads `data.json` and prints the content
* Create a script that dumps the above data to the file named `data.csv`
* Create a script that reads `data.csv` and prints the content
* Create a script that connects to a SQLite3 database, dumps the table `data` if it exists, creates a new table `data`, and inserts above data into the table. Read the data out again and print it.

# Chapter 8

* Create a distributable package, `converterz`, with a README file and a `setup.py` file.
* Copy the `convpack` package from chapter 3
* build the package

# Chapter 9

* Add unit tests to the package from chapter 8
* Make sure that `mypy`, `pylint`, `flake8`, and `black` doesn't find any errors.
