from bs4 import BeautifulSoup
import requests
import os

class JobScraper:
    def __init__(self):
        self.unfamiliar_skill = ''
        self.base_dir = os.path.join(os.getcwd(), 'job_postings')
        # Ensure the job_postings directory exists
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def get_unfamiliar_skill(self):
        self.unfamiliar_skill = input('Put some skill you are not familiar with\n> ')
        print(f'Filtering out {self.unfamiliar_skill}')

    # list(map(int, input('Put some skill you are not familiar with\n> ').split()))

    # x = list(map(int, input("Enter multiple values: ").split()))
    # print("List of students: ", x)



    def find_jobs(self):
        # Make the request to the website
        html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

        # Loop through jobs and filter by unfamiliar skill
        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
                skills = job.find('span', class_='srp-skills').text.replace(' ', '')
                more_info = job.header.h2.a['href']

                # If the unfamiliar skill is not in the job's required skills
                if self.unfamiliar_skill not in skills:
                    self.save_job(index, company_name, skills, more_info)

    def save_job(self, index, company_name, skills, more_info):
        # Save the job details to a text file
        file_path = os.path.join(self.base_dir, f'{index}.txt')
        with open(file_path, 'w') as f:
            f.write(f'Company Name: {company_name.strip()} \n')
            f.write(f'Required Skills: {skills.strip()} \n')
            f.write(f'More info: {more_info}\n')
        print(f'File saved: {index}')