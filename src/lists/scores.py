scores = [72, 81, 39]
average = sum(scores) / len(scores)

print("Average score : ", average,  "/100", sep="")
print()

i = 1
scores = []
while i > 0:
    try:
        score = int(input(f"Enter score for subject {i} : "))
        if score < 0 or score > 100:
            raise ValueError("Invalid score")
    except ValueError:
        print("Please enter a non -ve numeric value <= 100")
        continue
    else:
        scores.append(score)
        # OR use this syntax to append to list
        # scores += [score]
    choice = input("Do you want to continue inputting scores (y/n): ")
    if choice.lower() != "y":
        break
    i += 1
average = sum(scores) / len(scores)
print()
print(f"Average score of {i} subject(s): {average}/100")
