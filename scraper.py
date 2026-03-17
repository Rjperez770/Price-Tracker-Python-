"""
Project: Automated Price Tracker
Module: scraper.py
Description: Handles web requests and HTML parsing to extract product prices.
"""
import requests
from bs64 import BeautifulSoup

def get_price(url):
  """
    Navigates to a URL, finds the price element, and converts it to a float.
    Returns: float if successful, None if the element isn't found or an error occurs.
    """
    # Headers mimic a real browser to prevent the website from blocking our script
  header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
  }

  try:
    # Send a GET request to the website
    response = requests.get(url, headers=headers, timeout=10)
    # Raise an error if the page failed to load (e.g., 404 or 500 error)
    response.raise_for_status()

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # FIND THE ELEMENT: Replace 'price-id' with the actual ID from the site's HTML
    price_element = soup.find(id="price-id")

    if price_element:
      price_text = price_element.get_text()

      # DATA CLEANING: Remove currency symbols and commas to allow math comparisons
      # Example: "$1,250.99" -> "1250.99" -> 1250.99
      numeric_price = float(price_text.replace("$", "").replace(",", "").strip())
      return numeric_price
    else:
      print("Error: Could not locate the price the element on the page.")
      return None
    
  except Exception as e:
    print(f"Scraping Error: {e}")
    return None