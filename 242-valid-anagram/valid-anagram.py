class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = right = 0
        #return value
        if_anagram = False

        #anagram string is != the original
        if len(t)!=len(s):
            return if_anagram

        expected_cache = {}
        string_cache = {}

        #save the original string as a numeric cache
        for char in s:
            expected_cache[char]=expected_cache.get(char,0)+1

        #save a string to check as a numeric cache
        for char in t:
            string_cache[char]=string_cache.get(char,0)+1


        if sorted(string_cache.items()) == sorted(expected_cache.items()):
            if_anagram = True   

        return if_anagram