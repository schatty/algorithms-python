"""Given a string, write a function to check if it is a 
permutation of a palindrome. A palindrom is a word or
phrase that is the same forwards and backwards. A
permutation is a rearrangement of letters. The palidrone
does not need to be limited to just dictionary words. """

from collections import Counter


def is_perm(s):
    s = ''.join([c for c in s if c.isalpha()])
    s = s.lower()
   
    cnt = Counter(s)
    allowed_odd = 1 if len(s) % 2 == 1 else 0
    odds = 0
    for k, v in cnt.items():
        if v % 2 == 1:
            odds += 1
            if odds > allowed_odd:
                return False
    return True
        


s1 = "Tact Coa."
print(is_perm(s1))
