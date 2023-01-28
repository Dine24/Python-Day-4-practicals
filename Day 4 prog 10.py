import random

def is_scrambled(s1, s2):
    if s1 == s2:
        return True
    if sorted(s1) != sorted(s2):
        return False
    for i in range(1, len(s1)):
        if (is_scrambled(s1[:i], s2[:i]) and is_scrambled(s1[i:], s2[i:])) or (is_scrambled(s1[:i], s2[-i:]) and is_scrambled(s1[i:], s2[:-i])):
            return True
    return False

s1 = "great"
s2 = "rgeat"
print(is_scrambled(s1, s2))

s1 = "abcde"
s2 = "caebd"
print(is_scrambled(s1, s2))

s1 = "a"
s2 = "a"
print(is_scrambled(s1, s2))

s1 = "ab"
s2 = "ad"
print(is_scrambled(s1, s2))  

