import html
import re
from json import load
from typing import List

DB_WORD_FREQUENCIES = {}
NON_WORD_CHARACTER_PATTERN = re.compile("[.,!;:_/\"`$]+")


def get_clean_sentence_from_uni_lepizig_line(line):
    clean_sentence = line.split("\t")[1]
    clean_sentence = clean_sentence.replace("\n", "")
    clean_sentence = html.unescape(clean_sentence)
    clean_sentence = clean_sentence.replace("\u2019", "'")
    clean_sentence = clean_sentence.replace("\u201c", "\"")
    clean_sentence = clean_sentence.replace("\u201d", "\"")

    clean_sentence = clean_sentence.replace("\u2014", "-")

    clean_sentence = clean_sentence.replace("''", "'")
    clean_sentence = clean_sentence.replace("??", "?")

    return clean_sentence


def line_into_cleaned_words(line: str) -> List[str]:
    words = line.split(" ")

    temp_1 = [NON_WORD_CHARACTER_PATTERN.sub('', w) for w in words]
    temp_2 = []
    for w in temp_1:
        if w.endswith("'"):
            w = w[:-1]
        elif w.startswith("'"):
            w = w[1:]
        temp_2.append(w)

    return temp_2


def get_word_frequency(word: str) -> float:
    global DB_WORD_FREQUENCIES
    if (len(DB_WORD_FREQUENCIES) == 0):
        with open("data/word-frequencies.json", "r") as fh:
            DB_WORD_FREQUENCIES = load(fh)

    return DB_WORD_FREQUENCIES.get(word.lower(), 0)
