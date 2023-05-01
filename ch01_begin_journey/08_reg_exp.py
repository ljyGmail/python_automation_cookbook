import re

print(f"re.search(r'LOG','LOGS'): {re.search(r'LOG','LOGS')}")
print(f"re.search(r'LOG', 'NOT A MATCH'): {re.search(r'LOG', 'NOT A MATCH')}")

# How to do it...
# Match a pattern that is not at the start of the string
print(f"re.search(r'LOG','SOME LOGS'): {re.search(r'LOG','SOME LOGS')}")

# Match a pattern that is only at the start of the string
print(f"re.search(r'^LOG','LOGS'): {re.search(r'^LOG','LOGS')}")
print(f"re.search(r'^LOG', 'SOME LOGS'): {re.search(r'^LOG', 'SOME LOGS')}")

# Match a pattern that is only at the end of the string
print(f"re.search(r'LOG$','SOME LOG'): {re.search(r'LOG$','SOME LOG')}")
print(f"re.search(r'LOG$','SOME LOGS'): {re.search(r'LOG$','SOME LOGS')}")

# Match the word 'thing'
STRING = 'something in the things she shows me'
match = re.search(r'thing', STRING)
print(
    f'(STRING[:match.start()], STRING[match.start():match.end()], STRING[match.end():]): \
        {(STRING[:match.start()], STRING[match.start():match.end()], STRING[match.end():])}')
# Match the word 'thing' but not something or anything
match = re.search(r'\bthing', STRING)
print(
    f'(STRING[:match.start()], STRING[match.start():match.end()], STRING[match.end():]): \
        {(STRING[:match.start()], STRING[match.start():match.end()], STRING[match.end():])}')

# Match a pattern that's only numbers and dashes
print(
    f"re.search(r'[01234567890-]+', 'the phone number is 1234-567-890'): \
        {re.search(r'[01234567890-]+', 'the phone number is 1234-567-890')}")
print(
    f"re.search(r'[0123456789-]+', 'the phone number is 1234-567-890').group(): \
        {re.search(r'[0123456789-]+', 'the phone number is 1234-567-890').group()}")

# Match" an email address naively
print(f"re.search(r'\S+@\S+', 'my email is email.123@test.com').group():",
      re.search(r'\S+@\S+', 'my email is email.123@test.com').group())

match = re.search(r'[0123456789-]+', 'the phone number is 1234-567-890')
print(
    f"[int(n) for n in match.group().split('-')]: {[int(n) for n in match.group().split('-')]}")
