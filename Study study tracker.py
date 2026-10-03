print("STUDY TRACKER")

subject = input("Enter subject: ")
hours = float(input("Hours studied: "))

print("\n--- Study Summary ---")
print("Subject:", subject)
print("Study Time:", hours, "hours")

if hours >= 3:
    print("Great work! ")
elif hours >= 1:
    print("Good job! Keep going")
else:
    print("Let's try a little more tomorrow")
