class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        cache = set()
        while q:
            s = q.popleft()
            for word in wordDict:
                if s.startswith(word):
                    next = s[len(word):]

                    if next == "":
                        return True
                    if next not in cache:
                        q.append(next)
                        cache.add(next)
        return False