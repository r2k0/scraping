import urllib
import re

urls = ["http://finance.yahoo.com","http://google.com/finance"]

regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

for u in urls:
    htmlfile = urllib.urlopen(u)
    htmltext = htmlfile.read()
    titles = re.findall(pattern,htmltext)
    print titles
