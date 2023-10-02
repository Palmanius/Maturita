with open("nums.txt","r") as f:

    for line in f:
        nums = line.split(",")
        nums = [int(x) for x in nums]
        nums.sort()

def threeSum(self, nums):
        Solutions = []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = len(nums)-1

            while l<r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    Solve = [nums[i],nums[l],nums[r]]
                    Solutions.append(Solve)
                    while l<r and nums[l] == Solve[1]:
                        l += 1
                    while l<r and nums[r] == Solve[2]:
                        r -= 1 
        return Solutions
print(threeSum("",nums))