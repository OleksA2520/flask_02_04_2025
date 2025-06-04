#######################Task 1
"""Given an array of Player objects and a position (first position is 1), return the name of the chosen Player.
name is a property of Player objects, e.g Player.name"""

def duck_duck_goose(players, goose):
    index = (goose - 1) % len(players)
    return players[index].name

# В перший раз вирішила по іншом:
"""import random
from faker import Faker

def generate_players():
    fake=Faker()
    count = random.randint(6, 10)
    return [fake.first_name() for _ in range(count)]
players = generate_players()
print(players)

players_name=random.choice(players)
print(players_name)"""


####################Task 2
"""Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
often referred to as Pascal case). The next words should be always capitalized."""

import re

def with_camel_case(text):
    if not text:
        return text

    parts = re.split('[-_]', text)

    first = parts[0]
    rest = [word.capitalize() for word in parts[1:]]

    return first + ''.join(rest)

print(with_camel_case("Hello_my-friend"))
print(with_camel_case("it-is-impossible!"))