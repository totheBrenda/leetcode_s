## https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1 : return 'a'*n
        else : return 'a'*(n-1)+'b'