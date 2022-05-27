# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if sorted(word) == sorted(anagram):
        print('they are anagram')
        return True
    else:
        print('they are not anagram')
        return False


find_anagram('welcome', 'emoclew')

