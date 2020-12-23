from bs4 import BeautifulSoup
import re
import requests
    #   COMMON: title(citation_title), author(citation_author), pages(citation_firstpage, citation_lastpage), University (citation_author_institution), Year (citation_publication_date), organization/publisher(citation_publisher)
    #   Article: journal(citation_journal_title), volume(citation_volume), number(citation_issue), citationCount: 
    #   Conference, Chapter: booktitle(citation_conference_title), CiteCount(chaptercitations-count-number)
def getSpringDetails(url):
    springDetails = []
    journal = 'journal NA'
    volume = 'volume NA'
    issue = 'issue NA'
    book = 'book NA'
    authorList = ''
    authorKeywords = ''
    abstract = ''
    bibtex = ''
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    prettyHTML = soup.prettify()
    pageTitle = soup.find("meta", {"name": "citation_title"})
    title = (pageTitle['content'])
    firstPage = soup.find("meta", {"name": "citation_firstpage"})
    firstPageNumber = (firstPage['content'])
    lastPage = soup.find("meta", {"name": "citation_lastpage"})
    lastPageNumber = (lastPage['content'])
    pageCount = int(lastPageNumber) - int(firstPageNumber) + 1
    pageRange = firstPageNumber + "-" + lastPageNumber
    authors = soup.findAll("meta", {"name": "citation_author"})
    university = soup.find("meta", {"name": "citation_author_institution"})
    univ = (university['content'])
    publicationYear = soup.find("meta", {"name": "citation_publication_date"})
    year = (publicationYear['content'])
    publishedBy = soup.find("meta", {"name": "citation_publisher"})
    publisher = (publishedBy['content'])
    if '/article/' in url:
        keywords = soup.findAll("span", {"class": "c-article-subject-list__subject"})    
        #citations = soup.find("meta", {"name": ""})
        #citeCount = (citations['content'])
        journalName = soup.find("meta", {"name": "citation_journal_title"})
        journal = (journalName['content'])
        journalVolume = soup.find("meta", {"name": "citation_volume"})
        volume = (journalVolume['content'])
        journalIssue = soup.find("meta", {"name": "citation_issue"})
        issue = (journalIssue['content'])
        abstractParas = soup.find("meta", {"property": "og:description"})
        abstract = (abstractParas['content'])
        citationFetching = soup.findAll("li", {"class": "c-article-metrics-bar__item"})
        for lst in citationFetching:
            print('------------------')
            print(str(lst)) 
    elif '/chapter/' in url: 
        citations = soup.find("span", {"id": "chaptercitations-count-number"})
        citeCount = citations.contents[0]
        keywords = soup.findAll("span", {"class": "Keyword"})
        bookTitle = soup.find("meta", {"name": "citation_conference_title"})
        book = (bookTitle['content'])
        abstractParas = soup.findAll("p", {"class": "Para"})
        for para in abstractParas: 
            abstract += str(para.contents)[2:-2]
    #springDetails.append(title)
    if len(keywords) != 0: 
        for word in keywords: 
            authorKeywords += str(word.contents)[2:-6]
    else: 
        authorKeywords = 'Keywords NOT FOUND'
    if len(authors) != 0: 
        for author in authors: 
            authorList += author['content']
            authorList += '; '
    else: 
        authorList = 'Authors NOT FOUND'
    if '/article/' in url:

    elif '/chapter/' in url: 
        bibtex = '@inproceedings{' + 
    print(title)
    print(pageCount)
    print(pageRange)
    print(univ)
    print(year)
    print(publisher)
    print(authorKeywords)
    print(authorList)
    print(journal)
    print(volume)
    print(issue)
    print(book)
    print(abstract)

print('== Chapter ==')
getSpringDetails('https://link.springer.com/chapter/10.1007/978-3-319-94496-8_10')
print('== Article ==')
getSpringDetails('https://link.springer.com/article/10.1007/s11227-015-1543-4')
print("== Conf Paper ==")
getSpringDetails('https://link.springer.com/chapter/10.1007/978-0-387-35515-3_4')
