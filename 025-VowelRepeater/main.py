def repeat_vowels(s):
    vowel = ["a","e","i","o","u"]
    vowelCount = 0
    word = ""
    for i in s:
        word += i
        for j in vowel:
            if i.lower() == j:
                for k in range(vowelCount):
                    word += j
                vowelCount += 1
    return word
