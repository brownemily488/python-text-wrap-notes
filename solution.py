import textwrap

def solve(value):
    return textwrap.wrap(value["text"], width=value["width"], break_long_words=False, break_on_hyphens=False)
