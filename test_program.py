from io import StringIO
import unittest
import main
from unittest.mock import patch
from utils.logic import luhn_validation

class TestProgram(unittest.TestCase):
    def test_read_file(self):
        expected_output = "Lisa: $-93\nQuincy: error\nTom: $500\n"
        with patch('sys.stdout', new = StringIO()) as fake_output:
            main.read_file('data.txt')
            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_read_direct_input(self):
        expected_output = "\n\nLisa: $-93\nQuincy: error\nTom: $500\n"
        with patch('sys.stdout', new = StringIO()) as fake_output:
            main.read_direct_input(["Add Tom 4111111111111111 $1000",
                                                "Add Lisa 5454545454545454 $3000",
                                                "Add Quincy 1234567890123456 $2000",
                                                "Charge Tom $500",
                                                "Charge Tom $800",
                                                "Charge Lisa $7",
                                                "Credit Lisa $100",
                                                "Credit Quincy $200"])

            self.assertEqual(fake_output.getvalue(), expected_output)

    def test_luhn_validation(self):
        self.assertTrue(luhn_validation("4111111111111111"))
        self.assertFalse(luhn_validation("1234567890123456"))
        self.assertTrue(luhn_validation("79927398713"))
        self.assertFalse(luhn_validation("7992739871379927398713323"))




if __name__ == '__main__':
    unittest.main()