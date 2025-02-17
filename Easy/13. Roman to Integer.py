class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.replace("IV", "1")
        s = s.replace("IX", "2")
        s = s.replace("XL", "3")
        s = s.replace("XC", "4")
        s = s.replace("CD", "5")
        s = s.replace("CM", "6")
        res = 0
        for i in s:
            if i == "M":
                res += 1000
            elif i == "D":
                res += 500
            elif i == "C":
                res += 100
            elif i == "L":
                res += 50
            elif i == "X":
                res += 10
            elif i == "V":
                res += 5
            elif i == "I":
                res += 1
            elif i == "1":
                res += 4
            elif i == "2":
                res += 9
            elif i == "3":
                res += 40
            elif i == "4":
                res += 90
            elif i == "5":
                res += 400
            elif i == "6":
                res += 900

        return res
