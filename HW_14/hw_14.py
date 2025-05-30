def spin_words(sentence):
    # Your code goes here
    words = [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    return " ".join(words)

print(spin_words("Following to my dream"))


def neutralise(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("I can't compare these two strings")
    new_s = " ".join("+" if a == b == "+"
                     else "-" if a == b == "-"
                    else "0"
                    for a,b in zip(s1, s2)
                    )
    return new_s

print(neutralise("++-", "+++"))
assert(neutralise("+-+-+-+-", "+-+-----"))
assert(neutralise("---", "--"))