import pandas as pd
from urllib.request import urlopen
import os

def acmProcedure(article):
    pass

def brapciProcedure(article):
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
        print(url)
        print(downloadLink)


def ieeeProcedure(article):
    pass

def main():
    articles = pd.read_excel("articles.xls")
    for i in articles.index:
        if articles["status"][i] == "Accepted":
            if articles["source"][i][0] == "A":
                acmProcedure(articles.iloc[i])
            elif articles["source"][i][0] == "B":
                brapciProcedure(articles.iloc[i])
            elif articles["source"][i][0] == "I":
                ieeeProcedure(articles.iloc[i])

main()