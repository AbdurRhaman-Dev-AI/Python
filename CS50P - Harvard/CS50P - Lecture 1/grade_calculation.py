score = int(input("Enter your score (0-100): "))

if score >= 90 and score <= 100:
    print("Grade: AA+")
elif score >= 80 and score < 90:
    print("Grade: A+")
elif score >= 70 and score < 80:
    print("Grade: A")
elif score >= 60 and score < 70:
    print("Grade: B")
elif score >= 50 and score < 60:
    print("Grade: C")
elif score >= 40 and score < 50:
    print("Grade: D")
else:
    print("Grade: F")
