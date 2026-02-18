def calculate_score(correct, wrong):
    score = (correct * 4) - (wrong * 1)
    return score


print("NEET Biology Score Calculator (90 Questions)")
print("--------------------------------------------")

correct = int(input("Enter number of correct answers: "))
wrong = int(input("Enter number of wrong answers: "))

if correct + wrong > 90:
    print("Error: Total questions cannot exceed 90.")
else:
    score = calculate_score(correct, wrong)
    print("\nYour Final Score is:", score, "out of 360")
