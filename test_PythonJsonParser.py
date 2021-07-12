from unittest import TestCase
import PythonJsonParser


class TestPythonJsonParser(TestCase):
    def test_str_to_datetime(self):
        self.fail()

    def test_open_file(self):
        self.fail()

    def test_remove_duplicates_from_list(self):
        l1 = [1, "Hello", 3.4]
        l2 = [1, "Hello", 3.4, 1, "Hello World", 3.41]
        expected_l2 = [1, "Hello", 3.4, "Hello World", 3.41]

        actual_l1 = PythonJsonParser.remove_duplicates_from_list(l1)
        self.assertEqual(actual_l1, l1)

        actual_al2 = PythonJsonParser.remove_duplicates_from_list(l2)
        self.assertEqual(actual_al2, expected_l2)

    def test_reverse_string(self):
        s1 = "string"
        expected_s1 = "gnirts"
        actual_s1 = PythonJsonParser.reverse_string(s1)
        self.assertEqual(actual_s1, expected_s1)
