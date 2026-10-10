class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]
        res = ""

        for j in range(len(first_string)):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != first_string[j]:
                    return res
            res += first_string[j]

        return res
