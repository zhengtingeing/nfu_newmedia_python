import requests
from bs4 import BeautifulSoup

input_num = int(input())
page = requests.get('http://pvp.qq.com/web201605/herodetail/{fn}.shtml'.format(fn=input_num))
page.encoding='GBK'
contents = page.text
soup = BeautifulSoup(contents,'html.parser')
print('背景故事')
for tag in soup.find_all('div', class_='nr'):
    hero_story = tag.find('p')
    try:
        print(hero_story.text)
    except:
        pass
print('\n'+'技能')
for tag in soup.find_all('p',class_='skill-p3'):
    hero_skill = (tag.text)
    print(hero_skill.strip('\n'))

input('\n\n'+'请按任意键退出')
