import re

bcts_str = input()
pattern = re.compile(r'\(\)|\{\}|\[\]')

while pattern.search(bcts_str):
    bcts_str = pattern.sub('', bcts_str, count=1)

if len(bcts_str) != 0:
    print('no')
else:
    print('yes')