class Solution:
    def fizzBuzz(self, n: int):
        solve = []
        for i in range(1,n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    solve.append("FizzBuzz")
                else:
                    solve.append("Fizz")
            elif i % 5 == 0:
                solve.append("Buzz")
            else:
                solve.append(str(i))
        return(solve)
print(Solution.fizzBuzz("",10))