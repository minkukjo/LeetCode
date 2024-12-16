class Node:
    def __init__(self):
        self.map = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()
        self.failed = [False] * 301

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.map:
                node.map[ch] = Node()
            node = node.map[ch]
        node.isEnd = True
    
    def search(self, s, start):
        if self.failed[start]:
            return False
        if start >= len(s):
            return True
        node = self.root
        for i in range(start, len((s))):
            if s[i] not in node.map:
                return False
            node = node.map[s[i]]
            if node.isEnd:
                if self.search(s, i+1):
                    return True
                self.failed[i+1] = True
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        return trie.search(s, 0)