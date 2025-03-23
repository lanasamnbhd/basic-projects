import random
when=["2 years ago","1 month ago","yesterday", "today","tomorrow","in a few years"]
who=["Karen","Lana","Brus","my parents","they"]
location=["England","America","Azerbaijan","Germany","Italy","Korea"]
went=["cinema","university","party","school","holiday","date"]
happened=["made a lot of friends","ate a burger","found a secret key","will solve a mistery","writes a book"]
print(random.choice(when)+','+random.choice(who)+'that lived in'+random.choice(location)+'went to the'+random.choice(went)+'and'+random.choice(happened))
