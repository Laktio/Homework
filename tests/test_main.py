import pytest

from main import main

import unittest
from io import StringIO
from unittest.mock import patch

class TestMyFunction(unittest.TestCase):
    def test_main(self):
        with patch('sys.stdin', new=StringIO('1')):
            result = main()
            self.assertEqual(result, "C:\\Users\\ber_l\\OneDrive\\Рабочий стол\\Python\\Projects\\Homework\\data\\operations.json")