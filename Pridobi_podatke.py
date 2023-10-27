import requests
import re

for el in range(53, 100):
    for i in range(el*1000, (el+1)*1000):
        stran = requests.get(
            f'https://www.judoinside.com/judoka/{i}/judo-career'
        )
        with open(f'htmlji/skupek_strani{el+1}.html', 'a', encoding='utf-8') as dat:
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