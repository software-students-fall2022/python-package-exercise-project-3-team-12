# Python Package Exercise - Team 12

![Python build](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-12/actions/workflows/build.yaml/badge.svg)

## Documentation

This package is a guessing game, where a user can use functions to find hints and guess for an animal or object. 
A user can import their own guessing object and make a game for other.

First install the package into your environment:

`pip3 install -i https://test.pypi.org/simple/ examplepackageTeam12p3`

then put in the header:

`from examplepackageTeam12p3 import guess_game`

and begin using the functions in your program.

For the examples in functions this alias will be used:

`from examplepackageTeam12p3 import guess_game as game`
### Functions

#### `def import_file(fpath):`
    Takes input json file as string that contains details about interactions and rules so user can create their own game
`game.import_file(your_file)` to import your_file as the animal class  

#### `def interact(action:str, animal:Animal):`
    takes action as string and prints result of action.
	accesses a dictionary of lists where lists store result of action and turn/healthpoint loss.

#### `def letter_match(letter, animal:Animal):`
    takes a letter as input and returns whether or not letter is in animal name.
    returns array of indices where letter matches.  
    

#### `def handle_letter_match(animal:Animal, guesses:list):`
    
    handling user interaction w/ letter match
    

#### `def guess(guess_name, animal:Animal):`
    
    takes name of animal as string and returns true or false
    

#### `def handle_guess(animal:Animal):`
    
    handling user interaction when guessing
    
#### `def handle_input(actions, animal:Animal, guesses):`

#### `def stringify(keys):`

### Setup

#### Setup the virtual environment: 
1. Install pipenv with `python3 -m pip install --user pipenv`
2. Create the virtual environment and install this package `pip install -i https://test.pypi.org/simple/ examplepackageTeam12p3`
3. Activate the environment with `pipenv shell`
4. Exit the virtual environment with `exit`

Build the package with `python -m build`

#### Test with pytest:
1. Install pytest into your vitural environment with `pipenv install pytest`
2. Run `python3 -m pytest` from the main directory

## Team Members

Yvonne Wu (Yiyi Wu) : <https://github.com/Yvonne511>

Leah Durrett : <https://github.com/howtofly-lab>

Alexander Chen : <https://github.com/TheAlexanderChen>

John Kolibachuk : <https://github.com/jkolib>

PyPI: <https://test.pypi.org/project/examplepackageTeam12p3/>
