import unittest
from mock import MagicMock

class TestStringMethods(unittest.TestCase):

    def test_guess_age(self):
        
        import age_guesser
        
        # set reaction time to 0.3 seconds
        age_guesser.get_reaction_time = MagicMock(return_value=0.5)
        
        # test with valid inputs
        inputs = [100., 50., 30.]
        expected_outputs = [50.0, 25.0, 15.]
        for i, eo in zip(inputs, expected_outputs):
            o = age_guesser.guess_age(i)
            self.assertEqual(eo, o)

        # invalid inputs
        inputs_typeerror  = ["hello", "100"]
        inputs_valueerror = [-100, 0]
        with self.assertRaises(TypeError):
           for i in inputs_typeerror:
                age_guesser.guess_age(i)
        with self.assertRaises(ValueError):
           for i in inputs_valueerror:
                age_guesser.guess_age(i)


            

if __name__ == '__main__':
        unittest.main()
