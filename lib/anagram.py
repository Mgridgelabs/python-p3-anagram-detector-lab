
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = ''.join(sorted(self.word))

    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            sorted_candidate = ''.join(sorted(candidate.lower()))
            if sorted_candidate == self.sorted_word:
                matches.append(candidate)
        return matches

anagram = Anagram('listen')
print(anagram.match(['enlists', 'google', 'inlets', 'banana']))              