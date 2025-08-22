class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_string =min(strs, key=len)
        ret=""
        for idx,c in enumerate(min_string):
                if(all(c==strs[j][idx] for j in range(len(strs)))):
                    ret=ret+c
                else:
                    break
        return ret
        