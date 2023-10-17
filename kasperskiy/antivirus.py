from collections import Counter

s = input().strip()

letter_counts = Counter(s)

word_counts = Counter("kaspersky")

print(min(letter_counts['k'] // 2, letter_counts['a'], letter_counts['s'] // 2,
      letter_counts['p'], letter_counts['e'], letter_counts['r'], letter_counts['y'],))
