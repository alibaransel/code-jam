def solve(e, r, n, vList):
    distances = [0 for _ in range(n)]
    oldVList = []
    oldVIList = []
    for vI in range(n):
        v = vList[vI]
        for i in range(len(oldVList) - 1, -1, -1):
            oldV = oldVList[i]
            if oldV < v:
                oldVI = oldVIList.pop(i)
                oldVList.pop(i)
                distances[oldVI] = vI - oldVI
            else:
                break
        oldVList.append(v)
        oldVIList.append(vI)
    currE = e
    result = 0
    for i in range(n):
        v = vList[i]
        d = distances[i]
        if d == 0:
            result += v * currE
            currE = 0
        else:
            extraE = currE + d * r - e
            if extraE > 0:
                eSpend = min(currE, extraE)
                currE -= eSpend
                result += v * eSpend
        currE += r
    return result


if __name__ == "__main__":
    testCount = int(input())
    for i in range(testCount):
        (e, r, n) = [int(s) for s in input().split(" ")]
        vList = [int(s) for s in input().split(" ")]
        print("Case #" + str(i+1) + ": " + str(solve(e, r, n, vList)))
