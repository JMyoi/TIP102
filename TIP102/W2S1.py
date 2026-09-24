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

#print(find_difference(signals1_example1, signals2_example1)) 


"""
Two space probes have collected signals represented by integer arrays signals1 and signals2 of sizes n and m, respectively. Calculate the following values:

answer1: the number of indices i such that signals1[i] exists in signals2.
answer2: the number of indices j such that signals2[j] exists in signals1.
Return [answer1, answer2].

"""

def find_common_signals(signals1: list[int], signals2: list[int]) -> tuple[int, int]:
    answer1 = 0
    answer2 = 0
    for i in signals1:
        if i in signals2:
            answer1+=1
    for i in signals2:
        if i in signals1:
            answer2+=1
    return answer1, answer2

def find_common_signals_usingSet(signals1: list[int], signals2: list[int]) -> tuple[int, int]:
    Set1 = set(signals1)
    Set2 = set(signals2)
    answer1 = 0
    answer2 = 0
    for i in signals1:
        if i in Set2:
            answer1+=1
    for i in signals2:
        if i in Set1:
            answer2+=1
    return answer1, answer2

def find_common_signals_usingSet(signals1: list[int], signals2: list[int]) -> tuple[int, int]:
    dict1 = {}
    dict2 = {}
    answer1 = 0
    answer2 = 0
    for i in signals1:
        if i in dict1 and i in signals2:
            dict1[i]+=1
        elif i in signals2:
            dict1[i] = 1
        else:
            dict1[i] = 0
    for i in signals2:
        if i in dict2 and i in signals1:
            dict2[i]+=1
        elif i in signals1:
            dict2[i] = 1
        else:
            dict2[i] = 0
    for v in dict1.values():
        answer1 +=v
    for v in dict2.values():
        answer2 +=v
    return answer1, answer2


signals1_example1 = [2, 3, 2]
signals2_example1 = [1, 2]
#print(find_common_signals_usingSet(signals1_example1, signals2_example1))

signals1_example2 = [4, 3, 2, 3, 1]
signals2_example2 = [2, 2, 5, 2, 3, 6]
#print(find_common_signals_usingSet(signals1_example2, signals2_example2))

signals1_example3 = [3, 4, 2, 3]
signals2_example3 = [1, 5]
#print(find_common_signals_usingSet(signals1_example3, signals2_example3))


"""
Ground control needs to analyze the frequency of signal data received from different probes. Given an array of integers signals, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order. Return the sorted array.

Below is a buggy or incomplete version of the solution. Identify and fix the bugs in the code. Then, perform a code review and suggest improvements.
"""

def frequency_sort(signals):
    freq = {}
    for signal in signals:
        if signal in freq:
            freq[signal] += 1
        else:
            freq[signal] = 1

    sorted_signals = sorted(signals, key=lambda x: (freq[x], -x))

    return sorted_signals

signals1 = [1, 1, 2, 2, 2, 3]
signals2 = [2, 3, 1, 3, 2]
signals3 = [-1, 1, -6, 4, 5, -6, 1, 4, 1]

# print(frequency_sort(signals1)) 
# print(frequency_sort(signals2)) 
# print(frequency_sort(signals3))


"""
You are given an array paths, where paths[i] = [hubA, hubB] means there exists a direct communication path going from hubA to hubB. Return the final communication hub, that is, the hub without any outgoing path to another hub.

It is guaranteed that the paths form a line without any loops, therefore, there will be exactly one final communication hub.

"""
# true meaning that the hub points to another 
#false meaning that that hub does not point to another meaning it's final destination.
# dict = {
#     "Earth": True,
#     "Mars": True, 
#     "Titan": True, 
#     "Europa": False
# }

def find_final_hub(paths: list[list[str]]) -> str:
    hubsPoint: dict[str, bool] = {} 
    for path in paths:
        origin: str = path[0]
        dest: str = path[1]
        hubsPoint[origin] = True
        if dest in hubsPoint:
            continue
        else:
            hubsPoint[dest] = False
    print(f"hubsPoint: {hubsPoint}")
    for hub, point in hubsPoint.items():
        if point == False:
            return hub

paths1 = [["Earth", "Mars"], ["Mars", "Titan"], ["Titan", "Europa"]]
paths2 = [["Alpha", "Beta"], ["Gamma", "Alpha"], ["Beta", "Delta"]]
paths3 = [["StationA", "StationZ"]]

print(find_final_hub(paths1)) 
print(find_final_hub(paths2)) 
print(find_final_hub(paths3))

"""
simpler soluiton using set, 
Simpler set-based approach:

The final hub is the one that appears as a destination but never as an origin. Sets make this a one-liner:


def find_final_hub(paths: list[list[str]]) -> str:
    origins = {path[0] for path in paths}
    dests = {path[1] for path in paths}
    return (dests - origins).pop()
This is O(n) and arguably clearer because it directly expresses the problem: "what's in destinations but not origins?"
"""

