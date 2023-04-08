def solve(a, n, motes):
    if a == 1:
        return n
    absorbCount = 0
    motes.sort()
    moteList = []
    for mote in motes:
        if mote < a:
            a += mote
            absorbCount += 1
        else:
            extraMoteCount = 1
            a += a - 1
            while a <= mote:
                extraMoteCount += 1
                a += a - 1
            moteList.append([extraMoteCount, n - absorbCount])
            a += mote
            absorbCount += 1
    currCount = 0
    minCount = 101
    for (add, remove) in moteList:
        minCount = min(minCount, currCount + remove)
        if add < remove:
            currCount += add
            if currCount >= minCount:
                return minCount
        else:
            return minCount
    return min(minCount, currCount)


if __name__ == "__main__":
    testCount = int(input())
    for i in range(testCount):
        (a, n) = [int(s) for s in input().split(" ")]
        motes = [int(s) for s in input().split(" ")]
        print("Case #" + str(i+1) + ": " + str(solve(a, n, motes)))
