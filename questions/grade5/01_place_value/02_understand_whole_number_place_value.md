# Whole Number Place Value

Write %`random_digits("rr00r0")`% in expanded form with exponents.

Write the number name for %`random_digits("rr0r0r00")`%.

## Write the values of the given digits

[question]: <> (config.count = 3)
[question]: <> (digits = randint(5, 7))
[question]: <> (target = randint(0, 9))
[question]: <> (rn = n_random_digits(digits, target))
[question]: <> (dtc = randint(2, digits-2))
[question]: <> (n = change_digits(rn, dtc, target))

The %`target`%s in %`n`%

## Solve

[question]: <> (config.count = 1)

Write %`change_digits(n_random_digits(8, 0), randint(5), 0)`% in expanded form.

Write %`change_digits(n_random_digits(6, 0), randint(3), 0)`% in expanded form using exponents.

What is the number name for %`n_random_digits(7, 0)`%? What is the value of the %`ordinal_name(randint(1, 6))`% digit?

## Problem Solving

%`f=name_female()`% and %`m=name_male()`% chose numbers for a place-value game. %`f`% chose the number %`intname(random_digits("rrr000"))`%. %`m`% chose %`intname(random_digits("r000000"))`% for his number. Who chose the greater number? Explain.

One day, total attendance at the %`event()`% was %`a = n_random_digits(6)`%. Round %`a`% to the nearest hundred thousand, nearest ten thousand and nearest thousand. Which of these rounded amounts is closest to the actual attendance?

%`name_female()`% and her family went on a %`randint(5, 12)`% day vacation. She read %`randint(2, 12)`% pages of her book each day. How many total pages did she read while on vacation?

## Practice

[question]: <> (digits=randint(4,8))
[question]: <> (number=repeat(digits, str(randint(1, 9))))

%`m=name_male()`% says that in the number %`number`%, all the digits have the same value. Is %`m`% correct? Describe the relationship between the values of digits in the number.
