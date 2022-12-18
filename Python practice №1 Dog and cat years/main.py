def human__years__cat__years__dog__years(humanYears):
    catYears = 0 
    dogYears = 0
    if humanYears < 1:
        return ("your kitty and puppy so small :) ")
    elif humanYears == 1:
        catYears += 15
        dogYears += 15
        return [humanYears,catYears,dogYears]
    elif humanYears == 2:
        catYears += 24 
        dogYears += 24
        return [humanYears,catYears,dogYears]
    elif humanYears > 2:
        catYears +=24
        dogYears +=24
        years = humanYears - 2
        catYears += years *4
        dogYears += years *5
        return [humanYears,catYears,dogYears]

age = int(input("how old is your dog and cat? "))
print(human__years__cat__years__dog__years(age))
