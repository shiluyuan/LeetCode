"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
"""
"""
bfs
"""
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        wordDict = set(wordList)

        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path
                    for child in tree[source]
                    for path in construct_paths(child, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw:
                tree[word] += neigh,
            else:
                tree[neigh] += word,

        def bfs(this_lev, oth_lev, is_forw):
            nonlocal tree, wordDict
            if not this_lev:
                return False
            if len(this_lev) > len(oth_lev):
                return bfs(oth_lev, this_lev, not is_forw)
            for word in (this_lev | oth_lev):
                wordDict.discard(word)
            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index+1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)
                        if not done and neigh in wordDict:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs(next_lev, oth_lev, is_forw)

        tree = collections.defaultdict(list)
        is_found = bfs(set([beginWord]), set([endWord]), True)
        return construct_paths(beginWord, endWord, tree)