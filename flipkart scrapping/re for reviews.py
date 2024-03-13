import re

def extract_portion_from_url(url):
    return '&'.join(url.split('/')[5:][0].split('&')[:3])

# Example URL
url = 'https://www.flipkart.com/raya-silicone-keyboard-cover-hp-victus-15-16-gaming-laptops-laptop-skin/p/itm563b1e30879ae?pid=KSNGSQJGEHNGHAHA&lid=LSTKSNGSQJGEHNGHAHAXUEYAD&marketplace=FLIPKART&q=keyboard+skin&store=6bo%2Fai3&srno=s_1_40&otracker=AS_QueryStore_HistoryAutoSuggest_6_0_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_6_0_na_na_na&fm=organic&iid=68f2f6eb-31b5-4f12-8013-31cdd385d8a1.KSNGSQJGEHNGHAHA.SEARCH&ppt=None&ppn=None&ssid=5r19w9omgw0000001710048786737&qH=e75f17a89f161240'
print('/'.join(url.split('/')[:4])+'/'+ '&'.join(url.split('/')[5:][0].split('&')[:3]))
# Extracting the desired portion
desired_portion = extract_portion_from_url(url)

print("Desired portion:",)

print([1,2,3,4][2:])
a=1
while a:
    print(23)
    a-=1
    
for index,j in enumerate(full_reviews):
    print(f'{index}. {j[0]}  {j[1]}\n{j[2]}')