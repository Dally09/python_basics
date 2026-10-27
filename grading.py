#score = 65

score = int(input("Enter your score: "))

# if statement
if score >= 90:
    print("A")
elif 80 <= score <= 89:
    print("A-")
elif 70 <= score <= 79:
    print("B")
elif 60 <= score <= 69:
    print("B-")
elif 50 <= score <= 59:
    print("C")
elif 40 <= score <= 49:
    print("C-")
elif 30 <= score <= 39:
    print("D")
elif score >= 20 or score <= 29:
#elif score >= 20 and score <= 29:
    print("D-")
else:
    print("E")