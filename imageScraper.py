from bs4 import BeautifulSoup
import requests


html_text = requests.get(
    "https://papyri.info/apis/berkeley.apis.2294?rows=3&start=220&fl=id,title&fq=(images-int:true)&fq=facet_language:grc&sort=series+asc,volume+asc,item+asc&p=221&t=3676"
).text
firstpage = BeautifulSoup(html_text, "lxml")
pngurl = firstpage.find("div", id="image").find("h2").find("a")["href"]
secondpage = BeautifulSoup(requests.get(pngurl).text, "lxml")
finalurl = secondpage.find("select", id="images")

print(finalurl)
