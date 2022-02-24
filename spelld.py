import os
import random
import json

"""
Filters text so that it's in one format
Only replaces apostrophies as of now
"""
def filter_text(in_str):
    res = in_str
    res = res.replace(chr(8217), "'")
    return res


"""
Auto capitalizes in_str to match the case of match_str
"""
def match_text_case(in_str, match_str):
    res_str = ""

    i, j = 0, 0
    while (i < len(in_str) and j < len(match_str)):
        c = match_str[j]
        c_to_add = in_str[i]

        if (c.upper() == c):
            c_to_add = c_to_add.upper()
        res_str += c_to_add

        i += 1
        j += 1

    return res_str


"""
Read the text file
"""
def read_file(path):
    with open(path, "r") as file:
        input_text = file.read()
        input_text = " ".join(input_text.split("\n"))
        return filter_text(input_text)


"""
Output text to a file
"""
def write_file(path, str):
    # Remove any file if it exists
    if (os.path.isfile(path)):
        os.remove(path)
    with open(path, "w+") as file:
        file.write(str)


"""
Randomly capitalize (or lower) characters in a string
"""
def gen_capitals(in_str, p=0.05):
    def change_to_capital(str):
        odds = random.random()
        if (odds <= p):
            # Make string lower if already uppercase
            # Else, return the capitalization,
            if (str.upper() == str):
                return str.lower()
            return str.upper()
        else:
            return str
    return "".join(list(map(change_to_capital, in_str)))


"""
Generate random spaces in a string
"""
def gen_spaces(in_str, p=0.05):
    def add_spaces(str):
        odds = random.random()
        return f"{str} " if odds <= p else str
    return "".join(list(map(add_spaces, in_str)))


"""
Swap out words with their misspelled counterparts
Uses common misspellings found in misspelled/missp.json
"""
def gen_spelling_mistakes(in_str, p=0.05):
    # Load the file containing common mistakes
    common_mistakes = {}
    with open("./misspelled/missp.json") as file:
        common_mistakes = json.load(file)

    def misspell_words(str):
        odds = random.random()
        res_str = str

        key_str = str.lower()
        if (odds <= p
                and key_str in common_mistakes.keys()):
            res_str = random.choice(common_mistakes[key_str])
            res_str = match_text_case(res_str, str)
        return res_str + " "

    res = "".join(list(map(misspell_words, in_str.split(" "))))
    return res[:-1]


INPUT_PATH = "input.txt"
OUTPUT_PATH = "output.txt"
if (__name__ == '__main__'):
    text_to_mess = read_file(INPUT_PATH)
    text_to_mess = gen_spelling_mistakes(text_to_mess, p=0.025)
    text_to_mess = gen_capitals(text_to_mess, p=0.025)
    text_to_mess = gen_spaces(text_to_mess, p=0.025)
    write_file(OUTPUT_PATH, text_to_mess)
