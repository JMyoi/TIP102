def most_endangered(species_list) -> str:
    lowestSpeices = species_list[0].get("name")
    lowestPopulation = species_list[0].get("population")
    for species in species_list:
        print(f"on {species} ")
        if species.get("population") < lowestPopulation:
            lowestSpeices = species.get("name")
    return lowestSpeices

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))

#Week 2 TIP question on roman to integer

def roman_to_integer(s):
    romanNumerals: dict[str, int] = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100, 
        'D' : 500, 
        'M' : 1000, 
        'IV' : 4, 
        'IX' : 9, 
        'XL' : 40, 
        'XC' : 90, 
        'CD' : 400, 
        'CM' : 900
    }
    sum = 0
    i = len(s) - 1
    while i >= 0:
        # check next character to make sure it's not 2 digit subtraction 
        sliced = s[i-1:i+1]
        print(f"checking if {i} != 0 and if {sliced} is in the table")
        if i != 0 and sliced in romanNumerals:
            print(f"{sliced} is in table, now updating sum")
            sum += romanNumerals[sliced]
            i-=2
        else:
            print(f"Not in table, adding with {s[i]} = {romanNumerals[s[i]]}")
            sum += romanNumerals[s[i]]
            i -= 1
    return sum