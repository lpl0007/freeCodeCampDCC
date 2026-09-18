def is_balanced(s):
    s = s.lower()
    first = s[:int(len(s)/2)]
    if len(s) % 2 == 1:
        second = s[int((len(s)/2)) + 1:]
    else:
        second = s[(int(len(s)/2)):]
    vowel = ["a","e","i","o","u"]
    a, b = 0, 0
    for i in vowel:
        a += first.count(i)
        b += second.count(i)
    if a == b:
        return True
    else:
        return False
