import threading
import urllib
import os
import random
import re
import ctypes
from fake_useragent import UserAgent # Must be installed
import time
import datetime
format = "%a %b %d %H:%M:%S %Y"
ua = UserAgent()
a = input('Enter Media Name: ') # Use . for spaces. Case Sensitive?
q = input('Enter Quality: ') # This checks for more parameters; 720p, 1080p, HEVC, etc 
t = input('Run Search Every _ seconds: ') # How often will it check
T = random.randint(int(t)-3,int(t)+6) # Randomise
r = input('Enter Uploader: ')# This is the user on PirateBay. 'TvTeam' for everthing, 'guccicar' for Bluray Remux, 'nayhtut' for HEVC
b = str('&dn='+a)
R = urllib.request.Request('https://pirateproxy.red/user/'+r,data=None,headers={'User-Agent': ua.random, })
try:
    page1 = urllib.request.urlopen(R).read()
    page1D = page1.decode('utf-8',errors='ignore')
except urllib.error.HTTPError as error:
    page1D = error.read()
    page1D = page1D.decode('utf-8',errors='ignore')
    print('HTTP Error1')

print('Start')
A = re.search(b,page1D)
# Search Page
while A == None:
    T = random.randint(int(t)-3,int(t)+6) # To not look like a bot.
    time.sleep(int(T)) # Time Loop
    try:
        R = urllib.request.Request('https://pirateproxy.red/user/'+r,data=None,headers={'User-Agent': ua.random, })
        page1 = urllib.request.urlopen(R).read()
        page1D = page1.decode('utf-8',errors='ignore')
    except urllib.error.HTTPError as error:
        page1D = error.read()
        page1D = page1D.decode('utf-8',errors='ignore')
        print('HTTP Error2')
    print('Searching for',a)
    A = re.search(b,page1D)
    

if A != None:
    aS = A.start() - 200      # Refine search for Magnet Link
    aF = A.end() + 600
    page1D = page1D[aS:aF]
    A = re.search('magnet:',page1D)
    B = re.search('" title="Download',page1D) # Be Specific!!!
    aS =A.start()
    aF =B.start()
    magLink = page1D[aS:aF]# Magnet found
    print(a,'Found')
    C = re.search(str(q),magLink)
    
while C == None:
    T = random.randint(int(t)-3,int(t)+6)
    print('Found',a,'but not',q)
    time.sleep(int(T))
    try:
        R = urllib.request.Request('https://pirateproxy.red/user/'+r,data=None,headers={'User-Agent': ua.random, })
        page1 = urllib.request.urlopen(R).read()
        page1D = page1.decode('utf-8',errors='ignore')
    except urllib.error.HTTPError as error:
        page1D = error.read()
        page1D = page1D.decode('utf-8',errors='ignore')
        print('HTTP Error3')
    print('Searching. for',a)
    A = re.search(b,page1D)
    
    while A == None:
        T = random.randint(int(t)-3,int(t)+6)
        time.sleep(int(T)) # Time Loop
        try:
            R = urllib.request.Request('https://pirateproxy.red/user/'+r,data=None,headers={'User-Agent': ua.random, })
            page1 = urllib.request.urlopen(R).read()
            page1D = page1.decode('utf-8',errors='ignore')
        except urllib.error.HTTPError as error:
            page1D = error.read()
            page1D = page1D.decode('utf-8',errors='ignore')
            print('HTTP Error4')
        A = re.search(b,page1D)
        print('Page reverted to cached')
        
    if A != None:
        print('Updated page loaded')
        aS = A.start() - 200      
        aF = A.end() + 600
        page1D = page1D[aS:aF]
        A = re.search('magnet:',page1D)
        B = re.search('" title="Download',page1D) # Be Specific!!!
        aS =A.start()
        aF =B.start()
        magLink = page1D[aS:aF]# Magnet found
        C = re.search(str(q),magLink)
        
if C !=None:
    fd=str(magLink)
    print('Magnet Found. Download Has Begun')
    now = datetime.datetime.now()
    Now = now.strftime(format)
    ctypes.windll.user32.MessageBoxW(None,a+"\nDownload Has Begun\n"+Now,"Magnet Found! ",0 ) 
    os.startfile(fd) #Open Magnet link in default app
    sys.exit()

        

