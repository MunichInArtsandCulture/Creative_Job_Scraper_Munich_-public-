# Creative_Job_Scraper_Munich_-public-

Overview
This project automatically collects and categorizes creative job offers in Munich using a custom-built web scraper. The scraped job listings are processed using AI and sent to a Telegram group.

Features

    Automated Data Collection – Scrapes job listings from various cultural job boards.
    AI-Powered Sorting – Jobs are categorized by field using an AI model.
    Telegram Integration – Sends job listings directly to a Telegram group.

Usage

    Download & Run Locally – The scraper cannot be executed directly on GitHub. Clone the repository and run it on your local machine.
    Execution – Run 0000ScraperTotal.py to start the scraping process.
    Optional Telegram Integration –
        By default, job listings are sent to a Telegram group.
        To disable this, remove the file job2telegram1.4.py from 0000ScraperTotal.py.
    Job Storage – Cleaned job listings are saved in categorized_jobs.txt.
    Free, Non-AI Option – You can also get an unprocessed list of jobs by running 00job_scraper_master2.5.py locally. Jobs will be saved in a text file named cooljobs.txt without AI categorization.
    AI API Key – Insert your OpenAI API key (or another AI provider’s key) into job_classifier1.3.py for job categorization.

Requirements
Ensure you have Python 3.x installed and install the following dependencies:

pip install openai aiogram requests beautifulsoup4 selenium urllib3 webdriver-manager regex
