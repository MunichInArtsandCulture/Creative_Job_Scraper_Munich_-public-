from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Setze den WebDriver (z. B. ChromeDriver)
driver = webdriver.Chrome()

# URL der Staatsoper Seite
url = "https://www.staatsoper.de/jobs/im-buero"

# Funktion zum Scrapen der Stellenangebote
def scrape_staatsoper_jobs(url):
    driver.get(url)
    time.sleep(3)  # Warte auf das Laden der Seite (3 Sekunden, je nach Internetgeschwindigkeit anpassen)

    # BeautifulSoup zur Analyse des HTMLs verwenden
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extrahiere alle Jobtitel anhand der span mit der Klasse "accordion__title-text"
    job_titles = soup.find_all('span', class_='accordion__title-text')
    jobs = []

    # Iteriere durch alle gefundenen Jobtitel
    for job in job_titles:
        title = job.get_text(strip=True)  # Jobtitel extrahieren
        link = url  # Setze den Quelllink zur Seite selbst
        jobs.append({'title': title, 'link': link})

    # Schließe den Browser
    driver.quit()

    # Gib die gefundenen Jobs zurück
    return jobs

# Starte das Scraping für Staatsoper
jobs = scrape_staatsoper_jobs(url)

# Zeige die gefundenen Jobs an
for job in jobs:
    print(f"Job Title: {job['title']}")
    print("Employer: Bayerische Staatsoper (Office)")
    print(f"Link: {job['link']}")
    print('---')
