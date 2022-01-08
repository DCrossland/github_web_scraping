Top Repositories for GitHub Topics

Pick a website and describe your objective
Browse through different sites and pick on to scrape. Check the "Project Ideas" section for inspiration.
Identify the information you'd like to scrape from the site. Decide the format of the output CSV file.
Summarize your project idea and outline your strategy in a Juptyer notebook. Use the "New" button above.
Project Outline:
- Scrape https://github.com/topics
- Get list of topics. For each topic we'll extract topic, title, URL, description
- For each topic we'll get the top 25 repositories in the toic from the topic page
- For each repository, we'll pull repo name, username, stars and repo URL 
- For each toic we'll create a CSV file in the following formate:

Repo Name, Username, Stars, Repo URL
!pip install requests --upgrade --quiet
import requests
topics_url = 'https://github.com/topics'
response = requests.get(topics_url)
Check URL runs correctly

response.status_code
200
Count characters of output

len(response.text)
174248
page_contents = response.text
show first 1000 characters

page_contents[:1000]
'\n\n<!DOCTYPE html>\n<html lang="en" data-color-mode="auto" data-light-theme="light" data-dark-theme="dark">\n  <head>\n    <meta charset="utf-8">\n  <link rel="dns-prefetch" href="https://github.githubassets.com">\n  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">\n  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">\n  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">\n  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>\n  <link rel="preconnect" href="https://avatars.githubusercontent.com">\n\n\n\n  <link crossorigin="anonymous" media="all" integrity="sha512-E9wnWjoxQmh5A1jiWVYDPKOvA8VPf0iKQYoc+9ycMJvtAi9gOSlaUci+W2smxFIlWkV8hkX+O27S8NIB59iIDw==" rel="stylesheet" href="https://github.githubassets.com/assets/light-13dc275a3a314268790358e25956033c.css" /><link crossorigin="anonymous" media="all" integrity="sha512-nYSv3KrFhMlGUpjkFQBLMEN6HvHhijcoubQLjV3DWlcABEi2yDYf6KGUjRubJ5R+dJnKXR7jA4wu5Dg200SApA==" rel="s'

Use the requests library to download web pages
Inspect the website's HTML source and identify the right URLs to download.
Download and save web pages locally using the requests library.
Create a function to automate downloading for different topics/search queries.
Save webpage as file

with open ('webpage.html', 'w') as f:
    f.write(page_contents)
Use Beautiful Soup to parse and extract information
Parse and explore the structure of downloaded web pages using Beautiful soup.
Use the right properties and methods to extract the required information.
Create functions to extract from the page into lists and dictionaries.
(Optional) Use a REST API to acquire additional information if required.
!pip install beautifulsoup4 --upgrade --quiet
from bs4 import BeautifulSoup
Tell BS we are looking at htl

doc = BeautifulSoup(page_contents, 'html.parser')
doc

Select elements from webpage by rightclick on element and selecting inspect

selection_class = 'f3 lh-condensed mb-0 mt-1 Link--primary'
topic_title_tags = doc.find_all('p', {'class':selection_class})
len = count elements

len(topic_title_tags)
30
Show top 5 elements

topic_title_tags[:5]
[<p class="f3 lh-condensed mb-0 mt-1 Link--primary">3D</p>,
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Ajax</p>,
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Algorithm</p>,
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Amp</p>,
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Android</p>]
topic_title_tag0 = topic_title_tags[0]
topic_title_tag0
<p class="f3 lh-condensed mb-0 mt-1 Link--primary">3D</p>
Descriptions of topics

desc_selector = 'f5 color-fg-muted mb-0 mt-1'

