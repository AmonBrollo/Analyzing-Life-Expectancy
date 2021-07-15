# File: Analyzing Life Expectancy.py
# Solve real-world problems with programming building blocks.
# Author: Amon Brollo
 
max_life_expectancy = 0
min_life_expectancy = 100
max_entity = ""
min_entity = ""
max_year = ""
min_year = ""
life_len = 0
life_sum = 0
life_average = 0
year_of_interest_life_ex = 0.0
max_life_in_year = 0
min_life_in_year = 100
country_of_interest_life_sum = 0
country_of_interest_life_len = 0
country_of_interest_max_life = 0
country_of_interest_min_life = 100
country_of_interest_min_year = 0
country_of_interest_min_year = 10000

with open("life_expectancy.csv") as f:
    next(f)
    year_of_interest = int(input("Enter a year of interest: "))

    for line in f:
        line = line.strip()
        line = line.split(",")

        entity = line[0]
        year = int(line[2])
        life_ex = float(line[3])

        if life_ex > max_life_expectancy:
            max_life_expectancy = life_ex
            max_entity = entity
            max_year = year

        if life_ex < min_life_expectancy:
            min_life_expectancy = life_ex
            min_entity = entity
            min_year = year
        
        if year_of_interest == year:
            year_of_interest_life_ex = life_ex
            year_of_interest_entity = entity
            
            for i in year_of_interest_entity:
                life_sum = life_sum + 1
                life_len = life_len + life_ex
                
            if max_life_in_year < life_ex:
                max_life_in_year = life_ex
                max_life_entity = entity

            if min_life_in_year > life_ex:
                min_life_in_year = life_ex
                min_life_entity = entity

    life_average = life_len / life_sum

    print(f"The overall max life expectancy is: {max_life_expectancy} from {max_entity} in {max_year}")
    print(f"The overall min life expectancy is: {min_life_expectancy} from {min_entity} in {min_year}\n")
    print(f"For the year {year_of_interest}")
    print(f"The average life expectancy across all countries was {life_average:.2f}")
    print(f"The max life expectancy was in {max_life_entity} with {max_life_in_year}")
    print(f"The min life expectancy was in {min_life_entity} with {min_life_in_year}")

# This part allows the user to type in a country, then show the minimum, maximum, 
# and average life expectancy for that country.
with open("life_expectancy.csv") as f:
    next(f)
    country_of_interest = input("\nWhich country would you like to ivestigate? ")
    for line in f:
        line = line.strip()
        line = line.split(",")

        entity = line[0]
        code = line[1]
        year = int(line[2])
        life_ex = float(line[3])

        if country_of_interest == entity:

            if life_ex > country_of_interest_max_life:
                country_of_interest_max_life = life_ex
                country_of_interest_max_year = year

            if life_ex < country_of_interest_min_life:
                country_of_interest_min_life = life_ex
                country_of_interest_min_year = year

            for i in line[1]:
                country_of_interest_life_sum = country_of_interest_life_sum + 1
                country_of_interest_life_len = country_of_interest_life_len + life_ex

country_of_interest_life_average = country_of_interest_life_len / country_of_interest_life_sum
print(f"The average life expectancy  was {country_of_interest_life_average:.2f}")
print(f"The max life expectancy in {country_of_interest} was {country_of_interest_max_life:.2f} in {country_of_interest_max_year}")
print(f"The min life expectancy in was {country_of_interest_min_life:.2f} in {country_of_interest_min_year}")