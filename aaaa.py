class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        number = 0

        for i in range(low,high+1):
            if len(str(i)) % 2 == 0:
                x = str(i)[:len(str(i))//2]
                y = str(i)[len(str(i))//2:]
                if sum([int(j) for j in x]) == sum([int(k) for k in y]):
                    number += 1
        #         FHsum = 0
        #         SHsum = 0
        #         for a in FH:
        #             FHsum += int(a)
        #         for b in SH:
        #             SHsum += int(b)
        #         if FHsum == SHsum:
        #             number += 1
        return number

print(Solution.countSymmetricIntegers("",1200,1230))