import math
import decimal


def solve(a, b):
    decimal.getcontext().prec = 100
    f = math.ceil(decimal.Decimal(a).sqrt())
    l = math.floor(decimal.Decimal(b).sqrt())
    (lCount, _) = getCountUpTo(l)
    (fCount, fIn) = getCountUpTo(f)
    result = lCount - fCount
    if fIn:
        result += 1
    return result


global lastDigitCount

oneTwoThree = [
    (1, 0, 0),
    (2, 0, 0),
    (3, 0, 0),
    (4, 0, 0),
    (5, 0, 0),
    (6, 0, 0),
    (7, 0, 0),
    (8, 0, 0),
    (9, 0, 0),
    (0, 1, 0),
    (2, 1, 0),
    (4, 1, 0),
    (0, 2, 0),
    (1, 2, 0),
    (0, 0, 1),
]

lastDigitCount = 0

numbers = []


def getCountUpTo(limit):
    limitStr = str(limit)
    limitDigitCount = len(limitStr)
    if lastDigitCount < limitDigitCount:
        fillNumbers(limitDigitCount)
    return getNumberCount(limitStr)


def fillNumbers(limitDigitCount):
    global lastDigitCount
    for digitCount in range(lastDigitCount+1, limitDigitCount+1):
        newNumbers = []
        if digitCount % 2 == 1:
            for (c1, c2, c3) in oneTwoThree:
                cT = c1 + c2 + c3
                if cT <= digitCount:
                    c0 = digitCount - cT
                    mid = ""
                    if c1 % 2 == 1:
                        mid = "1"
                        c1 -= 1
                    elif c2 % 2 == 1:
                        mid = "2"
                        c2 -= 1
                    elif c3 % 2 == 1:
                        mid = "3"
                        c3 -= 1
                    else:
                        mid = "0"
                        c0 -= 1
                    c0 //= 2
                    c1 //= 2
                    c2 //= 2
                    c3 //= 2
                    if digitCount == 1:
                        newNumbers.append([mid])
                    elif c2 == 1:
                        c2 -= 1
                        newNumbers.append(
                            ["2" + "0" * c0 + mid + "0" * c0 + "2"]
                        )
                    elif c1 > 0:
                        c1 -= 1
                        newNumbers.append(
                            ["1" + s + mid + s[::-1] + "1"
                                for s in getZeroOneCombinations(c0, c1)]
                        )
        else:
            for (c1, c2, _) in oneTwoThree:
                if c1 % 2 + c2 % 2 == 0:
                    cT = c1 + c2
                    if cT <= digitCount and cT % 2 == 0:
                        c0 = digitCount - cT
                        c0 //= 2
                        c1 //= 2
                        c2 //= 2
                        if c2 == 1:
                            newNumbers.append(["2" + "0" * c0 * 2 + "2"])
                        elif c1 > 0:
                            c1 -= 1
                            newNumbers.append(
                                ["1" + s + s[::-1] + "1"
                                    for s in getZeroOneCombinations(c0, c1)]
                            )
        numbers.extend(joinSorted(newNumbers))
        lastDigitCount += 1


zeroOneCombinationMemory = {}


def getZeroOneCombinations(c0, c1):
    if c1 < 0:
        pass
    if (c0, c1) in zeroOneCombinationMemory.keys():
        return zeroOneCombinationMemory[(c0, c1)]
    combinations = []
    if c1 == 0:
        combinations = ["0" * c0]
    elif c1 == 1:
        combinations = ["0" * (c0-i) + "1" + "0" * i for i in range(c0+1)]
    elif c1 == 2:
        for i1 in range(c0, -1, -1):
            for i2 in range(c0-i1, -1, -1):
                combinations.append("0" * i1 + "1" + "0" *
                                    i2 + "1" + "0" * (c0-i1-i2))
    elif c1 == 3:
        for i1 in range(c0, -1, -1):
            for i2 in range(c0-i1, -1, -1):
                for i3 in range(c0-i1-i2, -1, -1):
                    combinations.append(
                        "0" * i1 + "1" + "0" * i2 + "1" + "0" * i3 + "1" + "0" * (c0-i1-i2-i3))
    zeroOneCombinationMemory[(c0, c1)] = combinations
    return combinations


def joinSorted(groups):
    sortedList = []
    while len(groups) > 0:
        minGroupI = 0
        minValue = "a"
        removeList = []
        for i in range(len(groups)):
            if len(groups[i]) == 0:
                removeList.append(i)
            else:
                value = groups[i][0]
                if value < minValue:
                    minGroupI = i
                    minValue = value
        sortedList.append(minValue)
        for removeI in removeList:
            groups.pop(i)
        groups[minGroupI].pop(0)
        if len(groups[minGroupI]) == 0:
            groups.pop(minGroupI)
    return sortedList


def getNumberCount(n):
    s = 0
    e = len(numbers)-1
    m = 0
    while s <= e:
        m = (s + e)//2
        if isFirstSmaller(n, numbers[m]):
            e = m - 1
        elif isFirstSmaller(numbers[m], n):
            s = m + 1
        else:
            return (m + 1, True)
    return (s, False)


def isFirstSmaller(s1, s2):
    s1Length = len(s1)
    s2Length = len(s2)
    if s1Length < s2Length:
        return True
    if s1Length > s2Length:
        return False
    return s1 < s2


if __name__ == "__main__":
    testCount = int(input())
    for i in range(testCount):
        (a, b) = (int(s) for s in input().split(" "))
        print("Case #" + str(i+1) + ": " + str(solve(a, b)))
