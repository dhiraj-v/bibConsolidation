springerUrlPath = 'PATH TO SPRINGER LINKS SEPERATED BY ', ' in .txt file springerURLs.txt'
springerURLs = open(springerUrlPath, "r")
content = springerURLs.read()
springerList = content.split(", ")
print(len(springerList))
import pandas as pd
df = pd.DataFrame(columns = ['title', 'authors', 'university', 'year', 'pageCount',  'pages', 'citationCount', 'journal', 'volume', 'iseue', 'conference' 'keywords', 'abstract', 'bibtext']
i = 0
for url in springerList: 
    i += 1
    df_length = len(df)
    to_append = getSpringDetails(url) 
    df.loc[len(df)] = to_append
    print(i)
df.to_excel("OUTPUT PATH AS EXCEL FILE - allSpringer.xlsx")  
