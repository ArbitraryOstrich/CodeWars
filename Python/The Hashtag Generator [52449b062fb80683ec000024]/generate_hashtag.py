def generate_hashtag(s):
    b = "#" + "".join([b.capitalize() for b in s.split()])
    if len(b) > 140 or len(b) == 1:
        return False
    return b
