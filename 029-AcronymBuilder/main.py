def build_acronym(s):
    words = s.split()
    acronym = ""

    ignore_words = ["a", "for", "an", "and", "by", "of"]

    for i in range(len(words)):
        word = words[i].lower()

        if i == 0 or word not in ignore_words:
            acronym += words[i][0].upper()
    return acronym
