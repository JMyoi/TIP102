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

#print(most_endangered(species_list))

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


#
"""

Keep a frequency map of endangered species
endangeredFreq = {
    'a': 0,
    'A': 0
}
iterate through the obderved_species and check if that species exists in endangered, if it does incriment and incriment the endangered total count.
O(n + m)
"""
def count_endangered_species(endangered_species: str, observed_species: str) -> int:
    endangeredFreq: dict[str, int] = {}
    totalEndangered = 0
    for endangered in endangered_species:
        endangeredFreq[endangered] = 0
    for species in observed_species:
        if species in endangeredFreq:
            endangeredFreq[species] +=1
            totalEndangered+=1
    return totalEndangered
    


endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

#print(count_endangered_species(endangered_species1, observed_species1)) 
#print(count_endangered_species(endangered_species2, observed_species2))  


"""
    brute force, for every character in obervaions, get the index whtere tha character is found in the layout, 
    keep that number, continue until we get all index, 
    add them together at the end and return, 
    P(n^2)

    make a dict of station layout iwth index, letter, to index
    {
        'p' = 0,
        'q' = 1
        ...
    }
    for every char in observation, find it's mapping index and compute the absolute difference of how we got there, | i - j |.
    we take the absolute value because it accounts for  going backwards and foward in index. 
        prevIndex = 4 - current = 2 totalDistance = 2, | 4 - 2 | = 2
        prev index = 5 - current = 8 total distance = 3, |5 - 8| = 3


"""
def navigate_research_station(station_layout: str, observations: str) -> int:
    stationIndexMap: dict[str, int] = {}
    runningSum: int = 0
    for i, station in enumerate(station_layout):
        stationIndexMap[station] = i
    print(f"Mapping: {stationIndexMap}")
    prevIndex = 0;
    for char in observations:
        currIndex = stationIndexMap.get(char)
        runningSum += abs(prevIndex - currIndex)
        prevIndex = currIndex
    return runningSum



station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

#print(navigate_research_station(station_layout1, observations1))  
#print(navigate_research_station(station_layout2, observations2))


"""

In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.

Write a function prioritize_observations() that sorts the elements of observed_species such that the relative ordering of items in observed_species matches that of priority_species. Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.
make a map of species and priority
{
    "cardinal": 1
}
then for every observed animal, if they are in priority list, then keep a new has table called frequendcy of the priority animal and the count of them observed,
if it is not a priority species then add it to a new array and at the end we will sort via alpahbetic order, 
turn the frequency inot an array.
then combine the two arrays into extend
"""

def prioritize_observations(observed_species, priority_species):
    priorityFreq = {}

    for species in priority_species:
        priorityFreq[species] = 0
    nonPriority = []

    for species in observed_species:
        if species in priorityFreq:
            priorityFreq[species] +=1
        else:
            nonPriority.append(species)
    
    nonPriority.sort()
    SortedSpecies = []
    for species in priority_species:
        SortedSpecies.extend([species] * priorityFreq[species])
    SortedSpecies.extend(nonPriority)

    return SortedSpecies

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

#print(prioritize_observations(observed_species1, priority_species1))
#print(prioritize_observations(observed_species2, priority_species2)) 

"""
problem 5
find amx and min of array, remove them, avereage them and push to distinct average
"""

def distinct_averages(species_populations) -> int:
    distinctAverage: set[float] = set()
    while species_populations:
        high: float = max(species_populations)
        low: float = min(species_populations)
        avg = (high + low) / 2
        distinctAverage.add(avg)
        species_populations.remove(high)
        species_populations.remove(low)
    return len(distinctAverage)

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 


    