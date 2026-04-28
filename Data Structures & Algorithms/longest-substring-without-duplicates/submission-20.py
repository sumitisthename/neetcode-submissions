class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0, 0
        char_set = set()
        max_size = 0
        while j <= len(s)-1:
            if s[j] not in char_set:
                char_set.add(s[j])
                max_size = max(max_size, len(char_set))
                j+=1
            else:
                char_set.remove(s[i])
                i+= 1
        return max_size