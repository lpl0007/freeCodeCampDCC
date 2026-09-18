def sortedStringToWord(string):
    word = []
    for i in string:
        word.append(i)
    word.sort()
    return word

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    str1 = sortedStringToWord(str1)
    str2 = sortedStringToWord(str2)
    if str1 == str2:
        return True
    else:
        return False
