def solve(matrix, h, w):
    rMaxes = [0 for _ in range(h)]
    cMaxes = [0 for _ in range(w)]
    for y in range(h):
        for x in range(w):
            n = matrix[y][x]
            rMaxes[y] = max(rMaxes[y], n)
            cMaxes[x] = max(cMaxes[x], n)
    for y in range(h):
        for x in range(w):
            n = matrix[y][x]
            if n != rMaxes[y] and n != cMaxes[x]:
                return "NO"
    return "YES"


if __name__ == "__main__":
    testCount = int(input())
    for i in range(testCount):
        (h, w) = input().split(" ")
        h = int(h)
        w = int(w)
        matrix = []
        for hI in range(h):
            matrix.append([int(s) for s in input().split()])
        print("Case #" + str(i+1) + ": " + solve(matrix, h, w))
