def solve(n, x, y):
    if x < 0:
        x *= -1
    a = x + y - 1
    if x == 0:
        a += 2
        b = a * (a + 1) // 2
        if n >= b:
            return 1.0
        else:
            return 0.0
    b = a * (a + 1) // 2
    t = y + 1
    if n < b + t:
        return 0.0
    if n >= b + a + 1 + t:
        return 1.0
    if n == b + t:
        return (0.5)**(t)
    n -= b
    correct = 0
    for tx in range(n+1):
        if tx >= t or n - tx > a + 1 + t:
            correct += comb(n, tx)
    return correct / 2**n


combMemory = {}


def comb(r, n):
    n = min(n, r - n)
    if n == 0:
        return 1
    if (r, n) in combMemory.keys():
        return combMemory[(r, n)]
    result = 1
    for i in range(n):
        result *= r - i
    for i in range(n, 0, -1):
        result //= i
    combMemory[(r, n)] = result
    return result


if __name__ == "__main__":
    testCount = int(input())
    s = ""
    for i in range(testCount):
        (n, x, y) = [int(s) for s in input().split(" ")]
        s += "Case #" + str(i+1) + ": " + str(solve(n, x, y)) + "\n"
    print(s)
