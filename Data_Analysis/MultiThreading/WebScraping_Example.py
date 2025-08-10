'''
Real World Example: for I/O bound tasks
Web Scapping
many network requests to fetch web pages, These tasks are I/ bound
becuase they spend a lot of time waiting for responses from 
servers. Multithreading can imporve the performance by alloweing
mutiple web pages to be fetched concurrently
'''
import threading
from concurrent.futures import ProcessPoolExecutor
import requests
#import bs4 web scraping
from bs4 import BeautifulSoup
##charmap error : solved when put encoding = 'utf-8'


urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/tutorials/',
    'https://python.langchain.com/docs/how_to/'
]

files = [
    'data1.txt',
    'data2.txt',
    'data3.txt'
]
def fetch_content(url,file_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f'fetched lengeth : {len(soup.text)} charecters from all url')
    with open(file_path,'w',encoding='utf-8') as file:
        file.write(soup.get_text())

threads = []
for url,file in zip(urls,files):
    thread = threading.Thread(target=fetch_content,args=(url,file,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web pages fetched")


