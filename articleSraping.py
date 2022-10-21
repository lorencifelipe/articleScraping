import pandas as pd
from urllib.request import urlopen, urlretrieve
import os

def createPath(dir,name):
    path = os.path.join(dir,name)
    if not os.path.exists(path):
        os.mkdir(path)

def mkdirs(dir):
    createPath(dir,"ACM")
    createPath(dir,"BRAPCI")
    createPath(dir,"IEEE")

def prepareName(name):
    return name.replace("/","-")[:200] + ".pdf"

def acmProcedure(article, dir):
    pass

def ieeeProcedure(article, dir):
    pass

def brapciProcedure(article, dir):
    os.chdir(dir+"/BRAPCI")
    url = article["url"]
    title = article["title"]
    name = prepareName(title)
    if not os.path.exists(name):
        s = "https://brapci.inf.br/index.php/res/download/" #String pattern
        f = urlopen(url).read().decode("utf-8") #Crude html
        i = f.find(s) #S index in f
        downloadLink = ""
        if i > -1 or url == "":
            while(f[i]!= "'"):
                downloadLink+=f[i]
                i+=1
            urlretrieve(downloadLink, name)
            print("Downloaded file: " + name)
        else:
            with open("brapci.log","a") as file:
                file.write(url+"\n")
            print("Warning at: " + url)
    os.chdir(dir)

def main():
    dir = os.getcwd()
    mkdirs(dir)
    articles = pd.read_excel("articles_2.xls")
    for i in articles.index:
        if articles["status"][i] == "Accepted":
            if articles["source"][i][0] == "A":
                acmProcedure(articles.iloc[i],dir)
            elif articles["source"][i][0] == "B":
                brapciProcedure(articles.iloc[i],dir)
            elif articles["source"][i][0] == "I":
                ieeeProcedure(articles.iloc[i],dir)

main()