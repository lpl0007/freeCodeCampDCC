def get_words(paragraph):
    word_counts = {}

    paragraph = paragraph.lower()
    paragraph = paragraph.replace(",", "")
    paragraph = paragraph.replace(".", "")
    paragraph = paragraph.replace("!", "")

    words = paragraph.split()

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)

    return sorted_words[:3]
