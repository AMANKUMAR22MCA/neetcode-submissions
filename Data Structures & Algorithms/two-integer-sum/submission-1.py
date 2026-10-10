class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res={}
        for index , value in enumerate(nums):
            diff = target - value
            if diff in res:
                return [res[diff],index]
            else:
                res[value]=index    
        return []        

 
        