import requests
import re

for i in range(1, 51):
    stran = requests.get(
        f'https://www.judoinside.com/judoka/{i}/judo-career'
    )
    with open('htmlji/big_stran.html', 'a', encoding='utf-8') as dat:
        dat.write(stran.text)


#for i in range(1, 101):
#    stran = requests.get(
#        f"https://www.judoinside.com/judoka/{i}/judo-career"
#    )
#
#    with open(f'htmlji/stran{i}.html', 'w', encoding='utf-8') as dat:
#        dat.write(stran.text)

#import requests
#
#stran = requests.get(
#    "https://www.imdb.com/search/title/?title_type=feature&num_votes=1000000,&sort=user_rating,desc&count=250"
#)
#
## print(stran)
## print(stran.text)
#with open("stran1.html", "w", encoding='utf-8') as dat:
#    dat.write(stran.text)
#
#for i in range(10):
#    stran = requests.get(
#        f"https://www.imdb.com/search/title/?title_type=feature&num_votes=10000,&sort=user_rating,desc&count=250&start={1+i*250}&ref_=adv_nxt"
#    )
#    with open(f"stran{i}.html", "w", encoding='utf-8') as dat:
#        dat.write(stran.text)


#from selenium import webdriver
#import time
#
#browser=webdriver.Chrome()
#
#browser.get('https://judobase.ijf.org/#/competition/profile/2346/results/0')
#html = browser.page_source
#time.sleep(10)
#with open('stran3.html', 'w', encoding='utf-8') as dat:
#    dat.write(html)
#    
#browser.close()