import collections
import itertools
import sys


def read_words(word_file):
    with open(word_file) as f:
        return set(f.read().split())


def read_tokens(token_file):
    with open(token_file) as f:
        for i, line in enumerate(f, 1):
            for token in line.split():
                yield i, token


def spell_check(tokens, words):
    top_n_words_to_print = 10
    for i, token in tokens:
        result = "Line {0} : {1} (".format(i, token)
        matched = {}
        for word in words:
            if has_same_char(token, word):
                matched[word] = levenshtein_distance(token, word)
        if 0 < len(matched):
            for word, distance in itertools.islice(
                collections.OrderedDict(
                    sorted(matched.items(), key=lambda w: w[1])
                ).items(),
                top_n_words_to_print,
            ):
                result += "{0}:{1} ".format(word, distance)
            result = "{0})".format(result.rstrip())
        else:
            result += "not in dictionary)"
        print(result)


def has_same_char(token, word):
    for c in set(token):
        if c.lower() in word.lower():
            return True
    return False


def levenshtein_distance(s, t):
    distances = range(len(s) + 1)
    for ti, tc in enumerate(t, 1):
        new_distances = [ti] + [0] * (len(s))
        for si, sc in enumerate(s):
            new_distances[si + 1] = (
                distances[si]
                if sc.lower() == tc.lower()
                else 1 + min((distances[si], distances[si + 1], new_distances[si]))
            )
        distances = new_distances
    return distances[-1]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Please input a filename.")
    spell_check(read_tokens(sys.argv[1]), read_words("words.txt"))
