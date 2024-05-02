"""
This script is used to prepare the data that is used for my sketch entered into the Weekly
Creative Coding Challenge held on openprocessing.org

Link to the sketch: https://openprocessing.org/sketch/2258655

Description
-----------
1) Get all sentences that contain one of the phrases listed in SEARCH_TERMS
2) Simplify them technicall
3) Get their sentiment and then bring them to a ultra-simple, ultra-condensed format

For the last step I am aiming to get a type of speking like Donald Trump uses it. And I want to
thank Kurt Andersen for his great article on that. Words and construction were taken from there.
https://www.theatlantic.com/magazine/archive/2018/03/how-to-talk-trump/550934/

Additional info
---------------
For more information please see the openprocessing link provided above!

Copyright notice
----------------
The basic senteces are taken from the corpus provided by the Universität Leipzig. Please see the
accroding copyright section "Text Corpus of the Universität Leipzig" in readme.md

"""

from glob import glob
from json import dump, dumps
from random import choice

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from tools import (get_clean_sentence_from_uni_lepizig_line,
                   get_word_frequency, line_into_cleaned_words)

SEARCH_TERMS = ["too complex", "high complexity"]

candidate_sentences = []

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

analyzer = SentimentIntensityAnalyzer()

adjectives_positive = [
    "amazing",
    "beautiful",
    "best",
    "big league",
    "brilliant",
    "elegant",
    "fabulous",
    "fantastic",
    "fine",
    "good",
    "great",
    "happy",
    "honest",
    "incredible",
    "nice",
    "outstanding",
    "phenomenal",
    "powerful",
    "sophisticated",
    "special",
    "strong",
    "successful",
    "top",
    "tremendous",
    "unbelievable",
]

adjectives_negative = [
    "boring",
    "crooked",
    "disgusting",
    "dishonest",
    "dopey",
    "dumb",
    "goofy",
    "horrible",
    "not good",
    "obsolete",
    "out of control",
    "overrated",
    "pathetic",
    "ridiculous",
    "rude",
    "sad",
    "scary",
    "stupid",
    "terrible",
    "unfair",
    "weak",
    "worst",
]

adverbs = [
    "absolutely",
    "badly",
    "basically",
    "certainly",
    "extremely",
    "frankly",
    "greatly",
    "highly",
    "incredibly",
    "totally",
    "truly",
    "unbelievably",
    "very",
    "viciously",
    "way",
]

sentiment_sentences = [
    [
        "### is ~a~ and ~A~ ~n~!",
    ],
    [
        "### is ~a~ ~n~!",
        "~n~! ### is so ~n~!",
    ],
    [
        "### is ~n~!",
    ],
    [
        "### exists.",
        "### does exist.",
        "### is a thing.",
        "### happens.",
        "### is there.",
    ],
    [
        "### is ~p~!",
    ],
    [
        "### is ~a~ ~p~!",
    ],
    [
        "### is ~a~ and ~A~ ~p~!",
    ]
]

for file in glob("data/**/eng_*sentences.txt", recursive=True):
    with open(file, "r", encoding="utf-8") as fh:
        for line in fh:
            for term in SEARCH_TERMS:
                clean_line = get_clean_sentence_from_uni_lepizig_line(line)
                if term.lower() in line.lower():

                    words = line_into_cleaned_words(clean_line)
                    filtered_words = [word for word in words if word.lower() not in stop_words]
                    lemmatized_words = [lemmatizer.lemmatize(x) for x in filtered_words]
                    lemmatized_line = " ".join(lemmatized_words)

                    sentiment = analyzer.polarity_scores(clean_line)["compound"]  # -1: bad -> 1: good

                    # TODO make frequency for lemmatized words and use it

                    frequency_min = 1
                    most_important_word = ""
                    for word in words:
                        freq = get_word_frequency(word)
                        if freq < frequency_min:
                            frequency_min = freq
                            most_important_word = word

                    if sentiment != 0:

                        sentiment_scaled = (sentiment + 1) / 2 * (len(sentiment_sentences)-1)
                        sentiment_int = round(sentiment_scaled)
                        sentiment_sentence = choice(sentiment_sentences[sentiment_int])
                        sentiment_sentence = sentiment_sentence.replace("###", most_important_word)
                        sentiment_sentence = sentiment_sentence.replace("~n~", choice(adjectives_negative))
                        sentiment_sentence = sentiment_sentence.replace("~p~", choice(adjectives_positive))
                        sentiment_sentence = sentiment_sentence.replace("~a~", choice(adverbs))
                        sentiment_sentence = sentiment_sentence.replace("~A~", choice(adverbs))
                        sentiment_sentence = sentiment_sentence[0].upper() + sentiment_sentence[1:]

                        result = {
                            "original": clean_line,
                            "simplified": lemmatized_line,
                            "sentiment": sentiment,
                            "sentiment_sentence": sentiment_sentence,
                            "most_important_word": most_important_word,
                        }
                        print(dumps(result, indent=2))
                        candidate_sentences.append(result)

with open("output/02.json", "w") as fh:
    dump(candidate_sentences, fh, indent=2)
