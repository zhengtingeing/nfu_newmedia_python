# -*- coding: utf-8 -*- 
import requests
from bs4 import BeautifulSoup

dict_num = dict()
for num in range(100,201):
    page = requests.get('http://pvp.qq.com/web201605/herodetail/{n}.shtml'.format(n=num))
    page.encoding='GBK'
    soup = BeautifulSoup(page.text,'html.parser')
    for tag in soup.find_all('div',class_='con1-pos'):
        hero_name = tag.find('label').text
        dict_num.setdefault(tag.find('label').text)
        dict_num[hero_name] = tag.find('span',class_='hidden').text
list_dict_num = [{'h_name': k, 'h_num': v} for k,v in dict_num.items()]
print(list_dict_num)

import csv
with open('data/num.tsv', 'w', encoding='utf8') as csvfile:
    fieldnames = ['h_name', 'h_num']
    writer = csv.DictWriter(csvfile, fieldnames=['h_name', 'h_num'])
    writer.writerows (list_dict_num)
