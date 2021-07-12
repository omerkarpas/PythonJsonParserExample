import PythonJsonParser


def main():
    pjs = PythonJsonParser.PythonJsonParser("python exercise.json")
    pjs.manipulate_file()


if __name__ == "__main__":
    main()
