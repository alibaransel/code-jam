
def solve(e, r, n, vList):
    vListSum = 0
    vListMax = vList[0]
    maxCount = 0
    for v in vList:
        vListSum += v
        if v > vListMax:
            vListMax = v
            maxCount = 1
        elif v == vList:
            maxCount += 1
    return vListSum * r + (e - r) * vListMax


if __name__ == "__main__":
    testCount = int(input())
    for i in range(testCount):
        (e, r, n) = [int(s) for s in input().split(" ")]
        vList = [int(s) for s in input().split(" ")]
        print("Case #" + str(i+1) + ": " + str(solve(e, r, n, vList)))
