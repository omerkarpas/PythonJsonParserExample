import json
from json import JSONDecodeError
import datetime


def remove_duplicates_from_list(a_list: list) -> list:
    return list(dict.fromkeys(a_list))


def reverse_string(string: str) -> str:
    return "".join(reversed(string))


class PythonJsonParser:
    def __init__(self, path_to_json_file: str):
        self.json_dict: dict or None = None
        self.new_json_dict: dict = {}
        self.path_to_file: str = path_to_json_file

    @staticmethod
    def str_to_datetime(date_time_str: str) -> str or None:
        print("Got a string, checking if this is a datetime string")
        try:
            dt: datetime = datetime.datetime.strptime(date_time_str, '%Y/%m/%d %H:%M:%S')  # YYYY/MM/DD HH:mm:ss
            dt = dt.replace(year=2021)
            str_date_time: str = dt.strftime('%Y/%m/%d %H:%M:%S')
            return str_date_time
        except ValueError:
            print("could not parse date time string. given string was: ", date_time_str,
                  " with template: YYYY/MM/DD HH:mm:ss")
            return None

    def open_file(self):
        try:
            with open(self.path_to_file, "r") as json_file:
                self.json_dict = json.load(json_file)
        except JSONDecodeError as err:
            print("JSON Decoding error: Bad input")
            print("Error message: ", err.msg)
            print("Error at line: ", err.lineno, "Column: ", err.colno)

    def manipulate_file(self):
        self.open_file()
        if self.json_dict is not None:
            for key in self.json_dict:
                value = self.json_dict[key]
                if isinstance(value, list):
                    self.new_json_dict[key] = remove_duplicates_from_list(value)
                    continue
                elif isinstance(value, str):
                    datetime_str = self.str_to_datetime(value)
                    if datetime_str is not None:
                        self.new_json_dict[key] = datetime_str
                        continue
                    self.new_json_dict[key] = reverse_string(value)
                    continue
                    # serialize to JSON using dumps
            with open(self.path_to_file + "_NEW", 'w') as new_json_file:
                json.dump(self.new_json_dict, new_json_file, indent=4)
