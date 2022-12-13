import re


class Autocompleter:
    def __init__(self):
        self.bigrams = {}
        self.trigrams = {}
        self.fourgrams = {}
        self.dictionary = {}

        with open("plugins/autocomplete/bigrams.txt", 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split()
                self.bigrams[words[0]] = words[1]
        with open("plugins/autocomplete/trigrams.txt", 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split()
                self.trigrams[words[0] + ' ' + words[1]] = words[2]
        with open("plugins/autocomplete/fourgrams.txt", 'r', encoding='utf-8') as f:
            for line in f:
                words = line.split()
                self.trigrams[words[0] + ' ' + words[1] + ' ' + words[2]] = words[3]
        with open("plugins/autocomplete/dictionary.txt", 'r', encoding='utf-8') as f:
            for line in f:
                elements = line.split()
                self.dictionary[elements[0]] = int(elements[1])


    def _get_next_by_previous_words(self, previous_word):
        key = previous_word
        if key in self.bigrams:
            return self.bigrams[key]
        return ''

    def get_next_by_previous_words(self, pr):
        answ = self._get_next_by_previous_words(pr)
        print(f'from {pr} returned {answ}')
        return answ

    def get_next_by_prefix(self, prefix):
        suitable = []
        for word in self.dictionary:
            if len(word) >= len(prefix) and word[:len(prefix)] == prefix:
                suitable.append((word, self.dictionary[word]))
        if len(suitable) == 0:
            return ''
        print(f'from {prefix} returned {max(suitable, key=lambda x: x[1])}')
        return max(suitable, key=lambda x: x[1])
