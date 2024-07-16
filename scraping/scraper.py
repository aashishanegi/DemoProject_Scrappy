import requests
from bs4 import BeautifulSoup
from database.db import insert_job_listing

def scrape_remoteok_jobs():
    base_url = "https://remoteok.com/remote-dev-jobs"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(base_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data from Remote OK. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    job_cards = soup.find_all('tr', class_='job')
    
    if not job_cards:
        print("No job cards found. Check the HTML structure or the URL parameters.")
        return
    
    for card in job_cards:
        title = card.find('h2', itemprop='title').get_text(strip=True)
        company = card.find('h3', itemprop='name').get_text(strip=True)
        location = "Remote"  # All jobs are remote
        salary = card.find('div', class_='salary')
        salary = salary.get_text(strip=True) if salary else 'N/A'
        requirements = card.find('div', class_='tags')
        requirements = ', '.join(tag.get_text(strip=True) for tag in requirements.find_all('span', class_='tag')) if requirements else 'N/A'
        apply_link = card.find('a', class_='preventLink')['href']
        apply_link = f"https://remoteok.com{apply_link}"
        
        job_details = {
            'title': title,
            'company': company,
            'location': location,
            'salary': salary,
            'requirements': requirements,
            'apply_link': apply_link
        }
        
        print(f"Inserting job: {job_details}")
        insert_job_listing(job_details)

def scrape_all_jobs():
    print("Starting to scrape jobs from Remote OK...")
    scrape_remoteok_jobs()
    print("Finished scraping jobs.")

if __name__ == "__main__":
    scrape_all_jobs()
