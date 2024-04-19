class Trie:

    def __init__(self):
        self.s = set()
        self.startsW = set()
        

    def insert(self, word: str) -> None:
        
        for i in range(len(word)):
            self.startsW.add(word[0:i+1]) 
        self.s.add(word)

    def search(self, word: str) -> bool:
        return word in self.s

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.startsW