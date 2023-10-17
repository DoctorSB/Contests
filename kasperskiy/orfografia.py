import string

def spell_check(input_str, dictionary):
    words = input_str.split()
    result = []
    for word in words:
        cleaned_word = word.strip(string.punctuation)
        if cleaned_word.lower() in dictionary:
            result.append('.' * len(word))
        elif cleaned_word.lower() == '':
            result.append('.' * len(word))
        else:
            result.append('~' * len(word))
    return ''.join(result)

res_str = input()
input_str = res_str.replace(' ', ' . ')

punctuation_symbols = [',', '.', '(', ')', '!', '?', ';', ':', '-', '[', ']',
                       '{', '}', '/', '\\', '|', '<', '>', '+', '=', '*', '&', '%', '^', '#', '@', '_', '`', '"', "'", '~']
dictionary = set(punctuation_symbols)

for _ in range(int(input())):
    dictionary.add(input().lower())

output_str = spell_check(input_str, dictionary)

print(res_str)
print(output_str)
