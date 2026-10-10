class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        # create a dict of letters and num of occurences
        letters = {}
        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1

        # decrement counts using t
        for letter in t:
            if letter not in letters or letters[letter] == 0:
                return False
            letters[letter] -= 1

        return True