topic_desc_tags = doc.find_all('p', {'class': desc_selector})
topic_desc_tags[:5]
[<p class="f5 color-fg-muted mb-0 mt-1">
           3D modeling is the process of virtually developing the surface and structure of a 3D object.
         </p>,
 <p class="f5 color-fg-muted mb-0 mt-1">
           Ajax is a technique for creating interactive web applications.
         </p>,
 <p class="f5 color-fg-muted mb-0 mt-1">
           Algorithms are self-contained sequences that carry out a variety of tasks.
         </p>,
 <p class="f5 color-fg-muted mb-0 mt-1">
           Amp is a non-blocking concurrency library for PHP.
         </p>,
 <p class="f5 color-fg-muted mb-0 mt-1">
           Android is an operating system built by Google designed for mobile devices.
         </p>]
div_tag = topic_title_tag0.parent
div_tag

Find parent of div for topic https link - search for class class 'a' from inspecting webpage as div parent not returning correct code

topic_link_tags = doc.find_all ('a', {'class': 'no-underline flex-1 d-flex flex-column'})
topic https link for topic 0

topic_link_tags[0]['href']
'/topics/3d'
top 5 topic https link tags

topic_link_tags[:5]
[<a class="no-underline flex-1 d-flex flex-column" href="/topics/3d">
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">3D</p>
 <p class="f5 color-fg-muted mb-0 mt-1">
           3D modeling is the process of virtually developing the surface and structure of a 3D object.
         </p>
 </a>,
 <a class="no-underline flex-1 d-flex flex-column" href="/topics/ajax">
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Ajax</p>
 <p class="f5 color-fg-muted mb-0 mt-1">
           Ajax is a technique for creating interactive web applications.
         </p>
 </a>,
 <a class="no-underline flex-1 d-flex flex-column" href="/topics/algorithm">
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Algorithm</p>
 <p class="f5 color-fg-muted mb-0 mt-1">
           Algorithms are self-contained sequences that carry out a variety of tasks.
         </p>
 </a>,
 <a class="no-underline flex-1 d-flex flex-column" href="/topics/amphp">
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Amp</p>
 <p class="f5 color-fg-muted mb-0 mt-1">
           Amp is a non-blocking concurrency library for PHP.
         </p>
 </a>,
 <a class="no-underline flex-1 d-flex flex-column" href="/topics/android">
 <p class="f3 lh-condensed mb-0 mt-1 Link--primary">Android</p>
 <p class="f5 color-fg-muted mb-0 mt-1">
           Android is an operating system built by Google designed for mobile devices.
         </p>
 </a>]
Create https link to topic

topic0_url = "https://github.com" + topic_link_tags[0]['href']
print(topic0_url)
https://github.com/topics/3d
Get topic titles text

topic_titles = []
for tag in topic_title_tags:
    topic_titles.append(tag.text.strip())
    
print(topic_titles)
['3D', 'Ajax', 'Algorithm', 'Amp', 'Android', 'Angular', 'Ansible', 'API', 'Arduino', 'ASP.NET', 'Atom', 'Awesome Lists', 'Amazon Web Services', 'Azure', 'Babel', 'Bash', 'Bitcoin', 'Bootstrap', 'Bot', 'C', 'Chrome', 'Chrome extension', 'Command line interface', 'Clojure', 'Code quality', 'Code review', 'Compiler', 'Continuous integration', 'COVID-19', 'C++']

topic_descs = []
for tag in topic_desc_tags:
    topic_descs.append(tag.text.strip())
 topic_descs[:5]
['3D modeling is the process of virtually developing the surface and structure of a 3D object.',
 'Ajax is a technique for creating interactive web applications.',
 'Algorithms are self-contained sequences that carry out a variety of tasks.',
 'Amp is a non-blocking concurrency library for PHP.',
 'Android is an operating system built by Google designed for mobile devices.']
Base URL + element https link

topic_urls = []
base_url = 'https://github.com'

for tag in topic_link_tags:
    topic_urls.append(base_url + tag['href'])

