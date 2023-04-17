INPUT_TEXT = """
    AFTER THE CLOSE OF THE SECOND QUARTER, OUR COMPANY, CASTAÑACORP
    HAS ACHIEVED A GROWTH IN THE REVENUE OF 7.47%. THIS IS IN LINE
    WITH THE OBJECTIVES FOR THE YEAR. THE MAIN DRIVER OF THE SALES HAS BEEN
    THE NEW PACKAGE DESIGNED UNDER THE SUPERVISION OF OUR MARKETING DEPARTMENT.
    OUR EXPENSES HAS BEEN CONTAINED, INCREASING ONLY BY 0.7%, THOUGH THE BOARD
    CONSIDERS IT NEEDS TO BE FURTHER REDUCED. THE EVALUATION IS SATISFACTORY
    AND THE FORECAST FOR THE NEXT QUARTER IS OPTIMISTIC. THE BOARD EXPECTS
    AN INCREASE IN PROFIT OF AT LEAST 2 MILLION DOLLARS.
"""

words = INPUT_TEXT.split()
print(f'words: {words}')

redacted = [''.join('X' if w.isdigit() else w for w in word) for word in words]
print(f'redacted: {redacted}')

ascii_text = [word.encode('ascii', errors='replace').decode(
    'ascii') for word in redacted]
print(f'ascii_text: {ascii_text}')

newlines = [word + '\n' if word.endswith('.') else word for word in ascii_text]
print(f'newlines: {newlines}')

LINE_SIZE = 80
lines = []
line = ''
for word in newlines:
    if line.endswith('\n') or len(line) + len(word) + 1 > LINE_SIZE:
        lines.append(line)
        line = ''
    line = line + ' ' + word

print(f'lines: {lines}')

lines = [line.title() for line in lines]
print(f'lines after title(): {lines}')

result = '\n'.join(lines)
print(f'result: {result}')
