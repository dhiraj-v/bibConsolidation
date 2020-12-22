from bs4 import BeautifulSoup
import re
import requests
def extractAllSpringer(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    prettyHTML = soup.prettify()
    pageTitle = soup.find("meta", {"name": "citation_title"})
    print(pageTitle['content'])
    
#The below is to call the function for the specific URL
extractAllSpringer('https://link.springer.com/chapter/10.1007/978-3-319-94496-8_10')

'''
Sample input tag structure 

<meta name="citation_title" content="Idea: Visual Analytics for Web Security"/>

'''
