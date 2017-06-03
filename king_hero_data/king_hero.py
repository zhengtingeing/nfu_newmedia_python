def get_hero_num():#从文件中提取英雄号码
    import csv
    with open('data/num.tsv','r',encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile,fieldnames=['h_name','h_num'])

        list_dict_num = []
        for row in reader:
            list_dict_num.append(dict(row))
        dict_num = {h['h_name']:h['h_num'] for h in list_dict_num}
    return(dict_num)

def convert_name_num(name):#输入英雄名，输出号码
    dict_num = get_hero_num()
    for x in dict_num:
        if name==x:
            num = dict_num[x]
    return(num)

def hero_information(name):#输入英雄名，输出技能和故事
    import requests
    from bs4 import BeautifulSoup

    try:
        hero_num = convert_name_num(name)
        page = requests.get('http://pvp.qq.com/web201605/herodetail/{n}.shtml'.format(n=hero_num))
        page.encoding='GBK'
        soup = BeautifulSoup(page.text,'html.parser')
    
        for tag in soup.find_all('div',class_='nr'):
            try:
                story = tag.find('p').text
            except:
                pass
        list_skill = []
        for tag in soup.find_all('p',class_='skill-p3'):
            hero_skill = tag.text
            list_skill.append(hero_skill)
        list_skill[0] = list_skill[0].strip('被动：')
        dict_story_skill = {name:[story,list_skill]}
        return(dict_story_skill)
    except UnboundLocalError:
        return('error')
