import pytest
from examplepackageTeam12p3 import game

class Tests:

    def example_fixture(self):
        '''
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        '''

        # place any setup you want to do before any test function that uses this fixture is run

        yield # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed
    
    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    
    def test_guess(self):
        """
        Test if guess correctly identifies that the strings match
        """

    def test_guess_lower(self):
        """
        Test if guess properly lowers the turns after a failed guess and resets the game after a successfull guess
        """

    def test_interact(self):
        """
        Test if interact properly displays its string
        """
    
    def test_interact_lower(self):
        """
        Test if interact properly lowers the turns after an interact
        """

    def test_import(self):
        """
        Test if import properly imports into the format for animal
        """
    
    def test_letter(self):
        """
        Test if letter_match properly checks if the letter is in the animal name
        """

    def test_letter_lower(self):
        """
        Test if letter_match properly lowers the turn count
        """