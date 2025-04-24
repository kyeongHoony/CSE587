import os
import json
import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

save_dir = "isca_data"
os.makedirs(save_dir, exist_ok=True)
save_path = os.path.join(save_dir, "isca_abstracts.json")

def get_isca_papers_from_dblp(year):
    url = f"https://dblp.org/db/conf/isca/isca{year}.html"
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    papers = []
    for entry in soup.find_all("cite", class_="data"):
        title_tag = entry.find("span", class_="title")
        acm_anchor = entry.find("a", title="Electronic edition @ACM Digital Library")
        if title_tag and acm_anchor:
            papers.append({
                "year": year,
                "title": title_tag.get_text(),
                "acm_url": acm_anchor['href']
            })
    return papers

def get_abstract_from_acm(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        html = requests.get(url, headers=headers, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")
        abstract_div = soup.find("div", class_="abstractSection abstractInFull")
        if abstract_div:
            return abstract_div.get_text(strip=True)
        else:
            return None
    except Exception as e:
        print(f" Failed to fetch abstract from {url}: {e}")
        return None

all_papers = []
for year in range(2023, 2025):  
    print(f"\n Processing ISCA {year}...")
    papers = get_isca_papers_from_dblp(year)
    for paper in tqdm(papers):
        abstract = get_abstract_from_acm(paper["acm_url"])
        paper["abstract"] = abstract
        time.sleep(1.0)  
    all_papers.extend(papers)

with open(save_path, "w", encoding="utf-8") as f:
    json.dump(all_papers, f, indent=2, ensure_ascii=False)

print(f"\n Abstracts saved to: {save_path}")