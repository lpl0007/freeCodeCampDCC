def jbelmu(text):
    text = text.split(" ")
    jumble = ""
    word = []
    for i in text:
        count = 0
        temp = ""
        for j in i:
            if count == 0:
                jumble += j
            elif count == len(i) - 1:
                temp = j
            else:
                word.append(j)
            count += 1
        count = 0
        word.sort()
        for j in word:
            jumble += j
        word.clear()
        jumble += temp + " "
    return jumble[:len(jumble)-1]
