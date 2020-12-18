import pandas as pd
#urls = ['https://link.springer.com/chapter/10.1007/978-3-319-94496-8_10', 'https://link.springer.com/chapter/10.1007/978-3-319-94496-8_10']
import pandas as pd
df = pd.DataFrame(columns = ['title', 'pages', 'keywords', 'conference', 'citations', 'univ', 'abstract'])
i = 0
for url in springerList: 
    i += 1
    df_length = len(df)
    to_append = extractDetailSpringer(url) 
    df.loc[len(df)] = to_append
    print(i)
df.to_excel("/content/drive/MyDrive/Tech/IIIT/SecurityVisualizationSLR/output.xlsx")  
#df.to_csv('/content/drive/MyDrive/Tech/IIIT/SecurityVisualizationSLR/data.csv')
#df.head()
