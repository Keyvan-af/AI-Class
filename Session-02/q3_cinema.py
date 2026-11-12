age = int(input("سن: "))
day = input("روز: ")

# Base price according to age
if age < 5:
    price = 0
elif 5 <= age <= 12:
    price = 50_000
elif age >= 60:
    price = 60_000
else:
    price = 100_000

# Special rule: 20% discount on Tuesday
if day == "سه شنبه" and price > 0:
    price = int(price * 0.8)

# Output
if price == 0:
    print("ورود رایگان!")
else:
    print(f"قیمت بلیط: {price} تومان")