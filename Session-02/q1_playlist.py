playlist = ["Shape of You", "Blinding Lights", "Believer", "Perfect"]

print("Number of songs:", len(playlist))

print("first song:", playlist[0])
print("last song:", playlist[-1])

playlist.append("Dynamite")

playlist.remove("Believer")

playlist.sort()
print("Sorted playlist:", playlist)

for i, song in enumerate(playlist):
    print(f"{i+1}. {song}")