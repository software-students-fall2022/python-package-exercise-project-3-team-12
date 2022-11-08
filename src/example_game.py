from examplepackageTeam12p3 import guess_game as game

animal = game.Animal()
turns = animal.turns
actions = animal.interactions.keys()
guesses = []

print('Welcome to our guessing game! Interact with the animal to receive clues on what it is and make your best guess!')

while(turns > 0):
    print('\nYour number of turns left: '+str(turns))
    print('Your available actions: '+game.stringify(actions)+'\n\tguess letter\n\tguess')
    guess = game.handle_input(actions, animal, guesses)

    if(guess):
        print('Congrats! You win!')
        break

    turns = animal.turns

    if(turns <= 0):
        print('Your game has ended! Better luck next time!')
