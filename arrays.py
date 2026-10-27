#store lots of data
#age = 18
#age_2 = 22

#data structures
#list, set, tuple, dictionary, queue

#people = [] #this is an empty list

people = ["Jack", "Mercy", "Jane", "Jill", "John"]
scores = [87, 45, 67, 52, 91, 29, 66, 71, 81]

#print(people[0], scores[0]) #first value

#print(people[-1]) #last value

#people.append("Willis") #add to list
#print(people)
#scores.append(90)
#print(scores)

#print(people)

people.sort()  #alphabetical
#print(people)
scores.sort()  #smallest to largest
#print(scores)

#print(scores[0], scores[-1])

#scores.sort(reverse=True)
#print(scores[3])

#print(round(sum(scores) / len(scores),3))

#scores.__eq__(91)
#print(True/False)

#print(scores.count(91))

scores.sort()
#slicing
#print(scores)
#print(scores[:3])  #top 3
#print(scores[-3:])  #last 3
#print(scores[3:5])  #does not include last number
#print(scores[::2])
#print(scores[::3])
#print(scores[::-1]) #is it sort in reverse?
#print(scores[::-2]) #reverse even numbers
#print(scores[::4]) #counts 4 and prints

#set - removes duplicates
numbers = {87, 89, 87, 67, 54}
#print(numbers)

#tuple - immutable data (data I do not want to change)
days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
#print(days.index("Sat"))

#dictionary - key + value
person = {"name": "Ben", "city": "Nairobi", "age": 24}
#print(person["name"])

#employees = []
#employees.append(person)
#employees.append(person)

employee = [
    {
        "name": "Karen", "age": 35 },
    {
        "name": "Greg", "age": 28 },
    {
        "name": "Anne", "age": 24 },
    ]
print(employee[1]["name"])
