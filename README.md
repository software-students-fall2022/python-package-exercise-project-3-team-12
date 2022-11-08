# Python Package Exercise - Team 12

![Python build](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-12/actions/workflows/build.yaml/badge.svg)

## Documentation

This package is a guessing game, where a user can use functions to find hints and guess for an animal or object.  
A user can import their own guessing object and make a game for others.

An example implementation can be found [here](src/example_game.py).

First install the package into your environment:

`pip3 install -i https://test.pypi.org/simple/ examplepackageTeam12p3`

then put in the header:

`from examplepackageTeam12p3 import guess_game`

and begin using the functions in your program.

For the examples in functions this alias will be used:

`from examplepackageTeam12p3 import guess_game as game`

### Functions

#### `import_file(fpath)`

Takes as input a json file as string that contains details about interactions and rules so that a user can create their own game.

Use `game.import_file(your_file)` to import your_file as the animal class  

#### `interact(action:str, animal:Animal)`

Accepts an action as a string and an Animal object. Prints the result of performing the action and lowers the turn count as defined in the Animal object.

You can use `game.interact(your_guess, game.Animal())` to make guesses using the default animal object

#### `letter_match(letter, animal:Animal)`

Takes a letter and animal object as input and returns an array of indices indexed starting at 1 of where the input letter can be found in the input animal.

Use `game.letter_match(your_letter, game.Animal())` to guess letters using the default animal object

#### `handle_letter_match(animal:Animal, guesses:list)`

Takes an animal object and a list which stores letter guesses already made as input and prompts the user for a letter guess input with input validation. Calls `letter_match(input, animal)` to check if input letter is in supplied animal's name, reduce turn count, and receive array of letter match indices to print. The guessed letter is appended to the guesses list when done. Returns `True` when correct input provided or `False` when incorrect input provided.

Use `game.handle_letter_match(game.Animal(), [])` to make a guess with input validation. This method is intended to be used in a loop

#### `guess(guess_name, animal:Animal)`

Accepts a guess string and an animal object to check the guess value against. Returns `True` if the names match or `False` if they do not.

Use `game.guess(your_guess, game.Animal())` to guess the name of the default animal object

#### `handle_guess(animal:Animal)`

Function that takes user input, strips input of white space, and converts input to lowercase before passing input to `guess(input, animal)`. Returns what is returned from `guess()`.

Use `game.handle_guess(game.Animal())` to make a guess of the name of the default animal object using an input prompt

#### `handle_input(actions, animal:Animal, guesses)`

Function that takes the keys of an animal object's interaction attribute as actions, the animal object itself, and an array of letters guessed as guesses. This function is designed to handle most of the interactions between the player and game and represents playing 1 round. It prompts the user for input on how they would like to act and validates the input to ensure that it is an action included in `actions` or is a special action (guess letter, guess). It then calls the function related to the user's choice of action. Returns `True` when the animal name is correctly guessed and returns `False` otherwise.

You can use `game.handle_input(game.Animal().interactions.keys(), game.Animal(), [])` to play 1 round of the game using the default animal where no letter match guesses have been made

#### `stringify(keys)`

This function takes an iterable and produces an output string that includes each item in the iterable converted to string and prepended with a newline and tab.

Use `game.stringify(your_iterable)` to convert your iterable to a formatted string

### Setup

#### Setup the virtual environment

1. Install pipenv with `python3 -m pip install --user pipenv`
2. Create the virtual environment and install this package `pip install -i https://test.pypi.org/simple/ examplepackageTeam12p3`
3. Activate the environment with `pipenv shell`
4. Exit the virtual environment with `exit`

Build the package with `python -m build`

#### Test with pytest

1. Install pytest into your vitural environment with `pipenv install pytest`
2. Run `python3 -m pytest` from the main directory

## Team Members

Yvonne Wu (Yiyi Wu) : <https://github.com/Yvonne511>

Leah Durrett : <https://github.com/howtofly-lab>

Alexander Chen : <https://github.com/TheAlexanderChen>

John Kolibachuk : <https://github.com/jkolib>

PyPI: <https://test.pypi.org/project/examplepackageTeam12p3/>
