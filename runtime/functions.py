import random
from pathlib import Path
from fractions import Fraction
from math import floor


def concat(a, b):
    return str(a) + str(b)


def randint(x, y=None):
    if y is None:
        y = x
        x = 1
    return random.randint(x, y)


def randint_even(x, y=None):
    return randint_multiple(2, x, y)


def randint_multiple(m, x, y=None):
    r = randint(x, y)
    while r % m != 0:
        r = randint(x, y)
    return r


def repeat(n, expr):
    result = ""
    for _ in range(n):
        result += str(expr)
    return result


def randpow(n, i, a=None):
    return n ** randint(i, a)


def multquant(n):
    if n < 2:
        raise "Must be at least 2"
    if n == 2:
        return "twice as many"
    else:
        return n + " times as many"


def name(male=False):
    file = "male.txt" if male else "female.txt"
    return _random_line(file)


def name_female():
    return name(False)


def name_male():
    return name(True)


def weekday():
    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    return days[randint(0, len(days) - 1)]


def _random_line(file):
    f = Path("data") / file
    if not f.exists():
        f = Path(
            "bazel-out/host/bin/runtime/run_generator.runfiles/mathquiz/runtime/data") / file

    with open(f, 'r') as f:
        names = f.read().splitlines()

    return names[randint(0, len(names) - 1)]


def fruit():
    return _random_line("fruit.txt")


def event():
    return _random_line("event.txt")


def intname(i, commas=True):
    if i < 0:
        raise "Must be positive"

    special_names = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        80: "eighty",
    }

    special = special_names.get(i)
    if special:
        return special

    result = ""

    need_comma = False

    if i >= 1000000:
        result += intname(i // 1000000, False)
        result += " million" + (", " if commas else " ")
        i = i % 1000000

    if i >= 1000:
        result += intname(i // 1000, False)
        result += " thousand" + (", " if commas else " ")
        i = i % 1000

    if i >= 100:
        result += intname(i // 100, False)
        result += " hundred "
        i = i % 100

    special = special_names.get(i)
    if i == 0:
        if commas:
            result = result[0:-2]
    elif special:
        result += special
    else:
        # we have a number between 21 - 99 that's not already one of the special
        # numbers above.
        tens = i // 10
        if tens > 0:
            tens_name = special_names.get(tens * 10)
            if tens_name:
                result += tens_name
            else:
                result += intname(tens, False) + "ty"

        ones = i % 10
        if ones > 0:
            result += "-" + intname(ones, False)

    return result


def round_next_multiple(n, m):
    floor = n // m
    return (floor + 1) * m


def skill():
    return _random_line("skill.txt")


def multiquant(n):
    if n == 2:
        return "twice as many"
    else:
        return f"{intname(n)} times as many"


def n_random_digits(n, exclude=None):
    return random_digits(repeat(n, "r"), exclude)


def random_digits(template, exclude=None):
    first = True
    result = ""
    for c in template:
        if c == 'r':
            r = randint(0, 9)
            while r == exclude or (first and r == 0):
                r = randint(0, 9)
            result += str(r)
        else:
            result += c

        first = False

    return int(result)


def change_digits(n, count, new_digit):
    # Generate positions of changed digits.

    s = str(n)

    positions = []
    for i in range(len(s)):
        positions.append(i)

    random.shuffle(positions)

    changed = 0

    temp = list(s)

    while changed < count:
        next_pos = positions.pop()
        if next_pos == 0 and new_digit == 0:
            continue

        temp[next_pos] = str(new_digit)
        changed += 1

    s = "".join(temp)

    return int(s)


def ordinal_name(n):
    if n < 1:
        raise "Must be at least 1"

    special_names = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
        13: "thirteenth",
    }

    special = special_names.get(n)
    if special:
        return special

    number_name = intname(n)
    suffix = "th"
    if n % 10 == 1:
        suffix = "st"
    elif n % 10 == 2:
        suffix = "nd"
    elif n % 10 == 3:
        suffix = "rd"

    return number_name + suffix


def random_decimal(whole_places, fractional_places):
    before = ""
    after = ""

    first = True
    for _ in range(whole_places):
        d = randint(0, 9)
        while d == 0 and first:
            d = randint(0, 9)

        before += str(d)
        first = False

    for _ in range(fractional_places - 1):
        after += str(randint(0, 9))

    if fractional_places > 0:
        after += str(randint(1, 9))

    return float(before + "." + after)


def dataset_row(name):
    line = _random_line(name + ".txt")
    parts = line.split(",")
    return (parts[0], parts[1])


def commaize(n):
    s = str(n)[::-1]

    result = ""
    count = 0
    for c in s:
        result += c
        count += 1
        if count % 3 == 0:
            result += ','

    s = result[::-1]
    if len(s) > 0 and s[0] == ',':
        s = s[1:]

    return s


def random_multiple(n, max):
    return randint(1, max) * n


def currency(v):
    return "${:.2f}".format(v)


def rand_values(n, list):
    idx = []
    for i in range(len(list)):
        idx.append(i)

    random.shuffle(idx)

    result = []
    for i in idx:
        result.append(list[i])

    return result


def digit():
    return randint(1, 9)


def uniq_decimals(count, min, max, places=2):
    result = []

    while len(result) < count:
        whole = randint(min, max)
        frac = n_random_digits(places)

        n = float(str(whole) + "." + str(frac))
        if not n in result:
            result.append(n)

    return result


def unique_sequence(min, max):
    result = []

    for i in range(min, max+1):
        result.append(i)

    random.shuffle(result)

    return result


def random_proper_fraction():
    denominator = randint(2, 10)
    numerator = randint(1, denominator - 1)

    return [numerator, denominator]


def random_fraction():
    denominator = randint(2, 10)
    numerator = randint(1, denominator - 1)

    return Fraction(numerator, denominator)


def fraction(numerator, denominator):
    return Fraction(numerator, denominator)


def mul(a, b):
    return a * b


def render_fraction(fraction):
    if fraction.denominator == 1:
        return str(fraction.numerator)

    if fraction.numerator > fraction.denominator:
        whole_part = fraction.numerator // fraction.denominator
        fraction = Fraction(
            fraction.numerator - (whole_part * fraction.denominator), fraction.denominator)
        return str(whole_part) + " " + render_fraction(fraction)

    return "$\\frac{" + str(fraction.numerator) + "}{" + str(fraction.denominator) + "}$"


class Parts:
    def __init__(self, denominator=None):
        self.second_of_remaining = Fraction(1, 10000)
        self.iters = 0
        while self.second_of_remaining.denominator > 12:
            self.denominator = denominator or randint(50, 500)
            self.first_part = randint(1, (3 * self.denominator) // 4)
            self.second_part = self.denominator - randint(
                self.first_part + 1, self.denominator - 1)
            self.second_of_remaining = (
                Fraction(1, 1) - self.first()) * self.second()
            self.iters += 1

    def first(self):
        return fraction(self.first_part, self.denominator)

    def second(self):
        return fraction(self.second_part, self.denominator)

    def third(self):
        return fraction(self.denominator - self.first_part - self.second_part, self.denominator)


def parts(denominator=None):
    return Parts(denominator)
