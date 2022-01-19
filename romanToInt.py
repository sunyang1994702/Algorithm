"""
Roman to Integer
Link: https://leetcode.com/problems/roman-to-integer/
"""

def romanToInt_1(self, s: str) -> int:
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, 
                "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    index = 1
    res = 0

    ## Looping the String s from back to front. 
    while index < len(s):
        twoBit_str = s[-(index+1)]+s[-index]
        if twoBit_str in roman_dic:
            res += roman_dic[twoBit_str]
            index += 2
        else:
            res += roman_dic[s[-index]]
            index += 1

    if index > len(s):
        return res
    else:
        return res + roman_dic[s[0]]


def romanToInt_2(self, s: str) -> int:
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    for i in range(len(s)):
        if i + 1 < len(s) and roman_dic[s[i]] < roman_dic[s[i+1]]:
            ## If the roman's number is smaller than right side roman's number
            ## Then substract current roman's number.
            res -= roman_dic[s[i]]
        else:
            ## If not, just add it normally. 
            res += roman_dic[s[i]]
    return res