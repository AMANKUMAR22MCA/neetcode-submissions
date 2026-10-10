class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            # res= {}
            # for num in nums :
            #     if num in res:
            #         res[num]+=1
            #     else:
            #         res[num]=1
            # for i , v in res.items():
            #     if v>1:
            #         return True
            # return False  

            res= set()
            for num in nums:
                if num in res:
                    return True    
                else:
                    res.add(num)   
            return False                   
                    