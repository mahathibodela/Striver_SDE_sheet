from collections import defaultdict
from bisect import bisect_right

class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        m = defaultdict(list)
        
        for index, char in enumerate(s):
            m[char].append(index)
        
        count = 0
        
        for word in words:
            pre = -1
            found = True
            for char in word:
                if char not in m:
                    found = False
                    break
                it = bisect_right(m[char], pre)
                if it == len(m[char]):
                    found = False
                    break
                pre = m[char][it]
            if found:
                count += 1
        
        return count
