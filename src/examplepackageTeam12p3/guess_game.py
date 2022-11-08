import json

class Animal:
    def __init__(self, name='lion', turns=20, interactions={
        'poke': ['it roars and bites your hand off', 10],
        'look': ['its yellow fur glistens gracefully in the sun', 1],
        'yell': ['it glances over at you and yawns, bearing its four large canines', 2],
        'look around': ['surrounding you are beautiful African plains', 1],
        'pet': ['its large mane feels good through your fingers', 3]
        }, letter_match=8) -> None:
        self.name = name
        self.turns = turns
        self.interactions = interactions
        self.letter_match = letter_match

def import_file(fpath):
    '''
    takes input file as string that contains details about interactions and rules so user can create their own game
    '''
    with open(fpath) as f:
        imported_animal = ""
        lines = f.readlines()
        for line in lines:
            imported_animal += line.replace("\n", "")
            ##print(line)
        imported_animal = imported_animal.replace("animal = ", "")
        imported_animal = imported_animal.replace("\'", "\"")
        #print(imported_animal)
        animal_json = json.loads(imported_animal)
        animal = animal_json
        print(animal)

def interact(action:str, animal:Animal):
    '''
    takes action as string and prints result of action.
	accesses a dictionary of lists where lists store result of action and turn/healthpoint loss.
    '''
    act_arr = animal.interactions.get(action)
    animal.turns = animal.turns - act_arr[1]
    return act_arr[0]

def letter_match(letter, animal:Animal):
    '''
    takes a letter as input and returns whether or not letter is in animal name.
    returns array of indices where letter matches.
    '''
    animal.turns = animal.turns - animal.letter_match
    matches = []
    for i in range(len(animal.name)):
        if (letter == animal.name[i]):
            matches.append(i+1)
    animal.turns -= 1
    return matches


def _handle_letter_match(animal:Animal, guesses:list):
    '''
    handling user interaction w/ letter match
    '''
    print("Guesses made: ", guesses)
    inp = input("Guess a letter: ").lower().strip()
    if (len(inp)>1):
        print("Input only 1 letter!")
        return False
    elif (inp in guesses):
        print("Already guessed this letter. Pick another.")
        return False
    else:
        guesses.append(inp)
        letter_arr = letter_match(inp, animal)

        if(len(letter_arr) == 0):
            print('No letter matches!')
        else:
            print('Matches at these positions: '+_stringify(letter_arr))
        
        return True



def guess(guess_name, animal:Animal):
    '''
    takes name of animal as string and returns true or false
    '''
    if(guess_name == animal.name.lower().strip()):
        return True
    else:
        animal.turns = animal.turns - 1
        return False   

def _handle_guess(animal:Animal):
    '''
    handling user interaction when guessing
    '''
    inp = input("Guess the animal: ").lower().strip()
    return guess(inp, animal)

def _handle_input(actions, animal:Animal, guesses):
    while(True):
        inp = input('What will you do?: ').lower().strip()

        if(inp == 'guess letter'):
            while(True):
                if(_handle_letter_match(animal, guesses)):
                    return False
        elif(inp == 'guess'):
            if(_handle_guess(animal)):
                return True
            else:
                print('Wrong, try again!')
                return False

        if(inp in actions):
            print(interact(inp, animal))
            interactions = animal.interactions
            del interactions[inp]
            return False
        else:
            print('Can\'t do that, sorry!')
            print('Your available actions: '+_stringify(actions)+'\n\tguess letter\n\tguess')

def _stringify(keys):
    output = ''
    for key in keys:
        output += '\n\t'+str(key)
    return output

def play():
    '''
    method used to play game
    '''
    animal = Animal()
    turns = animal.turns
    actions = animal.interactions.keys()
    guesses = []

    print('Welcome to our guessing game! Interact with the animal to receive clues on what it is and make your best guess!')

    while(turns > 0):
        print('\nYour number of turns left: '+str(turns))
        print('Your available actions: '+_stringify(actions)+'\n\tguess letter\n\tguess')
        guess = _handle_input(actions, animal, guesses)

        if(guess):
            print('Congrats! You win!')
            break

        turns = animal.turns

        if(turns <= 0):
            print('Your game has ended! Better luck next time!')

