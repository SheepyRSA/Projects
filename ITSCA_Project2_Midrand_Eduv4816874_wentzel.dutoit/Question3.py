# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 09:59:04 2024

@author: Wentz
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
 
baseUrl = "https://www.careerjunction.co.za/"

print('Which job position would you like to look for?\n')
jobSearch = input(str())
print('\n')
repoJob = jobSearch.replace(' ', '+')
csvTitle = jobSearch.replace(' ', '_')
nextPageUrl = baseUrl + 'jobs/results?keywords='+ repoJob +'&autosuggestEndpoint=%2Fautosuggest&location=0&category=&btnSubmit=+'
response = requests.get(nextPageUrl)  

if response.status_code == 200:
    pageContent = response.text
    soup = BeautifulSoup(pageContent,'html.parser')
    listAllJobs = soup.findAll('div', class_='module job-result')
    data = {
    'Title': [],
    'Recruiter': [],
    'Salary': [],
    'Position': [],
    'Location': [],
    'Date Posted': [],
    }
    
    for job in listAllJobs:
        title = job.find('h2').find('a').text.strip() if job.find('h2') else ''
        recruiter = job.find('h3').find('a').text.strip() if job.find('h3') else ''
        salary_elem = job.find('li', class_='salary') if job.find('li', class_='salary') else None
        salary = salary_elem.text.strip() if salary_elem else ''
        position_elem = job.find('li', class_='position') if job.find('li', class_='position') else None
        position = position_elem.text.strip() if position_elem else ''
        location_elem = job.find('li', class_='location').find('a') if job.find('li', class_='location') else None
        location = location_elem.text.strip() if location_elem else ''
        datePosted_elem = job.find('li', class_='updated-time') if job.find('li', class_='updated-time') else None
        datePosted = datePosted_elem.text.strip() if datePosted_elem else ''
        
        data['Title'].append(title if title else '')
        data['Recruiter'].append(recruiter if recruiter else '')
        data['Salary'].append(salary if salary else '')
        data['Position'].append(position if position else '')
        data['Location'].append(location if location else '')
        data['Date Posted'].append(datePosted if datePosted else '')
        print(data)        
else:
    print("Failed to get the page. Statsu code: " + response.status_code)

table = pd.DataFrame(data, columns=['Title', 'Recruiter', 'Salary', 'Position', 'Location', 'Date Posted'])
table.index = table.index + 1
table.to_csv(f'search_term_{csvTitle}.csv', sep=';', encoding='utf-8', index=False)
print(table)

"BeutifulSoup tutorial Accessed online 17/06/2024: https://letslearnabout.net/python/beautiful-soup/your-first-web-scraping-script-with-python-beautiful-soup/"