class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = right = 0
        #return value
        if_anagram = False

        #anagram string is != the original
        if len(t)!=len(s):
            return if_anagram

        expected_cache = [0]*26
        string_cache = [0]*26

        #save the original string as a numeric cache
        for char in s:
            pos = ord(char.lower())-ord('a')
            expected_cache[pos]+=1

        #save a string to check as a numeric cache
        for char in t:
            pos = ord(char.lower())-ord('a')
            string_cache[pos]+=1


        if string_cache == expected_cache:
            if_anagram = True   

        return if_anagram