topic_urls
['https://github.com/topics/3d',
 'https://github.com/topics/ajax',
 'https://github.com/topics/algorithm',
 'https://github.com/topics/amphp',
 'https://github.com/topics/android',
 'https://github.com/topics/angular',
 'https://github.com/topics/ansible',
 'https://github.com/topics/api',
 'https://github.com/topics/arduino',
 'https://github.com/topics/aspnet',
 'https://github.com/topics/atom',
 'https://github.com/topics/awesome',
 'https://github.com/topics/aws',
 'https://github.com/topics/azure',
 'https://github.com/topics/babel',
 'https://github.com/topics/bash',
 'https://github.com/topics/bitcoin',
 'https://github.com/topics/bootstrap',
 'https://github.com/topics/bot',
 'https://github.com/topics/c',
 'https://github.com/topics/chrome',
 'https://github.com/topics/chrome-extension',
 'https://github.com/topics/cli',
 'https://github.com/topics/clojure',
 'https://github.com/topics/code-quality',
 'https://github.com/topics/code-review',
 'https://github.com/topics/compiler',
 'https://github.com/topics/continuous-integration',
 'https://github.com/topics/covid-19',
 'https://github.com/topics/cpp']
Create CSV file(s) with the extracted information
Create functions for the end-to-end process of downloading, parsing, and saving CSVs.
Execute the function with different inputs to create a dataset of CSV files.
Verify the information in the CSV files by reading them back using Pandas.
https://www.youtube.com/watch?v=RKsLLG-bzEY 52.30

!pip install pandas --quiet
Import pandas as 'pd'

import pandas as pd
Create dataframe topics dictionary = topics_dict

topics_dict = {
    'title': topic_titles,
    'description': topic_descs,
    'url':topic_urls}
df= data frame. Use https://www.geeksforgeeks.org/create-a-pandas-dataframe-from-lists/ for more information and alternatives

topics_df = pd.DataFrame(topics_dict)
topics_df

topics_df.to_csv('topics.cvs')
Remove indexing

topics_df.to_csv('topics.cvs', index=None)
Document and share your work
 
Add proper headings and documentation in your Jupyter notebook.
Publish your Jupyter notebook to your Jovian profile
(Optional) Write a blog post about your project and share it onli
!pip install jovian --upgrade
Requirement already satisfied: jovian in /opt/conda/lib/python3.9/site-packages (0.2.41)
Requirement already satisfied: requests in /opt/conda/lib/python3.9/site-packages (from jovian) (2.27.0)
Requirement already satisfied: pyyaml in /opt/conda/lib/python3.9/site-packages (from jovian) (5.4.1)
Requirement already satisfied: click in /opt/conda/lib/python3.9/site-packages (from jovian) (8.0.1)
Requirement already satisfied: uuid in /opt/conda/lib/python3.9/site-packages (from jovian) (1.30)
Requirement already satisfied: idna<4,>=2.5 in /opt/conda/lib/python3.9/site-packages (from requests->jovian) (3.1)
Requirement already satisfied: certifi>=2017.4.17 in /opt/conda/lib/python3.9/site-packages (from requests->jovian) (2021.5.30)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/conda/lib/python3.9/site-packages (from requests->jovian) (1.26.7)
Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/conda/lib/python3.9/site-packages (from requests->jovian) (2.0.0)
import jovian
# Execute this to save new versions of the notebook
jovian.commit(project="scraping-github-topics-repositories")
getting information out of a topic page
topic_page_url = topic_urls[0]
topic_page_url
response = requests.get(topic_page_url)
check response code

response.status_code
len(response.text)
topic_doc = BeautifulSoup(response.text, 'html.parser')
h3_selection_class = 'f3 color-fg-muted text-normal lh-condensed'
repo_tags = topic_doc.find_all('h3', {'class': h3_selection_class})
len(repo_tags)
repo_tags[0]
a_tags = repo_tags[0].find_all('a')
repo_tags[0]
a_tags[0].text
strip to return clear text

a_tags[0].text.strip()
a_tags[1].text.strip()
base_url = 'https:github.com'
repo_url = base_url + a_tags[1]['href']
print(repo_url)
star_tags = topic_doc.find_all('span', {'class': 'Counter js-social-count'})

