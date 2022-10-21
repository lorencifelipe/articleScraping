from urllib.request import urlopen
import os

url = 'https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8485200'
webFile = urlopen(url)
print(webFile.read())