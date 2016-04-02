from google import search
import urllib2
import socket
import sys
from bs4 import BeautifulSoup

red	= 	"\033[01;31m"
green = 	"\033[01;32m"
yel =		"\033[01;33m"
norm	=	"\033[0m" 

def credit():
    print '''
	%s
	SQL vulnerability finder 
	https://github.com/maxstreiker/
	%s
	'''% (yel,norm)

def word_err(soup):
    i=-1
    words=['Warning', 'Fatal Error','Mysql','mysql','SQL','MySQL']
    for word in words:
	if word in str(soup):
		i+=1
    return i


def vuln_test(url):
    try:
	response =urllib2.urlopen(url)
	soup = BeautifulSoup( response.read(), 'html.parser' )
	url2=url+"'"
	response2=urllib2.urlopen(url2)
	soup2 = BeautifulSoup(response2.read(),'html.parser')
	if soup!=soup2 :
	    if word_err(soup2) > -1 :
		print "\n[%s*%s]Possible SQL vulnerability =>  %s "% (green,norm,url2)
    except urllib2.HTTPError :
	pass    
    except urllib2.URLError:
	pass
    
    
credit()
dork =raw_input("Inserire una dork (es: 'inurl:index.php?id=')  => ")
try:
    url_list=search(dork)
    for url in url_list:
	vuln_test(url)    
except urllib2.HTTPError:
    print "%sGoogle ban your IP%s (restart connection)  " %(red,norm)


