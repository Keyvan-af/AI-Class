import matplotlib.pyplot as plt
import pandas as pd
import random

SEED = 42
N_PER_CLASS = 50   # 50 apples + 50 bananas = 100 fruits

rng = random.Random(SEED)

# ---- 1) Overlapping fruit data -------------------------------------------
# Both classes now share almost the same length & width ranges,
# so the clusters visibly blend together.
apples = [
    {"length": round(rng.uniform(7.0, 12.0), 1),
     "width":  round(rng.uniform(4.0, 7.5), 1),
     "fruit":  "apple"}
    for _ in range(N_PER_CLASS)
]
bananas = [
    {"length": round(rng.uniform(8.0, 13.0), 1),
     "width":  round(rng.uniform(3.5, 6.5), 1),
     "fruit":  "banana"}
    for _ in range(N_PER_CLASS)
]

df = pd.DataFrame(apples + bananas)     # 200 rows
X = df[["length", "width"]]
y = df["fruit"]

COLORS = {"apple": "red", "banana": "gold"}

# ---- 1) Plot all 100 fruits ----------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))
for fruit in ["apple", "banana"]:
    subset = df[df["fruit"] == fruit]
    ax.scatter(subset["length"], subset["width"],
               c=COLORS[fruit], label=fruit,
               edgecolors="k", s=60, alpha=0.8)
ax.set_xlabel("Length (cm)")
ax.set_ylabel("Width (cm)")
ax.set_title("100 fruits (overlapping classes)")
ax.legend()
ax.grid(alpha=0.3)
plt.show()

# ---- 2) Add one new fruit and plot 201 -----------------------------------
new_fruit = {"length": 10.0, "width": 5.5, "fruit": "new"}
NEW_COLOR = "blue"

fig, ax = plt.subplots(figsize=(8, 6))
for fruit in ["apple", "banana"]:
    subset = df[df["fruit"] == fruit]
    ax.scatter(subset["length"], subset["width"],
               c=COLORS[fruit], label=fruit,
               edgecolors="k", s=60, alpha=0.8)

ax.scatter(new_fruit["length"], new_fruit["width"],
           c=NEW_COLOR, label="new fruit",
           edgecolors="k", s=180, marker="*", zorder=5)

ax.set_xlabel("Length (cm)")
ax.set_ylabel("Width (cm)")
ax.set_title("101 fruits (new fruit in overlapping region)")
ax.legend()
ax.grid(alpha=0.3)
plt.show()

# ---- 3) Euclidean distances to all 200 -----------------------------------
dx = X["length"] - new_fruit["length"]
dy = X["width"]  - new_fruit["width"]
df["distance_to_new"] = (dx**2 + dy**2) ** 0.5

# Closest 10 = the real "neighbors" that would drive a k-NN vote
closest = df.sort_values("distance_to_new").head(10)
print(closest.to_string(index=False))
print("\nHow many of the 5 closest are apples vs bananas:")
print(df.nsmallest(5, "distance_to_new")["fruit"].value_counts())
print(df["distance_to_new"].describe())