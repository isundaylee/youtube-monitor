def parse_integer(text):
    return int("".join(filter(lambda c: c != ",", text)))

