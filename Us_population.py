# Populatioinprojection of united state

# building a year period by second
dayPerSecond = 24*3600
yearPerSecond = dayPerSecond * 365

# computing birth rate per year(1 birth each 7 second)
birthPerYear = yearPerSecond // 7

# computing death rate per year(1 death each 13 second)
deathPerYear = yearPerSecond // 13

# computing emigration per year(1 emigration each 45 second)
emigrationPerYear = yearPerSecond // 45

# compute the total increase per year
increase = birthPerYear + emigrationPerYear
totalIncrease = increase - deathPerYear

current_population = 312032486

# computing each of next five years population
first_year = current_population + totalIncrease
second_year = first_year + totalIncrease
third_year = second_year + totalIncrease 
fourth_year = third_year + totalIncrease
fifth_year = fourth_year + totalIncrease

# printing the result 
print("-----------------------------Each next five years population-----------------------------------------")
print("current\t\t\t first year\tsecond year\tthird year\tfourth year\t fifth year")
print(f"{current_population:,}\t\t{first_year:,}\t{second_year:,}\t{third_year:,}\t{fourth_year:,}\t{fifth_year:,}")