"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        valCnt = dict()
        map = {'A' : 0, 'C' : 1, 'G': 2, 'T' : 3}
        sum = 0
        for x in range(len(s)):
            sum = (sum * 4 + map[s[x]]) & 0xFFFFF
            if x < 9:
                continue
            valCnt[sum] = valCnt.get(sum, 0) + 1
            if valCnt[sum] == 2:
                ans.append(s[x - 9 : x + 1])
        return ans