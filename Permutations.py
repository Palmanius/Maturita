class Solution:
    def permute(self, nums=list[int]):
        Solutions = []
        if len(nums) == 1:
            return str(nums[0])
        
        for i in nums:
            for j in Solution.permute("", [x for x in nums if x != i]):
                Solutions.append(str(i)+j)
        
            #Solutions.append([i] +x for x in Solution.permute("",[x for x in nums if x !=i]))
        return Solutions
                
nums = [1,2,3,4]

print(Solution.permute("",nums))
        