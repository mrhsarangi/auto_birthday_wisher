import requests
import datetime 


# CONSTANTS
FILEPATH = "data/data.csv"


def load_data(filepath: str) -> list[list]:
    with open(filepath) as f:
        header = f.readline()
        print(header)
        for line in f.readlines():
            print(line) 

    return [[]]


if __name__ == "__main__":
    data = load_data(FILEPATH)


