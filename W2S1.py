#Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.

def space_crew(crew: list[str], position: list[str]) -> dict[str, str]:
    SpaceStation: dict[str, str] = {}
    for i in range(len(crew)):
        SpaceStation[crew[i]] = position[i]
    return SpaceStation

exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

#print(space_crew(exp70_crew, exp70_positions))
#print(space_crew(ax3_crew, ax3_positions))

#Given a dictionary planets that maps planet names to a dictionary containing the planet's number of moons and orbital period, write a function planet_lookup() that accepts a string planet_name and returns a string in the form Planet <planet_name> has an orbital period of <orbital period> Earth days and has <number of moons> moons. If planet_name is not a key in planets, return "Sorry, I have no data on that planet.".



def planet_lookup(planet_name: str) -> str:
    planetary_info = {
        "Mercury": {
            "Moons": 0,
            "Orbital Period": 88
        },
        "Earth": {
            "Moons": 1,
            "Orbital Period": 365.25
        },
        "Mars": {
            "Moons": 2,
            "Orbital Period": 687
        },
        "Jupiter": {
            "Moons": 79,
            "Orbital Period": 10592
        }
    }
    result = planetary_info.get(planet_name)
    if result == None:
        return "Sorry, I have no data on that planet."
    else:
        return f"Planet {planet_name} has an orbital period of {result.get("Orbital Period")} Earth days and has {result.get("Moons")} moons."


#print(planet_lookup("Mars"))
#print(planet_lookup("Pluto"))

#As part of your job as an astronaut, you need to perform routine safety checks. You are given a dictionary oxygen_levels which maps room names to current oxygen levels and two integers min_val and max_val specifying the acceptable range of oxygen levels. Return a list of room names whose values are outside the range defined by min_val and max_val (inclusive).

def check_oxygen_levels(oxygen_levels: dict[str, int], min_val: int, max_val: int) -> list[str]:
    badRooms: list[str] = []
    for room, level in oxygen_levels.items():
        if level <= min_val or level >= max_val:
            badRooms.append(room)
    return badRooms

oxygen_levels = {
    "Command Module": 21,
    "Habitation Module": 20,
    "Laboratory Module": 19,
    "Airlock": 22,
    "Storage Bay": 18
}

min_val = 19
max_val = 22

#print(check_oxygen_levels(oxygen_levels, min_val, max_val))

# Write a function data_difference() that accepts two dictionaries experiment1 and experiment2 and returns a new dictionary that contains only key-value pairs found exclusively in experiment1 but not in experiment2.

def data_difference(experiment1: dict[str, int], experiment2: dict[str, int]) -> dict[str, int]:
    result: dict[str, int] = {}
    for k, v in experiment1.items():
        if k in experiment2 and experiment2.get(k) == v:
            continue
        else:
            result[k] = v
    return result

exp1_data = {'temperature': 22, 'pressure': 101.3, 'humidity': 45}
exp2_data = {'temperature': 18, 'pressure': 101.3, 'radiation': 0.5}

#print(data_difference(exp1_data, exp2_data))

#NASA has asked the public to vote on a new name for one of the nodes in the International Space Station. Given a list of strings votes where each string in the list is a voter's suggested new name, implement a function get_winner() that returns the suggestion with the most number of votes.

def get_winner(votes: list[str]) -> str:
    freqMap: dict[str, int] = {}

    for vote in votes:
        if freqMap.get(vote):
            freqMap[vote] +=1
        else:
            freqMap[vote] = 1

    print(f"freq map: {freqMap}")

    biggest = [0, ""]
    for name, voteCount in freqMap.items():
        print(f"is {voteCount} > {biggest[0]}")
        if voteCount > biggest[0]:
            biggest[1] = name
            biggest[0] = voteCount
            print(f"yes!, updating, to {name}")
    return biggest[1]

votes1 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert", "Colbert"]
votes2 = ["Colbert", "Serenity", "Serenity", "Tranquility", "Colbert"]

#print(get_winner(votes1))
#print(get_winner(votes2))


'''
Ground control has sent a transmission containing important information. A complete transmission is one where every letter of the English alphabet appears at least once.

Given a string transmission containing only lowercase English letters, return true if the transmission is complete, or false otherwise.
'''
"""
use a set to store all letters
Assuming that all inputs are all lowercase and english letters: 
false conditions
    if there is a repeat then return false
    if by the end the set size is not 26 then return false
true conditions
    if by the end the size of the set is 26
# """

def check_if_complete_transmission(transmission: str) -> bool:
    S:set = set()
    for char in transmission: 
        S.add(char)
    print(f"end of loop, length of set is: {len(S)}")
    return len(S) == 26
    
transmission1 = "thequickbrownfoxjumpsoverthelazydog"
transmission2 = "spacetravel"

#print(check_if_complete_transmission(transmission1))
#print(check_if_complete_transmission(transmission2))


# Signal Pairs

def max_number_of_string_pairs(signals: list[str]) -> int:
    signalFreq: dict[str, int] = {}
    totalPairs: int = 0
    for s in signals:
        revStr: str = s[::-1]
        print(f"reversed string: {revStr}")
        if revStr in signalFreq:
            signalFreq[revStr]+=1
            totalPairs+=1
        else:
            signalFreq[s] = 1
    return totalPairs

signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

# print(max_number_of_string_pairs(signals1))
# print(max_number_of_string_pairs(signals2))
# print(max_number_of_string_pairs(signals3))


# Q8 Find Differenc eof Two signal arrays

def find_difference(signals1: list[int], signals2: list[int]) -> tuple[list[int], list[int]]:
    Set1: set[int] = set(signals1)
    Set2: set[int] = set(signals2)
    return Set1 - Set2, Set2 - Set1



signals1_example1 = [1, 2, 3]
signals2_example1 = [2, 4, 6]

print(find_difference(signals1_example1, signals2_example1)) 
