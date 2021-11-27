# Chapter 2 Practice Quiz

## Write the following fractions as division expressions.

[question]: <> (config.count = 2)
[question]: <> (nominator = randint(1, 25))
[question]: <> (denominator = nominator + randint(1, 10))

$\frac{%`nominator`%}{%`denominator`%}$

## Write the following division expressions as fractions.

[question]: <> (config.count = 2)
[question]: <> (nominator = randint(1, 25))
[question]: <> (denominator = nominator + randint(1, 10))

$%`nominator`% \div %`denominator`%$

## Write the following division expressions as fractions, then solve.

[question]: <> (config.count = 2)
[question]: <> (denominator = randint(2, 25))
[question]: <> (nominator = denominator + randint(1, 10))

$%`nominator`% \div %`denominator`%$

## Add or subtract

[question]: <> (config.count = 2)
[question]: <> (denominator1 = randint(2, 10))
[question]: <> (nominator1 = randint(1, denominator1 - 1))
[question]: <> (denominator2 = randint(2, 10))
[question]: <> (nominator2 = randint(1, denominator2 - 1))

$\frac{%`nominator1`%}{%`denominator1`%} + \frac{%`nominator2`%}{%`denominator2`%}$

[question]: <> (config.count = 2)
[question]: <> (denominator1 = randint(2, 10))
[question]: <> (nominator1 = randint(1, denominator1 - 1))
[question]: <> (val1 = nominator1 / denominator1)
[question]: <> (denominator2 = randint(2, 10))
[question]: <> (nominator2 = randint(1, denominator2 - 1))
[question]: <> (val2 = nominator2 / denominator2)
[question]: <> (nom1 = nominator1 if val1 > val2 else nominator2)
[question]: <> (denom1 = denominator1 if val1 > val2 else denominator2)
[question]: <> (nom2 = nominator1 if val1 < val2 else nominator2)
[question]: <> (denom2 = denominator1 if val1 < val2 else denominator2)

$\frac{%`nom1`%}{%`denom1`%} - \frac{%`nom2`%}{%`denom2`%}$

## Estimate the answer using benchmarks

[question]: <> (config.count = 2)
[question]: <> (denominator1 = randint(2, 10))
[question]: <> (nominator1 = randint(1, denominator1 - 1))
[question]: <> (denominator2 = randint(2, 10))
[question]: <> (nominator2 = randint(1, denominator2 - 1))

$\frac{%`nominator1`%}{%`denominator1`%} + \frac{%`nominator2`%}{%`denominator2`%}$

[question]: <> (config.count = 2)
[question]: <> (denominator1 = randint(2, 10))
[question]: <> (nominator1 = randint(1, denominator1 - 1))
[question]: <> (val1 = nominator1 / denominator1)
[question]: <> (denominator2 = randint(2, 10))
[question]: <> (nominator2 = randint(1, denominator2 - 1))
[question]: <> (val2 = nominator2 / denominator2)
[question]: <> (nom1 = nominator1 if val1 > val2 else nominator2)
[question]: <> (denom1 = denominator1 if val1 > val2 else denominator2)
[question]: <> (nom2 = nominator1 if val1 < val2 else nominator2)
[question]: <> (denom2 = denominator1 if val1 < val2 else denominator2)

$\frac{%`nom1`%}{%`denom1`%} - \frac{%`nom2`%}{%`denom2`%}$

## Add

[question]: <> (config.count = 2)
[question]: <> (denominator = randint(2, 10))
[question]: <> (nominator = randint(1, denominator - 1))
[question]: <> (denominator2 = randint(2, 10))
[question]: <> (nominator2 = randint(1, denominator2 - 1))

$%`randint(2, 10)`%\frac{%`nominator2`%}{%`denominator2`%} + %`randint(2, 10)`% \frac{%`nominator`%}{%`denominator`%}$

## Solve problems

[question]: <> (frac1 = random_proper_fraction())
[question]: <> (frac2 = random_proper_fraction())
[question]: <> (frac3 = random_proper_fraction())

%`name_male()`% spent $\frac{%`frac1[0]`%}{%`frac1[1]`%}$ of an hour cleaning the table and $\frac{%`frac2[0]`%}{%`frac2[1]`%}$ of an hour mopping the floor. After he finished the housework, he spent $\frac{%`frac3[0]`%}{%`frac3[1]`%}$ of an hour watching TV. What is the difference between the time he spent watching TV and doing housework?

