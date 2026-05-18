class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        t_count = {}
        for c in t:
            t_count[c] = t_count.get(c,0) + 1

        window = {}
        have, need = 0, len(t_count)
        left = 0
        min_len = float("inf")
        min_l = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0) + 1
            if c in t_count and window[c] == t_count[c]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_l = left

                l = s[left]
                window[l] -= 1
                if l in t_count and window[l] < t_count[l]:
                    have -= 1
                left += 1

        return "" if min_len == float("inf") else s[min_l: min_l + min_len]