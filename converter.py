###
# converter.py - Text converter
###
import sys


# Helper functions
def upper_first_letter(input_str: str) -> str:
    return input_str[0].upper() + input_str[1:]


# Convertion functions
def to_lower(sentence: str) -> str:
    sentence = sentence.lower()
    return sentence


def to_upper(sentence: str) -> str:
    sentence = sentence.upper()
    return sentence


def to_sentence(sentence: str) -> str:
    sentence = sentence.lower()
    sentence = upper_first_letter(sentence)
    sentence = (lambda s: s if s[-1] == '.' else s + '.')(sentence)
    return sentence


def to_title(sentence: str) -> str:
    articles_list = ["as", "the", "a", "an", "is", "and", "but", "by", "for",
                     "in", "of", "to", "or", "nor", "on", "at"]
    new_sentence = ""
    words = sentence.lower().split(' ')

    for w in words:
        if w in articles_list:
            new_sentence += w
        else:
            new_sentence += upper_first_letter(w)
        new_sentence += ' '

    return new_sentence


def to_title_all(sentence: str) -> str:
    new_sentence = ""
    words = sentence.lower().split(' ')

    for w in words:
        new_sentence += upper_first_letter(w)
        new_sentence += ' '

    return new_sentence


def to_studly(sentence: str) -> str:
    return sentence


# parse the input strings
def parse_args() -> dict:
    ret = {"sentence": None, "to_type": None}
    ret["to_type"] = sys.argv[1]
    ret["sentence"] = sys.argv[2]
    return ret


def parse_input() -> dict:
    ret = {"sentence": None, "to_type": None}
    ret["to_type"] = input("What kind of conversion do you want? ")
    ret["sentence"] = input("Enter your sentence: ")
    print('\n')
    return ret


def print_help():
    msg = """
Usage: python converter.py [<OPTION>] ["<your sentence here>"]

Convert strings. If you provide any CLI arguments, you must provide an option
 along with the sentence in double quotes. If you do not provide arguments,
 you'll be asked for the arguments.

Options:
  -lower                convert to lowercase
  -upper                CONVERT TO UPPERCASE
  -sentence             Convert to sentence case.
  -title                Convert to Title Case
  -title-all            Convert To Title Case, Including The Arcicles
  -studly               CoNvErT tO sTuDlY cAsE

  -help                 Print this help message
    """
    print(msg)


# Code Entry
if __name__ == "__main__":
    user_input = {}
    output = ""

    # Choose parsing method
    if len(sys.argv) == 1:
        user_input = parse_input()
    elif len(sys.argv) == 3:
        user_input = parse_args()
    else:
        print_help()
        exit(1)

    # print(user_input)

    # Convert based on to_type
    if user_input["to_type"] == "-lower":
        output = to_lower(user_input["sentence"])
    elif user_input["to_type"] == "-upper":
        output = to_upper(user_input["sentence"])
    elif user_input["to_type"] == "-sentence":
        output = to_sentence(user_input["sentence"])
    elif user_input["to_type"] == "-title":
        output = to_title(user_input["sentence"])
    elif user_input["to_type"] == "-title-all":
        output = to_title_all(user_input["sentence"])
    elif user_input["to_type"] == "-studly":
        output = to_studly(user_input["sentence"])
    else:
        output = "You did not submit a proper conversion type."
        print_help()

    print(f"{output}")
