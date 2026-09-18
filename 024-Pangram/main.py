def is_pangram(sentence, letters):
    sentence = sentence.lower()
    sentence = sentence.replace(" ","")
    sentence = sentence.replace("!","")
    sentence = sentence.replace(".","")
    sentence = sentence.replace(",","")
    sentence = sentence.replace("?","")
    for i in sentence:
        if letters.find(i) == -1:
            return False
    for i in letters:
        if sentence.find(i) == -1:
            return False
    return True
