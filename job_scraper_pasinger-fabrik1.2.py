from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Webdriver-Setup
driver = webdriver.Chrome()

# Ziel-URL
url = "https://pasinger-fabrik.de/die-fabrik/stellenausschreibungen/"

# Funktion zum Scrapen der Jobs
def scrape_pasinger_fabrik_jobs(url):
    driver.get(url)
    time.sleep(3)  # Warten, bis die Seite geladen ist

    # HTML-Quelle analysieren
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Alle h2-Elemente mit strong innerhalb suchen
    job_titles = soup.find_all("h2")
    jobs = []

    for h2 in job_titles:
        strong = h2.find("strong")  # Das strong-Tag innerhalb jedes h2 finden
        if strong:
            title = strong.get_text(strip=True)  # Jobtitel extrahieren und Leerzeichen entfernen
            if title:  # Nur hinzufügen, wenn der Titel nicht leer ist
                link = url  # Der Link zur Website bleibt derselbe
                jobs.append({"title": title, "link": link})

    # Browser schließen
    driver.quit()

    return jobs

# Scraping starten
jobs = scrape_pasinger_fabrik_jobs(url)

# Ergebnisse ausgeben
for job in jobs:
    print(f"Job Title: {job['title']}")
    print("Employer: Pasinger Fabrik")
    print(f"Link: {job['link']}")
    print("---")
