class TrieNode:
    def __init__(self):
        self.child= {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.child:
                curr.child[i] = TrieNode()
            curr = curr.child[i]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.child:
                return False
            curr=curr.child[i]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i not in curr.child:
                return False
            curr = curr.child[i]
        return True
