vide = "e"


def sardinasPatterson(langage: list):
    quotientList = []
    quotientList.insert(0, langage)
    quotientLangage = getLangageQuotient(langage, langage)
    quotientList.insert(1, dropVideElement(quotientLangage))
    currentQuotient = quotientList[1]
    n = 2
    while len(currentQuotient) > 0:
        currentQuotient = getQuotientFromSuite(quotientList[0], quotientList[n - 1])
        if isLangageContainsVide(currentQuotient):
            print(quotientList)
            return False
        if currentQuotient in quotientList:
            print(quotientList)
            return True
        quotientList.insert(n, currentQuotient)
        n = n + 1
    return True


def getQuotientFromSuite(l0: list, ln: list):
    leftQuotient = set(getLangageQuotient(l0, ln))
    rightQuotient = set(getLangageQuotient(ln, l0))
    return list(leftQuotient.union(rightQuotient))


def isLangageContainsVide(langage):
    if vide in langage:
        return True
    return False


def getLangageQuotient(langageForPrefix, langageForExtract):
    quotient = []
    for prefix in langageForPrefix:
        quotient.extend(getResiduelFromLangage(langageForExtract, prefix))
    # union sans doublon list(set(quotient))
    return list(set(quotient))


def getResiduelFromLangage(langage, prefix):
    residuelList = []
    for word in langage:
        residuel = getResiduelFromWord(word, prefix)
        residuelList.append(residuel) if residuel != None else None
    return residuelList


def getResiduelFromWord(word, prefix):
    wordLen = len(word)
    prefixLen = len(prefix)
    if wordLen >= prefixLen and word.find(prefix) == 0:
        if wordLen == prefixLen:
            return vide
        return word[prefixLen:]


def dropVideElement(langage):
    try:
        langage.remove(vide)
    except ValueError:
        pass
    return langage


# print("Residuel a  : ", getResiduelFromLangage(["a", "ba", "aab", "bba"], "a"))
# print("Residuel b : ", getResiduelFromLangage(["ab", "ba", "aab", "bba"], "b"))
# print(
#     "Quotient : ",
#     getLangageQuotient(["000", "010", "011", "01001"], ["000", "010", "011", "01001"]),
# )
print(" check  : ", sardinasPatterson(["00", "01", "010"]))
