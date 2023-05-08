class Trie:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        cur = self.trie

        for char in word:
            if char not in cur.child:
                cur.child[char] = Trie()
            cur = cur.child[char]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.isEnd

            if word[index] == ".":
                for child in node.child.values():
                    if dfs(child, index+1):
                        return True
            
            if word[index] in node.child:
                return dfs(node.child[word[index]], index+1)
            return False
        return dfs(self.trie, 0)
