from bs4 import BeautifulSoup
import requests
import pandas as pd

html_text = requests.get(
    "https://papyri.info/search?INT=on&DATE_MODE=LOOSE&DOCS_PER_PAGE=4000&LANG=grc"
).text
soup = BeautifulSoup(html_text, "lxml")
results = soup.find_all("tr", class_="result-record")
firstresult = soup.find("tr", class_="result-record")
# print(firstresult)
print(firstresult.find("td", class_="identifier"))
frame = pd.read_csv("dataset.csv")
# for result in results:
#     Identifier = result.find("")
# print(results)
# frame = pd.DataFrame(
#     columns=[
#         "Identifier",
#         "Location",
#         "Date",
#         "Languages",
#         "medium",
#         "transcription",
#         "translation",
#         "url",
#         "image_id",
#     ]
# )
# frame.to_csv("dataset.csv")
