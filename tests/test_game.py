from io import StringIO
import pytest
from examplepackageTeam12p3 import guess_game as game

class Tests:
    @pytest.fixture
    def example_fixture(self):
        '''
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        '''

        # place any setup you want to do before any test function that uses this fixture is run

        yield # at the yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    # @pytest.fixture
    # def load_fixture(self):
    #     """
    #     fixture for loading in data
    #     """
    #     game.import_file()

    #     yield

    #     game.animal = {'name': 'lion', 'turns': 20, 'interactions': {
    #         'poke': ['it roars and bites your hand off', 10],
    #         'look': ['its yellow fur glistens gracefully in the sun', 1],
    #         'yell': ['it glances over at you and yawns, bearing its four large canines', 2],
    #         'look around': ['surrounding you are beautiful African plains', 1],
    #         'pet': ['its large mane feels good through your fingers', 3]
    #         }, 'letter_match': 1}

    # @pytest.fixture
    # def load_fixture_false(self):
    #     """
    #     fixture for loading in data incorrectly
    #     """
    #     yield

    @pytest.fixture
    def make_animal(self):
        animal = game.Animal()
        return animal

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    
    def test_guess(self, make_animal):
        """
        Test if guess correctly identifies that the strings match 
        """
        name = make_animal.name
        assert game.guess(name, make_animal) == True

    def test_guess_lower(self, make_animal):
        """
        Test if guess properly lowers the turns after a failed guess
        """
        before = make_animal.turns
        game.guess("tiger", make_animal)
        assert before > make_animal.turns

    def test_guess_fail(self, make_animal):
        """
        Test if guess properly fails for incorrect inputs
        """
        fails = ['l i o n', 'tiger', 'absfgdsgs', '12345']
        for fail in fails:
            assert game.guess(fail,make_animal) == False

    def test_handle_guess_fail(self, make_animal, monkeypatch):
        """
        Test if handle guess fails on incorrect input
        """
        fails = [' lio n ', ' L ion', '12345', 'asdfg', 'tiger ', ' Tig er']
        for fail in fails:
            monkeypatch.setattr('sys.stdin', StringIO(fail))
            assert game._handle_guess(make_animal) == False

    def test_handle_guess_case(self, make_animal, monkeypatch):
        """
        Test if handle guess lowers case for inputs properly
        """
        success = ['lion', 'Lion', 'lIon', 'liOn', 'lioN', 'LIon', 'LiOn', 'LioN', 'LIOn', 'LiON', 'lION', 'LION']
        for s in success:
            monkeypatch.setattr('sys.stdin', StringIO(s))
            assert game._handle_guess(make_animal) == True

    def test_handle_guess_strip(self, make_animal, monkeypatch):
        """
        Test if handle guess strips inputs properly
        """
        success = ['lion', ' lion','lion ',' lion ','  lion ']
        for s in success:
            monkeypatch.setattr('sys.stdin', StringIO(s))
            assert game._handle_guess(make_animal) == True

    def test_interact(self, make_animal):
        """
        Test if interact properly returns its string
        """
        for key in make_animal.interactions:
            assert make_animal.interactions[key][0] == game.interact(key, make_animal)          
    
    def test_interact_lower(self, make_animal):
        """
        Test if interact properly lowers the turn count
        """
        for key in make_animal.interactions:
            before = make_animal.turns
            game.interact(key, make_animal)
            assert before > make_animal.turns

    def test_interact_str(self, make_animal):
        """
        Test if the string returned by interact is valid
        """
        for key in make_animal.interactions:
            assert len(game.interact(key, make_animal)) > 0   

    # def test_import(self, load_fixture):
    #     """
    #     Test if import properly imports into the format for animal
    #     """

    # def test_import_incorrect(self, load_fixture_false):
    #     """
    #     Test if import properly handles incorrect import types
    #     """
    #     assert game.animal == {'name': 'lion', 'turns': 20, 'interactions': {
    # 'poke': ['it roars and bites your hand off', 10],
    # 'look': ['its yellow fur glistens gracefully in the sun', 1],
    # 'yell': ['it glances over at you and yawns, bearing its four large canines', 2],
    # 'look around': ['surrounding you are beautiful African plains', 1],
    # 'pet': ['its large mane feels good through your fingers', 3]
    # }, 'letter_match': 1}

    def test_letter(self, make_animal):
        """
        Test if letter_match properly checks if the letter is in the animal name
        """
        for letter in make_animal.name:
            match_arr = game.letter_match(letter, make_animal)
            assert len(match_arr) > 0
            for ind in match_arr:
                assert ind-1 == make_animal.name.find(letter)

    def test_letter_fail(self, make_animal):
        """
        Test if letter_match properly returns an empty array if there are no matches
        """
        fails = ['1','a','b','z','bb']
        for fail in fails:
            assert len(game.letter_match(fail, make_animal)) == 0

    def test_letter_lower(self, make_animal):
        """
        Test if letter_match properly lowers the turn count
        """
        before = make_animal.turns
        fails = ['1','a','b','z','bb']
        for fail in fails:
            game.letter_match(fail, make_animal)
            assert before > make_animal.turns

    # def test_letter_repeat(self, make_animal):
    #     """
    #     Test if letter_match does not allow repeats
    #     """

    # def test_play_win(self):
    #     """
    #     Test if play returns the correct value if you guess correctly
    #     """

    # def test_play_lose(self):
    #     """
    #     Test if play returns the correct value if you guess incorrectly
    #     """

    ####################################
    #      handle_letter_match tests
    ####################################

    def test_handle_let_mat_many_letters(self, make_animal, monkeypatch, capsys):
        '''
        test to make sure handle_letter_match properly handles input with >1 letter
        '''
        monkeypatch.setattr('sys.stdin', StringIO('abcd\n'))

        game.handle_letter_match(make_animal, [])
        assert 'Input only 1 letter!' in capsys.readouterr().out

    def test_handle_let_mat_dupe_guess(self, make_animal, monkeypatch, capsys):
        '''
        test to make sure handle_letter_match rejects duplicate letter guesses
        '''
        guesses = []

        monkeypatch.setattr('sys.stdin', StringIO('a\n'))
        game.handle_letter_match(make_animal, guesses)
        assert guesses[0] == 'a'

        monkeypatch.setattr('sys.stdin', StringIO('a\n'))
        game.handle_letter_match(make_animal, guesses)
        assert len(guesses) == 1
        assert 'Already guessed this letter. Pick another.' in capsys.readouterr().out

    def test_handle_let_mat_no_match(self, make_animal, monkeypatch, capsys):
        '''
        test to make sure correct output given when no match found
        '''
        monkeypatch.setattr('sys.stdin', StringIO('a\n'))

        game.handle_letter_match(make_animal, [])
        assert 'No letter matches!' in capsys.readouterr().out

    ####################################
    #           play tests
    ####################################

    # def test_play_success(self, monkeypatch, capsys):
    #     '''
    #     test to make sure game ends correctly when proper guess given
    #     '''
    #     game.play()
    #     monkeypatch.setattr('sys.stdin', StringIO('guess\n'))
    #     monkeypatch.setattr('sys.stdin', StringIO('lion\n'))
    #     assert 'Congrats! You win!' in capsys.readouterr().out

    # def test_play_failure(self, monkeypatch, capsys):
    #     '''
    #     test to make sure game ends correctly when turns used up
    #     '''
    #     game.play()
    #     monkeypatch.setattr('sys.stdin', StringIO('poke\n'))
    #     monkeypatch.setattr('sys.stdin', StringIO('poke\n'))
    #     assert 'Your game has ended! Better luck next time!' in capsys.readouterr().out