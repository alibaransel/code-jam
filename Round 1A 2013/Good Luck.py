import random


def solve(n, m, k, products):
    primeCounts = [0, 0, 0, 0]
    twoCount = 0
    fourCount = 0
    eightCount = 0
    for product in products:
        for primeI in range(4):
            prime = primes[primeI]
            count = 0
            while product % prime == 0:
                count += 1
                product //= prime
            primeCounts[primeI] = max(primeCounts[primeI], count)
            if prime == 2 and count > 0:
                if count == 1:
                    twoCount += 1
                elif count == 2:
                    fourCount += 1
                else:
                    eightCount += 1
    numberCount = sum(primeCounts)
    if numberCount == n:
        result = ""
        for primeI in range(4):
            result += str(primes[primeI]) * primeCounts[primeI]
        return result
    elif numberCount < n:
        result = ""
        for primeI in range(4):
            result += str(primes[primeI]) * primeCounts[primeI]
        result += "1" * (n - numberCount)
        return result
    else:
        diff = numberCount - n
        if m == 5:
            result = ""
            primeCounts[0] -= diff * 2
            for primeI in range(4):
                result += str(primes[primeI]) * primeCounts[primeI]
            result += "4" * diff
            return result
        else:
            c2 = primeCounts[0]
            c3 = primeCounts[1]
            c5 = primeCounts[2]
            c7 = primeCounts[3]
            c4 = 0
            c8 = 0
            if diff % 2 == 1:
                c4 += 1
                diff -= 1
            if fourCount > 0 and c4 == 0:
                c4 += 1
                diff -= 1
            if eightCount > 0:
                c8 += 1
                diff -= 2
            c8New = random.randint(0, diff // 4)
            c4New = diff - 2 * c8New
            c8 += c8New
            c4 += c4New
            result = ""
            result += "2" * (c2 - 2 * c4 - 3 * c8)
            result += "3" * c3
            result += "4" * c4
            result += "5" * c5
            result += "7" * c7
            result += "8" * c8
            return result


primes = [2, 3, 5, 7]

if __name__ == "__main__":
    input()
    (r, n, m, k) = [int(s) for s in input().split(" ")]
    print("Case #1:")
    for _ in range(r):
        products = [int(s) for s in input().split(" ")]
        print(solve(n, m, k, products))
