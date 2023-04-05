def solve(keys, n, chests):
    keyCounts = {i: 0 for i in range(201)}
    for key in keys:
        keyCounts[key] += 1
    path = []
    searchStartIndex = 0
    while True:
        chestOpened = False
        for cI in range(searchStartIndex, n):
            (lock, newKeys) = chests[cI]
            if lock > 0 and keyCounts[lock] > 0:
                path.append(cI)
                keyCounts[lock] -= 1
                for newKey in newKeys:
                    keyCounts[newKey] += 1
                chests[cI][0] = -lock
                chestOpened = True
                break
        if chestOpened:
            if len(path) == n:
                s = ""
                for i in path:
                    s += " " + str(i+1)
                return s[1:]
            searchStartIndex = 0
        else:
            if len(path) == 0:
                return "IMPOSSIBLE"
            lastOpenedChestI = path.pop(len(path)-1)
            (lock, newKeys) = chests[lastOpenedChestI]
            lock = -lock
            keyCounts[lock] += 1
            for newKey in newKeys:
                keyCounts[newKey] -= 1
            chests[lastOpenedChestI][0] = lock
            searchStartIndex = lastOpenedChestI + 1


if __name__ == "__main__":
    testCount = int(input())
    for i in range(testCount):
        (k, n) = [int(s) for s in input().split(" ")]
        keys = [int(s) for s in input().split(" ")]
        chests = []
        for _ in range(n):
            line = input().split(" ")
            chests.append([int(line[0]), [int(s) for s in line[2:]]])
        print("Case #" + str(i+1) + ": " + solve(keys, n, chests))
