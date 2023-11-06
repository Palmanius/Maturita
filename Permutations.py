class Solution:
    LoN = []
    def permute(self=list[int], nums=list[int]):
        if len(nums) < 2:
            return Solution.LoN.append(self)
        else:
            for i in nums:
                self.append(i)
                NewNums = [x for x in nums if x!=i]
                Solution.permute(self,NewNums)
 
        return Solution.LoN




        



nums = [1,2,3]

print(Solution.permute([],nums))
        