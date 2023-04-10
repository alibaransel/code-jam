def solve(s):
    firstFour = s[:4]
    (oneLength, twoLength, threeLength, threeMatch, fourMatch) = search(firstFour)
    return None


# dictionary = []
lengthDictionary = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
    10: [],
}


def search(firstFour):
    oneLength = []
    for word in lengthDictionary[1]:
        if word == firstFour[:1]:
            oneLength.append(word)
    twoLength = []
    for word in lengthDictionary[2]:
        if word == firstFour[:2]:
            twoLength.append(word)
    threeLength = []
    for word in lengthDictionary[3]:
        if word == firstFour[:3]:
            threeLength.append(word)
    threeMatch = {}
    fourMatch = {}
    for length in range(4, 11):
        threeMatch[length] = []
        fourMatch[length] = []
        for word in lengthDictionary[length]:
            matchCount = 0
            for i in range(4):
                if word[i] == firstFour[i]:
                    matchCount += 1
            if matchCount > 2:
                if matchCount == 3:
                    threeMatch[length].append(word)
                else:
                    fourMatch[length].append(word)
    return (oneLength, twoLength, threeLength, threeMatch, fourMatch)


if __name__ == "__main__":
    wordCount = int(input())
    for _ in range(wordCount):
        word = input()
        # dictionary.append(word)
        lengthDictionary[len(word)].append(word)
    testCount = int(input())
    caseResults = ""
    for i in range(testCount):
        caseResults += "Case #" + str(i+1) + ": " + str(solve(input())) + "\n"
    print(caseResults)
