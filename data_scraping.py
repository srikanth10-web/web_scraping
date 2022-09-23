import requests
from bs4 import BeautifulSoup
import csv
import pandas as p
url = "https://www.techmarkettips.com/?s=technology"
r=requests.get(url)
soup = BeautifulSoup(r.content,"html.parser")
titles=soup.find_all('div',class_='read-title')
category=soup.find_all('div',class_='read-categories')
#print(category)
mt=[]
mc=[]
for title,cat in zip(titles,category):
  mt.append(title.text)
  mc.append(cat.text)
#print(mt)
#print(mc)
d = {'mt':mt,'mc':mc}
model = p.DataFrame(data=d)
model.to_csv('tmt.csv')
