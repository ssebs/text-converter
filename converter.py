###
# converter.py - Text converter
###
import sys


# Convertion functions
def to_lower(sentence: str) -> str:
    pass


def to_upper(sentence: str) -> str:
    pass


def to_sentence(sentence: str) -> str:
    pass


def to_title(sentence: str) -> str:
    pass


def to_title_all(sentence: str) -> str:
    pass


def to_studly(sentence: str) -> str:
    pass


# parse the input strings
def parse_args() -> dict:
    ret = {"sentence": None, "to_type": None}
    return ret


def parse_input() -> dict:
    ret = {"sentence": None, "to_type": None}
    return ret


# Code Entry
if __name__ == "__main__":
    user_input = {}
    output = ""

    print(sys.argv)

    # Choose parseing method
    if len(sys.argv) == 1:
        user_input = parse_input()
    else:
        user_input = parse_input()

    # Convert based on to_type
    if user_input["to_type"] == "lower":
        output = to_lower(user_input["sentence"])
    elif user_input["to_type"] == "upper":
        output = to_upper(user_input["sentence"])

    print(f"\n> {output}")
