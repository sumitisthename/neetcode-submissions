class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        m = len(s1)
        s1 = ''.join(sorted(s1))
        l = 0
        r = m
        status = False

        for i in range(n):
            sub_str= s2[l:r]
            sub_str = ''.join(sorted(sub_str))
            print(sub_str)
            if s1 == sub_str:
                status = True
            r+=1
            l+=1
            print(sub_str)
        return status
