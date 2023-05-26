import requests
from bs4 import BeautifulSoup
import re

URL = 'http://www.columbia.edu/~fdc/sample.html'
response = requests.get(URL)
print(f'response: {response}')

page = BeautifulSoup(response.text, 'html.parser')

print(f'page.title: {page.title}')
print(f'page.title.string: {page.title.string}')

print(f"page.find_all('h3'): {page.find_all('h3')}")

link_section = page.find('h3', attrs={'id': 'chars'})
print(link_section)

section = []

for element in link_section.next_elements:
    if element.name == 'h3':
        break
    section.append(element.string or '')

result = ''.join(section)
print(f'result: {result}')

h2_h3 = page.find_all(re.compile('^h(2|3)'))
print(h2_h3)
