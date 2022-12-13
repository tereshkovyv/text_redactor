import re


bigrams = {}
trigrams = {}
fourgrams = {}
dictionary = {}


def prepare_ngrams(input):
    with open(input, 'r', encoding='cp1251') as f:
        for line in f:
            line = line.lower()
            reg = re.compile('[^а-я ]')
            line = reg.sub('', line)
            words = line.split()
            for i in range(len(words)):
                if i > 0:
                    key = words[i - 1]
                    method_name(bigrams, key, words[i])
                if i > 1:
                    key = words[i - 2] + ' ' + words[i - 1]
                    method_name(trigrams, key, words[i])
                if i > 2:
                    key = words[i - 3] + ' ' + words[i - 2] + ' ' + words[i - 1]
                    method_name(fourgrams, key, words[i])
                increment(dictionary, words[i])



def write_ngrams():
    with open("bigrams.txt", 'w', encoding='utf-8') as f:
        for bigram in bigrams:
            f.write(bigram + ' ' + get_max_element(bigrams[bigram]) + '\n')
    with open("trigrams.txt", 'w', encoding='utf-8') as f:
        for trigram in trigrams:
            f.write(trigram + ' ' + get_max_element(trigrams[trigram]) + '\n')
    with open("fourgrams.txt", 'w', encoding='utf-8') as f:
        for fourgram in fourgrams:
            f.write(fourgram + ' ' + get_max_element(fourgrams[fourgram]) + '\n')
    dictionary_sorted = sorted(dictionary.items(), key=lambda x: x[0])
    with open("dictionary.txt", 'w', encoding='utf-8') as f:
        for word in dictionary_sorted:
            f.write(word[0] + ' ' + str(word[1]) + '\n')


def get_max_element(dic):
    max_count = 0
    max_word = ""
    for word in dic:
        if dic[word] > max_count:
            max_count = dic[word]
            max_word = word
    return max_word


def method_name(ngrams, key, word):
    if key not in ngrams:
        ngrams[key] = {}
    increment(ngrams[key], word)


def increment(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1


prepare_ngrams("pushkin.txt")
write_ngrams()