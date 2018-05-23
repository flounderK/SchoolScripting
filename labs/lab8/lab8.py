import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u",
                    "--url",
                    help="The url you would like to scrape",
                    required=True)

args = parser.parse_args()

url = args.url
s = requests.session()
r = s.get(url)
soup = BeautifulSoup(r.content, "lxml")
scripts = soup.find_all("script")
