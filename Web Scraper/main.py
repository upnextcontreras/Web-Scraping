import time
from jobs import JobScraper  # Assuming JobScraper is in a file called 'jobs.py'

if __name__ == '__main__':
    scraper = JobScraper()  # Instantiate the JobScraper class
    scraper.get_unfamiliar_skill()  # Ask the user for the unfamiliar skill
    
    while True:
        scraper.find_jobs()  # Call the find_jobs method from the class
        
        # Ask if the user wants to exit
        if input("Do you want to exit? (y/n): ").lower() == "y":
            break
        else:
            time_wait = 10  # Set the wait time to 10 minutes
            print(f'Waiting {time_wait} minutes...')
            time.sleep(time_wait * 60)  # Sleep for the specified time before running again

            
