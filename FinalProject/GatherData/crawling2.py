import os
import json
import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException

import undetected_chromedriver as uc
from bs4 import BeautifulSoup
import time

def get_abstract_with_undetected_chrome(url):
    try:
        options = uc.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = uc.Chrome(options=options)
        driver.get(url)

        time.sleep(8)  
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        abstract_div = soup.find("div", class_="abstractSection abstractInFull")
        if abstract_div:
            return abstract_div.get_text(strip=True)

        meta_abstract = soup.find("meta", attrs={"property": "og:description"})
        if meta_abstract and meta_abstract.get("content"):
            return meta_abstract["content"]

        section_abstract = soup.find("section", id="abstract")
        if section_abstract:
            paragraphs = section_abstract.find_all("div", attrs={"role": "paragraph"})
            return "\n".join([p.get_text(" ", strip=True) for p in paragraphs])

        return None

    except Exception as e:
        print(f"[undetected-chromedriver] Failed to fetch abstract from {url}: {e}")
        return None

def convert_doi_to_acm_url(doi_url):
    if doi_url.startswith("https://doi.org/"):
        return doi_url.replace("https://doi.org", "https://dl.acm.org/doi")
    return doi_url

save_dir = "ISCA_data"
os.makedirs(save_dir, exist_ok=True)

def get_papers_from_dblp(year):
    url = f"https://dblp.org/db/conf/isca/isca{year}.html"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    papers = []
    for entry in soup.find_all("li", class_="entry inproceedings"):
        title_tag = entry.find("span", class_="title")
        if not title_tag:
            continue
        title = title_tag.text

        pdf_url = None
        for link in entry.find_all("a"):
            href = link.get("href", "")
            if "doi.org" in href or "acm.org" in href or "ieee.org" in href:
                pdf_url = href
                break
        papers.append({
            "title": title,
            "paper_url": pdf_url
        })
        print(pdf_url)

    return papers
  
def get_abstract_from_acm(url):
    return get_abstract_with_undetected_chrome(url)

target_years = [2023]

for year in target_years:  # ISCA 2007~2012
    all_papers = []
    print(f"\n📘 Processing ISCA {year}...")
    papers = get_papers_from_dblp(year)
    for paper in tqdm(papers[70:]):
        print(f"Processing: {paper['paper_url']}")
        abstract = get_abstract_from_acm(paper["paper_url"])
        paper["abstract"] = abstract
        time.sleep(1.0)  
    all_papers.extend(papers[70:])

    save_path = os.path.join(save_dir, f"isca_{year}_revised_abstracts.json")

# ✅ JSON으로 저장
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(all_papers, f, indent=2, ensure_ascii=False)

    print(f"\n Abstracts saved to: {save_path}")