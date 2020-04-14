def intToRoman(num):
        list1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        list2 = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman= ''
        n=len(list1)
        for i in range(n):
            if num<list1[i]:
                continue
            num = num - list1[i]
            roman = roman +  list2[i]
        return roman
#main program
num=int(input())
res=intToRoman(num)
print(res)
