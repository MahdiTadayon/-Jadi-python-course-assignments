import requests
import re
#import json
from bs4 import BeautifulSoup
r=requests.get('https://divar.ir/s/tehran')
#print(r.json())
soup=BeautifulSoup(r.text,'html.parser')
divs = soup.find_all('div', class_='kt-post-card__title')
tava=soup.find_all('div',attrs={'class':'kt-post-card__description'})
for div in divs:
    	for ta in tava:
		    if(re.sub(r'\s+',' ',ta.text).strip()=='توافقی'):
			    print(div.text)
    