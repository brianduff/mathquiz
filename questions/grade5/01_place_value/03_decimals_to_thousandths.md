# Decimals to Thousandths

0.0%`randint(1,9)`% is 10 times as great as what decimal?

0.00%`randint(1, 9)`% is $\frac{1}{10}$ of what decimal?

0.%`randint(1, 9)`% is 10 times as great as what decimal?

0.0%`randint(1, 9)`% is $\frac{1}{10}$ of what decimal?

## Write each decimal as a fraction

[question]: <> (config.count = 8)

%`random_decimal(0, randint(1, 3))`%

## Write each fraction as a decimal

[question]: <> (config.count = 8)
[question]: <> (power = randint(1, 3))
[question]: <> (`denominator = 10 ** power`)
[question]: <> (nominator = randint(2, denominator - 1))

$\frac{%`nominator`%}{%`denominator`%}$

## Problem solving

%`name_male()`% is beginning a science experiment in the lab. The instructions call for %`n=random_decimal(0, 3)`% kilogram of potassium. Write %`n`% as a fraction.

Mt. McKinley is the highest mountain peak in North America with an elevation of 20,320 feet. What is the value of the digit 3 in 20,320?

[question]: <> (number=randint(10, 99))

%`name_male()`% said that 0.0%`number`% can be written as $\frac{%`number`%}{100}$. Is he correct? Explain.

[question]: <> (data=dataset_row("continent_area"))

The area of the continent of %`data[0]`% is %`data[1]`% square miles. Write %`data[1]`% in expanded form using exponents to show powers of 10.

[question]: <> (n=randint(2, 9))

Write the fractions $\frac{%`n`%}{10}$, $\frac{%`n`%}{100}$, and $\frac{%`n`%}{1000}$ as decimals. How are these decimals related?

[question]: <> (total=randint(30, 60))
[question]: <> (first_month=(total // 3) + randint(0, 4))
[question]: <> (second_month=(total // 3) - randint(0, 9))

In three months, %`name_male()`% watched a total of %`total`% movies. If he watched %`first_month`% movies in June and %`second_month`% movies in July, how many movies did he watch in August? Write an equation using the variable $a$ to model your work.
