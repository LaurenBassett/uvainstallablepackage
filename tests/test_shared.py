import sys
import unittest
sys.path.append('.')
import shared as sh

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)

class TestFunction(unittest.TestCase):
    def test_whitespace(self):
        # Compress Whitespace
        output = sh.space_compress("word       word      word")
        self.assertEqual(output, "word word word")

    def test_newline(self):
        # If passed multiline string, it should return a single line
        output = sh.space_compress("word \n word \n word")
        self.assertEqual(output, "word word word")
    def test_exception_int(self):
        #If passed an int, it should run an assert Error
        try:
            output = sh.space_compress(1)
        except AssertionError as e:
            self.assertEqual(type(e), AssertionError)
            
    def test_exception_bool(self):
        #If passed a boolean, it should run an assert error
        try:
            output = sh.space_compress(True)
        except AssertionError as e:
            self.assertEqual(type(e), AssertionError)


if __name__ == '__main__':
    unittest.main()