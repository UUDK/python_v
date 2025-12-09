import requests
import bs4
from pathlib import PosixPath as Path


def scrape_example_quotes_toscrape_com(
    url: str = "http://quotes.toscrape.com/",
) -> str:
    """Fetch and parse the title of a webpage."""
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    quote = soup.find('div', class_='quote').find('span', class_='text').get_text(strip=True)
    return quote

def scrape_example_quotes_toscrape_com_with_selenium():
    """Fetch and parse the title of a webpage using Selenium."""
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = Service()  # Adjust path to Chrome driver if necessary
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get("http://quotes.toscrape.com/js/")
        quote_element = driver.find_element(By.CLASS_NAME, 'quote').find_element(By.CLASS_NAME, 'text')
        quote = quote_element.text.strip()
    finally:
        driver.quit()

    return quote
if __name__ == "__main__":
    print(scrape_example_quotes_toscrape_com())
    print(scrape_example_quotes_toscrape_com_with_selenium())