"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.childs = dict()
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        node = self.root
        for letter in word:
            child = node.childs.get(letter)
            if child is None:
                child = TrieNode()
                node.childs[letter] = child
            node = child
        node.isWord = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        return self.find(self.root, word)
    
    def find(self, node, word):
        if word == '':
            return node.isWord
        if word[0] == '.':
            for x in node.childs:
                if self.find(node.childs[x], word[1:]):
                    return True
        else:
            child = node.childs.get(word[0])
            if child:
                return self.find(child, word[1:])
        return False