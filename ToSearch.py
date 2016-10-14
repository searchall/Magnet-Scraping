import requests
import time
import datetime
from bs4 import BeautifulSoup
import time
import sys
import ctypes
import urllib
import os
import random
import re
from fake_useragent import UserAgent


format = '%a %b %d %H:%M:%S %Y'
searchTerm = input('Enter Search Term: ')
att1 = input('Attribute 1: ')
att2 = input('Attribute 2: ')
T = input('Frequency: ')
ua = UserAgent()
urlPb = 'https://pirateproxy.vip/search/'+searchTerm+'/0/99/0'

while True:
    print('Searching')
    try:
        pageO = urllib.request.Request(urlPb,data=None,headers={'User-Agent': ua.random, })
        pageR = urllib.request.urlopen(pageO).read()
        pageR = pageR.decode('utf-8',errors='ignore')
        
    except urllib.error.HTTPError as error:
        pageR = error.read()
        pageR = pageR.decode('utf-8',errors='ignore')
        print('HTTP Error')


    soup = BeautifulSoup(pageR, 'lxml')
        
    magnets = [a['href'] for a in soup.find_all('a', title='Download this torrent using magnet')]
        
    for M in magnets:
        if att1 in M:
            print(M)
            if att2 in M:
                os.startfile(str(M))
                now = datetime.datetime.now()
                Now = now.strftime(format)
                ctypes.windll.user32.MessageBoxW(None,'Found!\n@\n'+Now,'Download Has Begun',0 )
                print('Magnet Found. Download Has Begun')
                sys.exit()
                break
            else:
                pass
        else:
            pass
    
    time.sleep(int(T))

