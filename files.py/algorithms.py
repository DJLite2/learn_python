# algorithm is work compleate step by step,for example palov cooking steps

# polindrom string   polindrom is gereg  becouse left to right read = right to left read

def polindrom(str):
    startindex = 0
    endindex = len(str) - 1

    for x in str:
        if str[startindex] != str[endindex]:
            return False
        else:
            return True


print(polindrom("racecar"))
print(polindrom("merbrem"))
print(polindrom("hommer"))
