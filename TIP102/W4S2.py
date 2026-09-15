#Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. You need to identify if there is a pair of tasks whose combined time matches the available slot.

#Given a list of integers representing the time required for each task and an integer representing the available time slot, write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.
"""





"""
#Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_task_pair(task_times, available_time):
    l = 0
    r = len(task_times) - 1
    while l < r:
        sum_task = task_times[l] + task_times[r]
        if sum_task == available_time:
            return True
        elif sum_task > available_time:
            r -= 1
        else: 
            l += 1
    return False
                                      
                                      
task_times = [30, 45, 60, 90, 120]
available_time = 105
#print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
#print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
#print(find_task_pair(task_times_3, available_time))


"""
You work with clients across different time zones and often have gaps between your work sessions. You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, each with a start time and an end time. Your task is to find the smallest gap between any two consecutive work sessions.

Given a list of tuples where each tuple represents a work session with a start and end time (both in 24-hour format as integers, e.g., 1300 for 1:00 PM), write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

"""

"""
On the conversion, t // 100 peels off the hours and t % 100 peels off the minutes, 
so 1300 becomes 13*60 + 0 = 780 and 1230 becomes 12*60 + 30 = 750
1230 - 750 = 480

1500: 15 * 60 + 0 = 900
70: 7 * 60 = 42 - 7 modulo 100 = 30
1600: 16 * 60 + 0 = 960

960 - 900 = 60

"""

def find_smallest_gap(work_sessions):
    time = []
    for sessions in work_sessions:
        time.append(sessions[0])
        time.append(sessions[1])
    difference = []
    for i, t in enumerate(time):
        if i == (len(time) - 1):
            break;
        curr = time[i]
        Next = time[i+1] 
        C_curr = (curr // 100) * 60 + (curr % 100)
        N_min = (Next // 100) * 60 + (Next % 100 )
        diff = N_min - C_curr
        difference.append(diff)
    return min(difference)
        
# 2n = O(n)

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
#print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
#print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
#print(find_smallest_gap(work_sessions_3))


"""
You travel frequently and need to keep track of your expenses. You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), write a function that returns the expense categories and the total expenses for each category. Additionally, the function should return the category with the highest total expense.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

{
 "food": 12.5 + 7.5, 
 "Transportation":  15.0, 
 "Accommodation": 50.0
 
}
"""


def calculate_expenses(expenses):
    total = {}
    for expense in expenses:
        if expense[0] in total:
            total[expense[0]] += expense[1]
        else:
            total[expense[0]] = expense[1]
    maxi = 0
    maxName = ""
    for key, value in total.items():
        if value > maxi:
            maxi = value
            maxName = key
    return (total, maxName)
            
            


expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))

"""
As a digital nomad who writes blogs, articles, and reports regularly, it's important to analyze the text you produce to ensure clarity and avoid overusing certain words. You want to create a tool that analyzes the frequency of each word in a given text and identifies the most frequent word(s).

Given a string of text, write a function that returns the unique words and the number of times each word appears in the text. Additionally, return a list of the word(s) that appear most frequently.
"""