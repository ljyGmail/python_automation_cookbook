import re

match = re.search(
    r'the phone number is ([\d-]+)', '37: the phone number is 1234-567-890')

print(f'match.group(): {match.group()}')
print(f'match.group(1): {match.group(1)}')

pattern = re.compile('The answer to question (\w+) is (yes|no)', re.IGNORECASE)

print(
    f"pattern.search('Naturally, the answer to question 3b is YES'): {pattern.search('Naturally, the answer to question 3b is YES')}")

print(
    f"pattern.search('Naturally, the answer to question 3b is YES').groups(): {pattern.search('Naturally, the answer to question 3b is YES').groups()}")

PATTERN = re.compile(r'([A-Z][\w\s]+?).(TX|OR|OH|MI)')
TEXT = 'the jackalopes are the team of Odessa,TX while the knights are native of Corvallis OR and the mud hens come from Toledo.OH; the whitecaps have their base in Grand Rapids,MI'
print(f'list(PATTERN.finditer(TEXT)): {list(PATTERN.finditer(TEXT))}')
print(f'PATTERN.findall(TEXT): {PATTERN.findall(TEXT)}')

# Groups can be assigned names. (?P<groupname>PATTERN)
PATTERN = re.compile(r'(?P<city>[A-Z][\w\s]+?).(?P<state>TX|OR|OH|MN)')
match = PATTERN.search(TEXT)

print(f'match.groupdict(): {match.groupdict()}')
print(f"match.group('city'): {match.group('city')}")
print(f"match.group('state'): {match.group('state')}")
print(f'(match.group(1), match.group(2)): {(match.group(1), match.group(2))}')
