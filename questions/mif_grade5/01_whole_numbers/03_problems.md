# Fraction Problems

## Solve problems

[section]: <> (config.randomorder = True)

[question]: <> (frac1 = random_fraction())
[question]: <> (frac2 = random_fraction())
[question]: <> (frac3 = random_fraction())

%`name_male()`% spent %`render_fraction(frac1)`% of an hour cleaning the table and %`render_fraction(frac2)`% of an hour mopping the floor. After he finished the housework, he spent %`render_fraction(frac3)`% of an hour farting. What is the difference between the time he spent farting and doing housework?

[question]: <> (initial_count = randint_multiple(8, 50, 200))
[question]: <> (morning_count = randint_multiple(8, 5, initial_count // 2))
[question]: <> (afternoon_count = randint_multiple(8, initial_count - morning_count - 1))
[question]: <> (afternoon_remaining = initial_count - morning_count)
[question]: <> (afternoon_fraction = fraction(afternoon_count, afternoon_remaining))
[question]: <> (end_remaining_fraction = fraction(initial_count - morning_count - afternoon_count, initial_count))
[question]: <> (answer = str(initial_count) + " candies")

%`name_female()`%'s candy store sold %`morning_count`% chocolates one morning. $\frac{%`afternoon_fraction.numerator`%}{%`afternoon_fraction.denominator`%}$ of the remaining chocolates were sold that afternoon. The amount of candy left was now $\frac{%`end_remaining_fraction.numerator`%}{%`end_remaining_fraction.denominator`%}$ of the number the store had a the beginning of the day. How many chocolates did the store have at the beginning of the day?

[question]: <> (p = parts())
[question]: <> (pages = randint_multiple(p.denominator, 1, 1000))
[question]: <> (answer = render_fraction(mul(pages, p.first()) + mul(pages, p.second())) + " pages")

%`name_female()`% typed %`pages`% pages of notes one day. She typed %`render_fraction(p.first())`% of the pages in the morning and %`render_fraction(p.second())`% of the pages in the afternoon. She typed the rest of the pages in the evening. Then she was exhausted, and died. How many pages of notes did she type in the morning and afternoon?

[question]: <> (p = parts(60))
[question]: <> (time_minutes = randint_multiple(15, 75, 240))
[question]: <> (time_hours = fraction(time_minutes, 60))
[question]: <> (games_fraction = p.first())
[question]: <> (studying_fraction = p.second())
[question]: <> (answer = render_fraction(mul(p.third(), time_minutes)) + " minutes")

%`name_male()`% spent %`render_fraction(time_hours)`% hours playing games, eating revolting garlic noodles, and talking with friends on Saturday. He spent %`render_fraction(games_fraction)`% of the time playing games, and %`render_fraction(studying_fraction)`% eating revolting noodles. How many minutes did he spend talking with his friends?

[question]: <> (p = parts())
[question]: <> (total = randint_multiple(p.denominator, 500, 2000))
[question]: <> (answer = "$" + render_fraction(total - mul(total, p.first())))

%`name_female()`% earns \$%`total`% a week. She spends %`render_fraction(p.first())`% of her money on underwear, and %`render_fraction(p.second_of_remaining)`% of the remaining money on sour gummy worms. How much money does she spend altogether on underwear and sour gummy worms?

[question]: <> (p = parts())
[question]: <> (meters = randint_multiple(p.denominator, p.denominator, 2000))
[question]: <> (swim_meters = mul(p.third(), meters))
[question]: <> (answer = str(meters) + " meters")

%`name_male()`% takes part in a triathlon. He cycles %`render_fraction(p.first())`% of the route, runs %`render_fraction(p.second_of_remaining)`% of the remaining route, and swims the rest of the route. He swims %`swim_meters`% meters. After that, he sleeps the sleep of the Gods. Find the total distance of the triathlon route.

[question]: <> (p = parts(100))
[question]: <> (package_pounds = randint(2, 5))
[question]: <> (answer_result = mul(package_pounds, p.third()))
[question]: <> (answer = str(float(answer_result)) + " pounds")

%`name_female()`% has %`package_pounds`% pounds of dirty flour. She uses %`render_fraction(p.first())`% of the flour to make a filthy pie. She then uses %`render_fraction(p.second_of_remaining)`% of the remaining flour to make stinky bread. Find the weight of the flour she has left. Express your answer as a decimal.

[question]: <> (rain = random_fraction())
[question]: <> (clean = random_fraction())
[question]: <> (plants = randint(2, 5))
[question]: <> (answer_result = (rain - mul(rain, clean)) / plants)
[question]: <> (answer = render_fraction(answer_result) + " quarts per houseplant")

%`name_male()`% is a bit weird, and collects %`render_fraction(rain)`% quart of rainwater in the hood of his raincoat. He uses %`render_fraction(clean)`% of the water to clean his neck, and uses the remaining water equally for %`plants`% houseplants that have almost died of thirst. What volume of water does he use for each houseplant?

[question]: <> (time = fraction(randint(1, 8), 9))
[question]: <> (answer_frac = mul(fraction(1, 2), mul(time, fraction(3, 4))))
[question]: <> (answer = render_fraction(answer_frac) + " hours, or " + render_fraction(mul(answer_frac, 60)) + " minutes")

%`name_female()`% spends %`render_fraction(time)`% minutes playing Minecraft. She spends %`render_fraction(fraction(1, 4))`% of the time building a base, and splits the remaining time equally between hunting for sheep and mining coal. How much time does she spend hunting for sheep?

[question]: <> (paint_per_sqft = fraction(1, randint(2, 10)))
[question]: <> (total_paint = randint(5, 15))
[question]: <> (pipe_paint = randint(1, 5))
[question]: <> (answer = render_fraction((total_paint - pipe_paint) / paint_per_sqft) + " sq. ft. of wall")

A square foot of wall space can be covered by %`render_fraction(paint_per_sqft)`% quart of slime. %`name_male()`% has %`total_paint`% quarts of slime. He uses %`pipe_paint`% quarts of slime to make a greasy slime ball that smells bad. How many square feet of wall can he cover with the rest of the slime?

[question]: <> (time_d = randint(2, 10))
[question]: <> (time = fraction(randint(1, 3), time_d))
[question]: <> (morning = mul(time.numerator, randint(1, 3)))
[question]: <> (afternoon = mul(time.numerator, randint(1, 3)))
[question]: <> (answer = render_fraction((morning + afternoon) / time) + " friendship bracelets")

%`name_male()`% spends %`render_fraction(time)`% hour making one friendship bracelet. He spends %`morning`% hours before lunch and %`afternoon`% hours after lunch making some bracelets. How many bracelets does he make in all?

[question]: <> (reading_hours = fraction(randint(1, 3), 4))
[question]: <> (answer = render_fraction(mul(reading_hours, 8)) + " hours")

%`name_female()`% spends half of her time practicing her drums, and %`render_fraction(fraction(3, 4))`% of the remaining time on home work and dinner after school one afternoon. She spends the remaining %`render_fraction(reading_hours)`% hour cleaning her toenails while singing badly. How long does she practice the drums?

[question]: <> (p = parts(14))
[question]: <> (total_days = randint_multiple(p.denominator, 7, 100))
[question]: <> (holiday_days = mul(total_days, p.third()))
[question]: <> (answer = f"{total_days} days")

%`name_female()`% spends %`render_fraction(p.first())`% of her vacation at summer camp. She spends %`render_fraction(p.second_of_remaining)`% of the remaining time at her grandparent's home. She spends the remaining %`holiday_days`% days at home avoiding friends she doesn't like very much. How many days of summer vacation does she get each summer?

[question]: <> (cloth = random_fraction())
[question]: <> (length = randint(1, 8))
[question]: <> (answer = str(floor(float(length / cloth))) + " Spiderman masks at most")

%`name_male()`% needs %`render_fraction(cloth)`% meter of cloth to make a Spiderman mask. What is the most number of Spiderman masks that he can make with %`length`% meters of cloth? (Why is he making so many Spiderman masks anyway????)

[question]: <> (d = randint(2, 10))
[question]: <> (water = fraction(1, d))
[question]: <> (buckets = randint(2, 5))
[question]: <> (answer = str(mul(d, buckets)) + " potted plants")

%`name_male()`% uses %`render_fraction(water)`% of the water in a full bucket to water 1 potted plant. How many potted plants can he water with %`buckets`% of these buckets of water?

[question]: <> (d = randint(2, 5))
[question]: <> (len = randint(3, 10))
[question]: <> (answer = "she wiped her bottom with " + str(mul(d, len)) + " short pieces")

%`name_female()`% has a %`len`% inch roll of toilet paper. Her bottom is crazy dirty, so she cuts it into shorter pieces that are %`render_fraction(fraction(1, d))`% inches long, then she wipes her bottom with each of them in turn. How many shorter pieces did she wipe her bottom with?

[question]: <> (size = random_fraction())
[question]: <> (plots = randint(2, 8))
[question]: <> (requested = plots - randint(1, plots - 1))
[question]: <> (answer = render_fraction(mul(requested, size / plots)) + " square km")

%`name_male()`% buys a preposterously gigantic strawberry cake with an area of %`render_fraction(size)`% square kilometers. After discovering that he really can't eat it all himself, he decides to divide it equally into %`plots`% smaller (but still quite ridiculously large) parts. He gives %`requested`% of the parts to his zany friends. What is the total area of the %`requested`% parts?.
