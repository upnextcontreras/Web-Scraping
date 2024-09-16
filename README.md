# Job Scraper

This is a simple job scraper tool that scrapes job postings from the TimesJobs website, filters out jobs based on a user-provided unfamiliar skill, and saves relevant job details to a text file.

## Features

- Scrapes job postings for Python-related jobs from the TimesJobs website.
- Allows the user to input a skill they are not familiar with, and filters out jobs that require that skill.
- Saves job details such as company name, required skills, and job links to a `.txt` file for each job found.

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/your-username/job-scraper.git
   cd job-scraper
```
Run the script:
   ```bash
   python main.py
```
## Files

- main.py: The main entry point of the program. It runs the job scraping process and asks the user if they want to exit.
- jobs.py: Contains the JobScraper class, which handles scraping jobs, filtering them by unfamiliar skill, and saving the results to files.

## Requirements

- Python 3.x
- BeautifulSoup4
- Requests

Install the required packages with:
```bash
pip install beautifulsoup4 requests
```
## Example Output
<img width="247" alt="WEB OUTPUT" src="https://github.com/user-attachments/assets/5c2a4a82-08f6-4edf-8316-7bf4b05214b3">

<img width="119" alt="JOB LIST" src="https://github.com/user-attachments/assets/56267528-1b65-4dc0-aabd-d3303ae979da">

## How It Works

- The JobScraper class fetches job listings from the TimesJobs website using requests and parses the HTML using BeautifulSoup.
- The user inputs a skill they are unfamiliar with, and the scraper filters out any jobs that list that skill.
- For each relevant job, the script saves the job details into a text file located in the job_postings directory.
