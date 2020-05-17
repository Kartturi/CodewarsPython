
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


def longestPalindrome(self, s: str) -> str:
    founded_palindromes = []


def checkIfPalindrome(str):
    result = ""
    for s in str:
        result = result + s
    if result == str:
        return True
    else:
        return False


def longestPalindrome2(s: str) -> str:
    def expand(s, l, r):
        while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
            l -= 1
            r += 1
        return r-l-1
    if s == None or len(s) < 1:
        return ""
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand(s, i, i)
        len2 = expand(s, i, i+1)
        maxl = max(len1, len2)
        if maxl > end-start:
            start = i-(maxl-1)//2
            end = i+maxl//2
    return s[start:end+1]


print(longestPalindrome2("abababab"))
