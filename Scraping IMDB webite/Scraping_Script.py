import pandas as pd 
import requests
from bs4 import BeautifulSoup




html_code=requests.get('https://www.imdb.com/search/title/?groups=top_1000').text

def delete_1(a):
    a=a.replace('\n','')
    return a.strip()
cl=['runtime','genre','value']
L=[]
for i in range(0,len(soup.find_all('div',class_='lister-item-content'))):
    
    
    soup_1=soup.find_all('div',class_='lister-item-content')[i]
    A=[]
    A.append(soup_1.find('a').text)
    for c in cl:
        if c!='genre':
            A.append(delete_1(soup_1.find('span',class_=c).text))
        else:
            AA=[]
            AA.append(delete_1(soup_1.find('span',class_=c).text))
            A.append(AA)
        
        
    A.append(delete_1(soup_1.find_all('p', class_='text-muted')[1].text))
    
    AA=soup_1.find_all('p',class_='')[0].text
    l=AA.split('|')
    Directors=delete_1(l[0]).split(':')
    Directors=Directors[1].split(',')
    
    Stars=delete_1(l[1]).split(':')
    Stars=Stars[1].split(',')
    A.append(Directors)
    A.append(Stars)
    
    year=a.find('span',class_='lister-item-year text-muted unbold').text
    A.append(int(year[1:len(year)-1]))
    
    
    
    G_V=soup_1.find_all('p',class_='sort-num_votes-visible')[0]
    l=G_V.find_all('span')
    votes=l[1].text
    votes=int(votes.replace(',',''))
    if len(l)>2:
        Gross=l[4].text
        Gross=float(Gross[1:len(Gross)-1])
    else:
        Gross=None
    
    A.append(votes)
    A.append(Gross)
    
    L.append(A)

columns=['Title','Runtime','Genres','Score','Description','Directors','Stars','Year','Numbre of votes','Gross(M$)']

columns=['Title','Runtime','Genres','Score','Description','Directors','Stars','Year','Numbre of votes','Gross(M$)']
df=pd.DataFrame(L,columns=columns)
df.to_excel('data.xlsx')