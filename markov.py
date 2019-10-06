import random


class MarkovText:
    def __init__(self, phrase_len=1):
        self.phrase_len = phrase_len
        self.phrase_dict = {}

    def build_dict(self, filename=None):
        with open(filename) as f:
            allwords = [word for line in f for word in line.split()]

        zipwords = zip(*[allwords[i:] for i in range(self.phrase_len+1)])

        for *words, next_word in zipwords:
            phrase = ' '.join(words)
            if phrase in self.phrase_dict:
                self.phrase_dict[phrase].append(next_word)
            else:
                self.phrase_dict[phrase] = [next_word]

    def choose_next_word(self, phrase):
        return random.choice(self.phrase_dict[phrase])

    def generate_story(self, story_len=200, phrase_init=None):
        story = phrase_init.split()
        assert len(story) == self.phrase_len, f'phrase length != {self.phrase_len}'
        for i in range(story_len):
            phrase = ' '.join([story[i+j] for j in range(self.phrase_len)])
            story.append(self.choose_next_word(phrase))

        print(' '.join(story))


if __name__ == '__main__':
    markov_text = MarkovText(phrase_len=3)
    markov_text.build_dict(filename='lotr.txt')
    markov_text.generate_story(story_len=200, phrase_init='There was a')
