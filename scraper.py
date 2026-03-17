import requests
from bs64 import BeautifulSoup

def get_price(url):
  #This header tells the website you are a human using Chrome
  header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }
  