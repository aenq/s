#
# Stack Overflow questions scraper
#

# Libraries
import json
import requests
from bs4 import BeautifulSoup

# Base url
start_url = 'https://stackoverflow.com/questions?tab=newest&page='

# Loop over Stack Overflow questions pages
for page_num in range(1, 10):
    # get next page url
    url = start_url + str(page_num)
    
    # HTTP GET request to the given url
    response = requests.get(start_url)
    # parse content
    content = BeautifulSoup(response.text, 'lxml')

    # extract question links
    links = content.findAll('a', {'class' : 's-link'})
    description = content.findAll('div', {'class': 's-post-summary--content-excerpt'})

    # extract question description
    print('\n\nURL:', url)

    # loop over Stack Overflow question list
    for index in range(0, len(description)):
        # store items in dict
        question = {
            'title': links[index].text,
            'url': links[index]['href'],
            'description': description[index].text.strip().replace('\n', '')
        }

        print(json.dumps(question, indent=2))