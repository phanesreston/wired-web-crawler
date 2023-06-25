import requests
from bs4 import BeautifulSoup

URL = 'https://www.wired.com/'
headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}
page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
stories = soup.find_all('a', href=True)
story_array = []

for story in stories:
    story_href = story['href']
    if '/story/' in story_href:
        if '#' not in story_href:
            if story_href not in story_array: 
                story_array.append(story_href)
                print(story_href)