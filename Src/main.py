import re
import csv
import requests
from bs4 import BeautifulSoup
import os


def ScrapingAWSDocument():
    re_delete_indent = re.compile(r'\n +')
    base_url = "https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/"
    target_url = "https://docs.aws.amazon.com/ja_jp/config/latest/developerguide/managed-rules-by-aws-config.html"
    r = requests.get(target_url)
    r.encoding = 'utf-8'

    soup = BeautifulSoup(r.text, 'lxml')
    link_list = soup.find(id="main-col-body").find_all("li")

    rules = []
    for child in link_list:
        child_url = base_url + child.get('a').get("href")[2:]
        r2 = requests.get(child_url)
        r2.encoding = 'utf-8'
        soup2 = BeautifulSoup(r2.text, 'lxml')
        detail = soup2.find(id="main-col-body").p.text.strip()
        detail = re_delete_indent.sub(' ', detail)
        rules.append(
            {
                'rule_name': soup2.h1.text,
                'rule_detail': detail,
                "url": child_url
            }
        )
    return rules


def cd():
    os.chdir(os.path.dirname(__file__))


if __name__ == "__main__":
    cd()
    # rules =
