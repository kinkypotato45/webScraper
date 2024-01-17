from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get(
    "https://papyri.info/search?INT=on&DATE_MODE=LOOSE&DOCS_PER_PAGE=4000&LANG=grc"
).text
soup = BeautifulSoup(html_text, "lxml")
# results = soup.find_all("tr", class_="result-record")
results = soup.find_all("tr", class_="result-record")
frame = pd.read_csv("dataset.csv")
imageid = 0
for result in results:
    id = result.find("td", class_="identifier")
    # print(id)
    url = result.find("a")["href"]
    location = result.find("td", class_="display-place").text
    date = result.find("td", class_="display-date").text
    language = result.find("td", class_="language").text

    identifier = id["title"]
    if identifier in frame["Identifier"].values:
        continue
    df = {
        "Identifier": identifier,
        "Location": location,
        "Date": date,
        "Languages": language,
        "medium": "",
        "transcription": "",
        "translation": "",
        "url": "https://papyri.info" + url,
        "image_id": str(imageid),
    }
    imageid += 1
    frame = frame._append(df, ignore_index=True)
    # frame.reset_index()

    # print(identifier)
    # print(url)
    # print(location)
    # print(date)
    # print(language)

print(frame)
frame.to_csv("dataset.csv", index=False)
