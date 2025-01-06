class Solution:
    def shiftingLetters(self, s, shifts):
        #oh this was hard for me so I looked up sol
        n = len(s)
        prefix_diff = [0] * (n + 1)
        for l, r, d in shifts:
            prefix_diff[r + 1] += 1 if d else -1
            prefix_diff[l] += -1 if d else 1
        diff = 0
        res = [ord(c) - ord("a") for c in s]
        for i in reversed(range(n + 1)):
            diff += prefix_diff[i]
            res[i - 1] = (diff + res[i - 1]) % 26
        s = [chr(ord("a") + n) for n in res]
        return "".join(s)
