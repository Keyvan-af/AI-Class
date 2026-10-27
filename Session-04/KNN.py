import matplotlib.pyplot as plt
import pandas as pd
import random

SEED = 42
N_PER_CLASS = 100   # 100 apples + 100 bananas = 200 fruits

# ---- 1) Build 200 fruits with length & width ------------------------------
rng = random.Random(SEED)

apples = [
    {"length": round(rng.uniform(6, 9), 1),
     "width":  round(rng.uniform(6, 8), 1),
     "fruit":  "apple"}
    for _ in range(N_PER_CLASS)
]
bananas = [
    {"length": round(rng.uniform(12, 20), 1),
     "width":  round(rng.uniform(2, 4), 1),
     "fruit":  "banana"}
    for _ in range(N_PER_CLASS)
]

df = pd.DataFrame(apples + bananas)     # 200 rows
X = df[["length", "width"]]
y = df["fruit"]

COLORS = {"apple": "red", "banana": "gold"}

# ---- 1) Plot all 200 fruits ----------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
for fruit in ["apple", "banana"]:
    subset = df[df["fruit"] == fruit]
    ax.scatter(subset["length"], subset["width"],
               c=COLORS[fruit], label=fruit,
               edgecolors="k", s=60, alpha=0.8)
ax.set_xlabel("Length (cm)")
ax.set_ylabel("Width (cm)")
ax.set_title("200 fruits")
ax.legend()
ax.grid(alpha=0.3)
plt.show()

# ---- 2) Add one new fruit and plot 201 ------------------------------------
new_fruit = {"length": 10.5, "width": 5.0, "fruit": "new"}
NEW_COLOR = "blue"

fig, ax = plt.subplots(figsize=(8, 6))

# first: the 200 original fruits
for fruit in ["apple", "banana"]:
    subset = df[df["fruit"] == fruit]
    ax.scatter(subset["length"], subset["width"],
               c=COLORS[fruit], label=fruit,
               edgecolors="k", s=60, alpha=0.8)

# then: the 201st fruit, highlighted with its own color + marker
ax.scatter(new_fruit["length"], new_fruit["width"],
           c=NEW_COLOR, label="new fruit",
           edgecolors="k", s=140, marker="*", zorder=5)

ax.set_xlabel("Length (cm)")
ax.set_ylabel("Width (cm)")
ax.set_title("201 fruits (new fruit highlighted)")
ax.legend()
ax.grid(alpha=0.3)
plt.show()

# ---- 3) Euclidean distances from the new fruit to all 200 ----------------
dx = X["length"] - new_fruit["length"]
dy = X["width"]  - new_fruit["width"]
distances = (dx**2 + dy**2) ** 0.5      # pandas Series, one per fruit

df["distance_to_new"] = distances       # save them next to the data
print(df.head(10))                      # peek
print(f"\nTotal distances computed: {len(df)}")