len(star_tags)
star_tags[0]
star_tags[0].text.strip()
stars_str = '77'
stars_str[-1]
stars_str[:-1]
float(stars_str[:-1]) * 1000
int(float(stars_str[:-1]) * 1000)
Convert star string to interger, strip if last character is k remove float everything before the k and multiply by 10000 (k) and return as interger else return interger of stars string

def parse_star_count(stars_str):
    stars_str = stars_str.strip()
    if stars_str[-1]== 'k':
       return int(float(stars_str[:-1]) * 1000)
    return int(stars_str)
int(stars_str)
parse_star_count(star_tags[0].text.strip())
def get_repo_info(h3_tag, star_tag):
    #returns all the required info about a repository
    a_tags = h3_tag.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    repo_url = base_url + a_tags[1]['href']
    stars = parse_star_count(star_tag.text.strip())
    return username, repo_name, stars, repo_url
get_repo_info(repo_tags[0], star_tags[0])
range(len(repo_tags))
topic_repos_dict = {
    'username': [],
    'repo_name': [],
    'stars' : [],
    'repo_url': []
    
}

for i in range(len(repo_tags)) :
    repo_info = get_repo_info(repo_tags[i], star_tags[i])
    
    topic_repos_dict['username'].append(repo_info[0])
    topic_repos_dict['repo_name'].append(repo_info[1])
    topic_repos_dict['stars'].append(repo_info[2])
    topic_repos_dict['repo_url'].append(repo_info[3])
    
topic_repos_df = pd.DataFrame(topic_repos_dict)
topic_repos_df
Define function to get repo info for all topics

def get_topic_page(topic_url):
    #Download the page
    response = requests.get(topic_url)
    #Check successful response
    if response.status_code != 200:
        raise Exception('Failed to load page {}'.format(topic_url))
    #Parse using Beautiful Soup
    topic_doc = BeautifulSoup(response.text, 'html.parser')
    return topic_doc

def get_repo_info(h3_tag, star_tag):
    #returns all the required info about a repository
    a_tags = h3_tag.find_all('a')
    username = a_tags[0].text.strip()
    repo_name = a_tags[1].text.strip()
    repo_url = base_url + a_tags[1]['href']
    stars = parse_star_count(star_tag.text.strip())
    return username, repo_name, stars, repo_url

def get_topic_repos(topic_doc):
      
    #Get h3 tags containing repo title, repo URL and username 
    h3_selection_class = 'f3 color-fg-muted text-normal lh-condensed'
    repo_tags = topic_doc.find_all('h3', {'class': h3_selection_class})
    
    #GEt start tags
    star_tags = topic_doc.find_all('span', {'class': 'Counter js-social-count'})
    
    #Create dictionary
    topic_repos_dict = {
    'username': [],
    'repo_name': [],
    'stars' : [],
    'repo_url': []
    }   
    
    #Get repo info
    for i in range(len(repo_tags)):
        repo_info = get_repo_info(repo_tags[i], star_tags[i])
        topic_repos_dict['username'].append(repo_info[0])
        topic_repos_dict['repo_name'].append(repo_info[1])
        topic_repos_dict['stars'].append(repo_info[2])
        topic_repos_dict['repo_url'].append(repo_info[3])
    
    return pd.DataFrame(topic_repos_dict)
url4 = topic_urls[4]
topic4_doc = get_topic_page(url4)
url4
len(topic4_doc)
topic4_repos = get_topic_repos(topic4_doc)
topic4_repos
Tidy code up

get_topic_repos(get_topic_page(topic_urls[4]))
topic_urls[5]
get_topic_repos(get_topic_page(topic_urls[5]))
Save to cvs

get_topic_repos(get_topic_page(topic_urls[5])).to_csv('angular.csv', index=None)
Write a single function to : 1. Get the list of topics from the topic pages 2. Get the list of top repos from the individual topic pages 3. For each topic, create a CSV of the top repos for the topic
