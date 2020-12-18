from bs4 import BeautifulSoup
import re
import requests
def extractDetailSpringer(url):
    abstract = ''
    authorKeywords = ''
    pages = ''
    citations = ''
    uniList = ''
    returnData = []
    '''
    pages, keywords, citeCount, university, abstract = 
    '''
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    prettyHTML = soup.prettify()
    pageTitle = soup.find("h1", {"class": "ChapterTitle"})
    abstractParas = soup.findAll("p", {"class": "Para"})
    #authors = soup.findAll("span", {"class": "authors-affiliations__name"})
    pageNumbers = soup.find("span", {"class": "page-numbers-info"})
    keywords = soup.findAll("span", {"class": "Keyword"})
    citationCount = soup.find("span", {"class": "test-metric-count c-button-circle gtm-chaptercitations-count"})
    universities = soup.findAll("span", {"class": "affiliation__name"})
    conference = soup.find("span", {"data-test": "ConfSeriesName"})
    #print('title')
    pageTitleContents = pageTitle.contents[0]
    returnData.append(pageTitleContents)
    #print('PAGES: ')
    regexPages = r'(?!0|1$)\d{1,4}[-](?!0|1$)\d{1,4}'
    pages = re.search("(?!0|1$)\d{1,4}[-](?!0|1$)\d{1,4}", str(pageNumbers.contents[0])).group()
    #print(type(pages))
    returnData.append(pages)
    #print('KEYWORDS: ')
    if len(keywords) != 0: 
        for word in keywords: 
            authorKeywords += str(word.contents)[2:-6]
    else: 
        authorKeywords = 'NOT FOUND'
    #print(authorKeywords)
    returnData.append(authorKeywords)
    #print('CONFERENCE: ')
    if not conference:
        conferenceName = 'NOT FOUND'    
    else:
        conferenceName = conference.contents[0]
    returnData.append(conferenceName)
    #print('CITATIONS: ')
    if not citationCount:
        citations = '0'
    else: 
        citations = (str(citationCount.contents)[2:-2])
    #print(citations)
    returnData.append(citations)
    #print("UNIVERSITIES: ")
    for uni in universities: 
        uniList += str(uni.contents)[2:-2]
        uniList += '; '
    #print(uniList)
    returnData.append(uniList)
    #print('ABSTRACT: ')
    for para in abstractParas: 
        abstract += str(para.contents)[2:-2]
    #print(abstract)
    returnData.append(abstract)
    return returnData
