
import names


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import html2text

import bs4
CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
CHROMEDRIVER_PATH = 'C:/Program Files/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )
driver = webdriver.Chrome('C:/Program Files/chromedriver')
h = html2text.HTML2Text()
def scraper(job_title):
    #job_title="fashion designer" #hardcoded for now
    job_split = job_title.split()
    job_title = job_title.replace(' ', '%20')
    driver.get('https://www.livecareer.com/resume-search/search?jt='+job_title)
    content = driver.page_source
    soup = bs4.BeautifulSoup(content, 'lxml')
    links= []
    for link in soup.findAll('a'):
        if(link.has_attr('href')):
            for k in job_split:
                if(k.lower() in link['href']):
                    links.append('https://www.livecareer.com'+link['href'])
                    print('https://www.livecareer.com'+link['href'])

    for link in links:
        driver.get(link)
        elem = driver.find_element_by_id('document')
        resume = h.handle(elem.get_attribute('innerHTML')).encode('utf-8')
        #insert saving code here


scraper('Python Developer')