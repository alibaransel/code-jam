import math
import decimal


def solve(r, t):
    decimal.getcontext().prec = 100
    a = 2
    b = 2*r - 1
    c = -t
    x = (-b + decimal.Decimal(b**2 - 4*a*c).sqrt()) / (2*a)
    return math.floor(x)


if __name__ == "__main__":
    testCount = int(input())
    for i in range(testCount):
        (r, t) = [int(s) for s in input().split(" ")]
        print("Case #" + str(i+1) + ": " + str(solve(r, t)))
