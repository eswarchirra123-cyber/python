# String Analyzer and Formatter
# Syllabus topics: string creation and manipulation, string methods, string formatting, input/output, loops
sentence = input("Enter a sentence: ")
clean = sentence.strip()
words = clean.split()
print("Length:", len(clean))
print("Uppercase:", clean.upper())
print("Lowercase:", clean.lower())
print("Title case:", clean.title())
print("Word count:", len(words))
print(f"Summary: Your sentence has {len(words)} words.")
