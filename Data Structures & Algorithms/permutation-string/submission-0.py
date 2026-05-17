class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1 = [0] * 26
        for s in s1:
            count_s1[ord(s) - ord('a')] += 1

        count_s2 = [0] * 26
        window_size = len(s1)

        # Step 2: build first window
        for i in range(window_size):
            count_s2[ord(s2[i]) - ord('a')] += 1

        # Step 3: slide the window
        for right in range(window_size, len(s2)):
            if count_s1 == count_s2:
                return True
            count_s2[ord(s2[right]) - ord('a')] += 1               # add new right char
            count_s2[ord(s2[right - window_size]) - ord('a')] -= 1  # remove old left char

        return count_s1 == count_s2  # check the last window