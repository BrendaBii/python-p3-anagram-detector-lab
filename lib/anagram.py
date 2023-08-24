# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        my_word = [letter for letter in self.word]
        my_list = []
        for item in list:
            word_list = [l for l in item]
            if(sorted(my_word) == sorted(word_list)):
                my_list.append(item)
        return my_list