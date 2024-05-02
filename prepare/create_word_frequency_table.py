from collections import defaultdict
from glob import glob
from json import dump

total_count = 0
word_frequencies = defaultdict(int)

for file in glob("data/**/eng_*words.txt", recursive=True):
    with open(file, "r", encoding="utf-8") as fh:
        for line in fh:
            parts = line.split("\t")
            word = parts[1].lower()
            count = int(parts[2])

            total_count += count
            word_frequencies[word] += count

for key, val in word_frequencies.items():
    word_frequencies[key] = val/total_count

with open("data/word-frequencies.json", "w") as fh:
    dump(word_frequencies, fh, indent=2)
