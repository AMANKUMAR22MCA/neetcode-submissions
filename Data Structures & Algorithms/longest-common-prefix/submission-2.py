class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        first_str = strs[0]
        for i in range(len(first_str)):
           for word in strs[1:]:
              if i >= len(word) or word[i]!=first_str[i]:
                  return first_str[:i]
        return first_str        