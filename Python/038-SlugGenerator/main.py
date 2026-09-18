def generate_slug(string):
    slug = ""

    for char in string:
        if char.isalnum() or char == " ":
            if char == " ":
                if slug and not slug.endswith("%20"):
                    slug += "%20"
            else:
                slug += char.lower()

    if slug.endswith("%20"):
        slug = slug[:-3]

    return slug
