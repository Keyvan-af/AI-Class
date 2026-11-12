words = {
    "i": "من",
    "love": "دوست دارم",
    "python": "پایتون",
    "ai": "هوش مصنوعی",
    "you": "تو",
    "we": "ما",
    "book": "کتاب",
}

sentence = "I love python and AI"

translated = []
translated_count = 0
untranslated_count = 0

for word in sentence.split():
    key = word.lower()
    if key in words:
        translated.append(words[key])
        translated_count += 1
    else:
        translated.append(f"[{word}]")
        untranslated_count +=1
    
print(" ".join(reversed(translated)))

print("Number of translated words:", translated_count)
print("Number of untranslated words:", untranslated_count)