[question]: <> (initial_count = randint_multiple(8, 50, 200))
[question]: <> (morning_count = randint_multiple(8, 5, initial_count // 2))
[question]: <> (afternoon_count = randint_multiple(8, initial_count - morning_count - 1))
[question]: <> (afternoon_remaining = initial_count - morning_count)
[question]: <> (afternoon_fraction = fraction(afternoon_count, afternoon_remaining))
[question]: <> (end_remaining_fraction = fraction(initial_count - morning_count - afternoon_count, initial_count))

%`name_female()`%'s candy store sold %`morning_count`% chocolates one morning. $\frac{%`afternoon_fraction.numerator`%}{%`afternoon_fraction.denominator`%}$ of the remaining chocolates were sold that afternoon. The amount of candy left was now $\frac{%`end_remaining_fraction.numerator`%}{%`end_remaining_fraction.denominator`%}$ of the number the store had a the beginning of the day. How many chocolates did the store have at the beginning of the day?

[question]: <> (pages = randint_multiple(4, 20, 100))
[question]: <> (morning_numerator = randint(1, 8))
[question]: <> (afternoon_numerator = randint(1, 4))
[question]: <> (morning_fraction = fraction(morning_numerator, 16))
[question]: <> (afternoon_fraction = fraction(afternoon_numerator, 16))

%`name_female()`% typed %`pages`% pages of notes one day. She typed $\frac{%`morning_fraction.numerator`%}{%`morning_fraction.denominator`%}$ of the pages in the morning and $\frac{%`afternoon_fraction.numerator`%}{%`afternoon_fraction.denominator`%}$ of the pages in the afternoon. She typed the rest of the pages in the evening. How many pages of notes did she type in the morning and afternoon?

[question]: <> (time_hours = randint_multiple(2, 4, 10))
[question]: <> (games_numerator = randint(1, 8))
[question]: <> (studying_numerator = randint(1, 4))
[question]: <> (games_fraction = fraction(morning_numerator, 16))
[question]: <> (studying_fraction = fraction(afternoon_numerator, 16))

%`name_male()`% spent %`time_hours`% hours playing games, stidying, and talking with friends on Saturday. He spent %`render_fraction(games_fraction)`% of the time playing games, and %`render_fraction(studying_fraction)`% studying. How many minutes did he spend talking with his friends?

[question]: <> (p = parts())
[question]: <> (total = randint_multiple(p.denominator, 500, 2000))

%`name_female()`% earns \$%`total`% a week. She spends %`render_fraction(p.first())`% of her money on groceries, and %`render_fraction(p.second_of_remaining)`% of the remaining money on clothes. How much money does she spend altogether on groceries and clothes?......

[question]: <> (p = parts())
[question]: <> (meters = randint_multiple(p.denominator, p.denominator, 2000))
[question]: <> (swim_meters = mul(p.third(), meters))

%`name_male()`% takes part in a triathlon. He cyles %`render_fraction(p.first())`% of the route, runs %`render_fraction(p.second_of_remaining)`% of the remaining route, and swims the rest of the route. He swims %`swim_meters`% meters. Find the total distance of the triathlon route.

[question]: <> (p = parts(100))
[question]: <> (package_pounds = randint(2, 5))

%`name_female()`% has %`package_pounds`% pounds of flour. She uses %`render_fraction(p.first())`% of the flour to make a pie. She then uses %`render_fraction(p.second_of_remaining)`% of the remaining flour to make bread. Find the weight of the flour she has left. Express your answer as a decimal.

[question]: <> (rain = random_fraction())
[question]: <> (clean = random_fraction())
[question]: <> (plants = randint(2, 5))

%`name_male()`% collects %`render_fraction(rain)`% quart of rainwater. He uses %`render_fraction(clean)`% of the water to clean his bike, and uses the remaining water equally for %`plants`% houseplants. What volume of water does he use for each houseplant?

[question]: <> (hour_frac = randint_multiple(2, 2, 10))
[question]: <> (time = fraction(hour_frac, hour_frac + 1))

%`name_female()`% spends %`render_fraction(time)`% hour playing Minecraft. She spends %`render_fraction(fraction(1, 4))`% of the time building a base, and splits the remaining time equally between hunting for sheep and mining coal. How much time does she spend hunting for sheep?

[question]: <> (paint_per_sqft = fraction(1, randint(2, 10)))
[question]: <> (total_paint = randint(5, 15))
[question]: <> (pipe_paint = randint(1, 5))

A square foot of wall space needs %`render_fraction(paint_per_sqft)`% quart of paint. %`name_male()`% has %`total_paint`% quarts of paint. He uses %`pipe_paint`% quarts to paint a pipe. How many square feet of wall can he paint with the rest?

%`name_male()`% spends %`render_fraction(random_fraction())`% hour making one friendship bracelet. He spends %`randint(2, 5)`% hours before lunch and %`randint(2, 6)`% hours after lunch making some bracelets. How many bracelets does he make in all?

%`name_female()`% spends half of her time practicing her drums, and %`render_fraction(fraction(3, 4))`% of the remaining time on home work and dinner after school one afternoon. She spends the remaining %`render_fraction(fraction(randint(1, 3), 4))`% hour reading. How long does she practice the drums?

[question]: <> (p = parts(14))
[question]: <> (total_days = randint_multiple(p.denominator, 7, 100))
[question]: <> (holiday_days = mul(total_days, p.third()))

%`name_female()`% spends %`render_fraction(p.first())`% of her vacation at summer camp. She spends %`render_fraction(p.second_of_remaining)`% of the remaining time at her grandparent's home. She spends the remaining %`holiday_days`% days holidaying with her family. How many days of summer vacation does she get each summer?
