scores = {"Ali": 18, "Sara": 20, "Reza": 9, "Mina": 14, "Omid": 11.5}

# a) Print each student's score and rank
for name, score in scores.items():
    if score >= 17:
        rank = "عالی"
    elif score >= 14:
        rank = "خوب"
    elif score >= 10:
        rank = "قبول"
    else:
        rank = "مردود"
    print(f"{name}: {score} → {rank}")

# b) List of passing students (score >= 10)
passed = [name for name, score in scores.items() if score >= 10]
print("قبول شده‌ها:", passed)

# c) Class average
average = sum(scores.values()) / len(scores)
print("میانگین کلاس:", average)

# d) Top student
top_student = max(scores, key=scores.get)
print("نفر اول:", top_student)