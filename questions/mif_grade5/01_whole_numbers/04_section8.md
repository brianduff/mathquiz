# Section 8 Quiz

## Solve these problems

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
