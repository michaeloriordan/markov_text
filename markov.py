import random


class MarkovText:
    def __init__(phrase_len=1):
        self.phrase_len = phrase_len
        self.phrase_dict = {}

    def build_dict(filename=None):
        with open(filename) as f:
            allwords = [word for line in f for word in line.split()]

        zipwords = zip(*[allwords[i:] for i in range(self.phrase_len+1)])

        for *words, next_word in zipwords:
            phrase = ' '.join(words)
            if phrase in self.phrase_dict:
                phrase_dict[phrase].append(next_word)
            else:
                phrase_dict[phrase] = [next_word]


with open('lotr.txt') as f:
    fulltext = [word for line in f for word in line.split()]

zipped_words = zip(fulltext, fulltext[1:], fulltext[2:], fulltext[3:])

markov_dict = {}

for *words, next_word in zipped_words:
    phrase = ' '.join(words)
    if phrase in markov_dict:
        markov_dict[phrase].append(next_word)
    else:
        markov_dict[phrase] = [next_word]


def choose_next_word(phrase):
    return random.choice(markov_dict[phrase])


story = 'There was a'.split()
for i in range(200):
    phrase = ' '.join([story[i+j] for j in range(3)])
    story.append(choose_next_word(phrase))

print(' '.join(story))
