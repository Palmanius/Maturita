def toRoman(num):
    conversion_table = [[1,"I"],
                    [4,"IV"],
                    [5,"V"],
                    [9,"IX"],
                    [10,"X"],
                    [40,"XL"],
                    [50,"L"],
                    [90,"XC"],
                    [100,"C"],
                    [400,"CD"],
                    [500,"D"],
                    [900,"CM"],
                    [1000,"M"]]
    
    conversion_table = conversion_table[::-1]
    
    roman = ""
    
    for i in conversion_table:
        if num>0:
            if num//i[0] != 0:
                roman += i[1] * (num//i[0])
                num = num % i[0]

    return roman


print((-1)//(1000))
print(toRoman(-1))