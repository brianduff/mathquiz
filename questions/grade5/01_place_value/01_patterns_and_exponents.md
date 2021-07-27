# Patterns with Exponents and Powers of 10

Write $10%%repeat(randint(2, 10), r" \times 10")%%$ with an exponent.

Write $%`randint(2, 9)`%%%repeat(randint(2, 10), r" \times 10")%%$ with an exponent.

How many zeros are in the standard form of $10^{%%randint(12)%%}$? Write this number in standard form.

## In the following questions, find each product.

[question]: <> (config.count = 5)

$%%randint(9)%% \times 10^%%randint(9)%%$

[question]: <> (config.count = 1)

$%%randint(9)%% \times %%randpow(10, 6)%%$

[question]: <> (config.count = 2)

$%%randpow(10, 6)%% \times %%randint(9)%%$

## Problem solving

%`name_female()`% saw $%%randint(5)%% \times 10^1$ dogs in the park on Saturday. She saw %`multiquant(randint(5))`% dogs on Sunday as she saw on Saturday. How many dogs did she see over the two days?

%`name_female()`% buys %`a=randint(5, 20)`% pounds of %`fruit()`%. Each pound costs $%`b=randint(5)`%. If she gives the cashier %`intname(round_next_multiple(a*b, 20) // 20)`% $20 dollar bills, how much change should she receive?

%`a=name_male()`% practiced %`skill()`% for %`randint(15, 60)`% minutes. %`b=name_female()`% practiced for %`randint(2, 4)`% times as long as %`a`%. How many minutes did %`b`% practice? How many minutes in all did %`a`% and %`b`% practice? Write an equation to model your work.

## Practice

### Choose all equations that are true.

[section]: <> (config.randomorder = True)
[section]: <> (c=randint(3, 7))
[section]: <> (question="10" + repeat(c-1, r" \times 10"))

[ ] $%%question%% = %%10 ** c%%$
[ ] $%%question%% = %%10 * c%%$
[ ] $%%question%% = %%(10 * c)*(10** (c-2))%%$
[ ] $%%question%% = 10^%%c%%$
[ ] $%%question%% = %%(10 * c)*(10 ** (c-1))%%$

### Choose all equations that are true.

[section]: <> (config.randomorder = True)
[section]: <> (c=randint(2, 9))
[section]: <> (p=randint(3, 7))
[section]: <> (`answer=c * (10**p)`)

[ ] $%%answer%% = %%c%% \times %%10**(p-1)%%$
[ ] $%%answer%% = %%c%% \times %%10**p%%$
[ ] $%%answer%% = %%c%% \times 10^%%p-1%%$
[ ] $%%answer%% = %%c%% \times 10^%%p%%$
[ ] $%%answer%% = %%c%% \times 10^%%p+1%%$
