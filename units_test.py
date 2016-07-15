import unittest
from units import Conversor, UnitError


class ConversorTest(unittest.TestCase):
    def test_convert(self):
        result = Conversor.convert('m', 'yd', 3.4)
        expected_result = (3.7182399999999998, 'yd')
        self.assertEqual(result, expected_result)

    def test_unsupported_unit(self):
        self.assertRaises(UnitError, Conversor.convert, 'x', 'yd', 3.4)

    def test_parse_string(self):
        result = Conversor.parse_str('3.4 m')
        expected_result = (3.4, 'm')
        self.assertEqual(result, expected_result)

    def test_parse_string_error(self):
        self.assertRaises(ValueError, Conversor.parse_str, '3f4 m')
        self.assertRaises(UnitError, Conversor.parse_str, '3.4 x')

if __name__ == '__main__':
    unittest.main()
