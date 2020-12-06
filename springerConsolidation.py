from bs4 import BeautifulSoup
import re
import requests

def extractDetailSpringer(url):
    abstract = ''
    authorKeywords = ''
    pages = ''
    citations = ''
    uniList = ''
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    prettyHTML = soup.prettify()
    abstractParas = soup.findAll("p", {"class": "Para"})
    #authors = soup.findAll("span", {"class": "authors-affiliations__name"})
    pageNumbers = soup.find("span", {"class": "page-numbers-info"})
    keywords = soup.findAll("span", {"class": "Keyword"})
    citationCount = soup.find("span", {"class": "test-metric-count c-button-circle gtm-chaptercitations-count"})
    universities = soup.findAll("span", {"class": "affiliation__name"})
    #print('PAGES: ')
    regexPages = r'(?!0|1$)\d{1,4}[-](?!0|1$)\d{1,4}'
    pages = re.search("(?!0|1$)\d{1,4}[-](?!0|1$)\d{1,4}", str(pageNumbers.contents[0])).group()
    #print(pages)
    #print('KEYWORDS: ')
    for word in keywords: 
        authorKeywords += str(word.contents)[2:-6]
        authorKeywords += '; '
    #print(authorKeywords)
    #print('CITATIONS: ')
    if not citationCount:
        citations = '0'
    else: 
        citations = (str(citationCount.contents)[2:-2])
    #print(citations)
    #print("UNIVERSITIES: ")
    for uni in universities: 
        uniList += str(uni.contents)[2:-2]
        uniList += '; '
    #print(uniList)
    #print('ABSTRACT: ')
    for para in abstractParas: 
        abstract += str(para.contents)[2:-2]
    #print(abstract)
    return pages, authorKeywords, citations, uniList, abstract
