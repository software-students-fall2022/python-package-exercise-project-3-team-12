import json

animal = {'name': 'lion', 'turns': 20, 'interactions': {
    'poke': ['it roars and bites your hand off', 10],
    'look': ['its yellow fur glistens gracefully in the sun', 1],
    'yell': ['it glances over at you and yawns, bearing its four large canines', 2],
    'look around': ['surrounding you are beautiful African plains', 1],
    'pet': ['its large mane feels good through your fingers', 3]
    }, 'letter_match': 1}
animals = [animal]


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
        animals.append(animal_json)
        print(animals)

def interact(action:str):
    '''
    takes action as string and prints result of action.
	accesses a dictionary of tuples where tuples store result of action and turn/healthpoint loss.
    '''
    act_arr = animal.get('interactions').get(action)
    animal.update({'turns': animal.get('turns') - act_arr[1]})
    return act_arr[0]

def letter_match(letter):
    '''
    takes a letter as input and returns whether or not letter is in animal name.
    returns array of indices where letter matches.
    '''
    if(animal.get('letter_match') > 0):
        animal.update({'turns': animal.get('turns') - 1})
        matches = []
        name = animal.get('name')
        for i in range(len(name)):
            if (letter == name[i]):
                matches.append(i)
        print("matches: ",matches)
        return matches
    else:
         print('You cannot guess anymore letters!')


def handle_letter_match():
    '''
    handling user interaction w/ letter match
    '''
    while (True):
        inp = input("Guess a letter: ").lower()
        if (len(inp)>1):
            print("Input only 1 letter!")
        else:
            letter_match(inp)
            break


def guess(guess_name):
    '''
    takes name of animal as string and returns true or false
    '''
    if(guess_name.lower() == animal.get('name').lower()):
        print("You guessed correctly!")
        return True
    else:
        print("Wrong. Try again.")
        return False   

def handle_guess():
    '''
    handling user interaction when guessing
    '''
    inp = input("Guess the animal: ").lower()
    return guess(inp)

def handle_input(actions):
    while(True):
        inp = input('What will you do?: ').lower()

        if(inp == 'guess letter'):
            return handle_letter_match()
            #return False
        elif(inp == 'guess'):
            return handle_guess()

        if(inp in actions):
            interact(inp)
            return False
        else:
            print('Can\'t do that, sorry!')
            print('Your available actions: '+stringify(actions)+'\n\tguess letter\n\tguess')

def stringify(keys):
    output = ''
    for key in keys:
        output += '\n\t'+key
    return output

def play():
    '''
    method used to play game
    '''
    turns = animal.get('turns')
    actions = animal.get('interactions').keys()

    print('Welcome to our guessing game! Interact with the animal to receive clues on what it is and make your best guess!')

    while(turns > 0):
        print('\nYour number of turns left: '+str(turns))
        print('Your available actions: '+stringify(actions)+'\n\tguess letter\n\tguess')
        guess = handle_input(actions)

        if(guess):
            print('Congrats! You win!')
            break

        turns = animal.get('turns')

        # to do: handle guesses and handle letter guesses

        if(turns <= 0):
            print('Your game has ended! Better luck next time!')
        
