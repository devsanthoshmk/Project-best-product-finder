import time
st=time.time()
from lxml import etree
import csv

import requests
# url = f"https://www.flipkart.com/search?q=keyboard%20skin&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
            
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'}
# r = requests.get(url, headers=headers)
'''commit'''
file=open('flipkart scrapping/del.html')
html_content=file.read()
tree=etree.HTML(html_content)

products=tree.xpath('//div[@class="_4ddWXP"]')[:20]
full_list=[]#name#rat#price#reviews

for product in products:
    full_reviews=[]
    name_atag=product.xpath('.//a[@class="s1Q9rs"]')[0]
    try:
        rat=product.xpath('.//div[@class="_3LWZlK"]')[0].text
    except IndexError:
        rat="no ratings"
    url1="https://www.flipkart.com"+name_atag.get('href')
    url='/'.join(url1.split('/')[:4])+'/product-reviews/'+ '&'.join(url1.split('/')[5:][0].split('&')[:3])
    for page_no in range(1,3):
        headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"}
        r1 = requests.get(url+f'&page={page_no}', headers=headers)
        tree1=etree.HTML(r1.text)
        try:
            reviews=tree1.xpath('//div[@class="col _2wzgFH K0kLPL"]')
        except IndexError:
            pass
        
        for review in reviews:
            print(len(review))
            rat=review.xpath('./div[1]/div[1]')[0].text    
            review_title=review.xpath('./div[1]/p')[0].text
            review_discription=review.xpath('./div[2]/div[1]/div[1]/div[1]')[0].text
            full_reviews.append([rat,review_title,review_discription]) 
     
        if not tree1.xpath('//a[@class="_1LKTO3"]/span'):
                    break
    full_list.append([name_atag.get('title'),rat,product.xpath('.//div[@class="_30jeq3"]')[0].text,full_reviews])

file=open("delta.csv",'w')
wrter=csv.writer(file)
wrter.writerows(full_list)
file.close()
print(len(full_list))
# for index,j in enumerate(full_reviews):
#         print(f'{index}. {j[0]}  {j[1]}\n{j[2]}') 
    
print((time.time()-st)/60)