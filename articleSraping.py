import pandas as pd
from urllib.request import urlopen, urlretrieve
import os

def acmProcedure(article, dir):
    pass

def brapciProcedure(article, dir):
    os.chdir(dir+"/BRAPCI")
    url = article["url"]
    title = article["title"]
    s = "https://brapci.inf.br/index.php/res/download/" #String pattern
    f = urlopen(url).read().decode("utf-8") #Crude html
    i = f.find(s) #S index in f
    downloadLink = ""
    if i > -1:
        while(f[i]!= "'"):
            downloadLink+=f[i]
            i+=1
        urlretrieve(downloadLink,title+".pdf") #MUST TRUNCATE NAME TO FIT IN TITLE + FILTER <sup> tag
       # print(url)
       # print(downloadLink)
    os.chdir(dir)


def ieeeProcedure(article, dir):
    pass

def main():
    dir = os.getcwd()
    articles = pd.read_excel("articles.xls")
    for i in articles.index:
        if articles["status"][i] == "Accepted":
            if articles["source"][i][0] == "A":
                acmProcedure(articles.iloc[i],dir)
            elif articles["source"][i][0] == "B":
                brapciProcedure(articles.iloc[i],dir)
            elif articles["source"][i][0] == "I":
                ieeeProcedure(articles.iloc[i],dir)

main()