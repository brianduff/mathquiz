# Understand Decimal Place Value

Draw a place value chart for the number %`random_decimal(1, 3)`%. Write its number name and tell the value of the %`ordinal_name(randint(2, 4))`% digit.

Write %`random_decimal(3, 3)`% in expanded form.

## Write each number in standard form

$\left( %`randint(2, 9)`% \times 1 \right) + \left( %`randint(2, 9)`% \times \frac{1}{100} \right) + \left( %`randint(2, 9)`% \times \frac{1}{%`commaize(1000)`%} \right)$

%`randint(1, 9)`% + %`random_decimal(0, 1)`% + 0.0%`randint(1, 9)`% + 0.00%`randint(1, 9)`%

%`intname(n_random_digits(3))`% and %`intname(n_random_digits(2))`% hundredths

## For each question, write two decimals that are equivalent to the given decimal

[question]: <> (config.count = 4)

%`random_decimal(randint(0, 1), 1)`%%`repeat(randint(0, 2), "0")`%

## Problem solving

%`name_male()`% has a piece of wood that measures $%`randint(2, 9)`% \times \frac{1}{10} + %`randint(2, 9)`% \times \frac{1}{100} + %`randint(2, 9)`% \times \frac{1}{1,000}$ meter. How can this measurement be written as a decimal?

[question]: <> (sections = randint(2, 12))
[question]: <> (per_section = randint(50, 100))

There are %`sections * per_section`% people in the movie theater. The same number of people are seated in each of the %`sections`% different sections of the theater. How many people are seated in each section?

[question]: <> (digit1 = randint(1, 9))
[question]: <> (digit2 = randint(1, 9))

%`name_female()`%'s softball batting average is 0.%`digit1`%%`digit2`%0, and %`b=name_female()`%'s is 0.%`digit1`%0%`digit2`%. %`b`% says they have the same average. What error did she make? Explain.

[question]: <> (names = ["Hamburger", "Salad", "Sandwich", "Pizza"])
[question]: <> (wholecost = randint(2, 6))
[question]: <> (costs = [0, 0, 0, 0])
[question]: <> (costs[0] = wholecost + (random_multiple(5, 19) / 100))
[question]: <> (costs[1] = wholecost + (random_multiple(5, 19) / 100))
[question]: <> (costs[2] = wholecost + (random_multiple(5, 19) / 100))
[question]: <> (costs[3] = wholecost + (random_multiple(5, 19) / 100))
[question]: <> (selected = rand_values(2, costs))

These items are on the menu: %`names[0]`% (%`currency(costs[0])`%), %`names[1]`% (%`currency(costs[1])`%), %`names[2]`% (%`currency(costs[2])`%), %`names[3]`% (%`currency(costs[3])`%). %`x=name_male()`% spent %`currency(selected[0] + selected[2])`%. Which two items did %`x`% buy?

%`name_male()`% drew a pentagon with each side measuring %`randint(2, 9)`% inches. %`name_female()`% drew a hexagon with each side measuring %`randint(2, 9)`% inches. Which shape has a greater perimeter? Write an equation to help explain your answer.

## Practice

Find two decimals that are equivalent to $\left(%`randint(2, 9)`% \times 100 \right) + \left(%`randint(2, 9)`% \times \frac{1}{10} \right) + \left( %`randint(2, 9)`% \times \frac{1}{100} \right)$

$$
 \begin{tabular}{r}
     5 \\
     + 12 \\
     \hline
     17
 \end{tabular}
$$
