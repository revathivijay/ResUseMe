from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import html2text
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


import bs4
# CHROME_PATH = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
# CHROMEDRIVER_PATH = 'C:/Program Files/chromedriver'
# WINDOW_SIZE = "1920,1080"
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# chrome_options.binary_location = CHROME_PATH
#
# driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
#                           chrome_options=chrome_options
#                          )
# h = html2text.HTML2Text()
driver = webdriver.Chrome('C:/Program Files/chromedriver')
delay = 4
def findingSkills(job_title):
    driver.get('https://www.linkedin.com/login')
    time.sleep(20)
    #job_title="fashion designer" #hardcoded for now
    job_split = job_title.split()

    job_title = job_title.replace(' ', '%20')
    url = "https://www.google.dz/search?q=site:linkedin.com/in/%20"+job_title
    driver.get(url)
    content = driver.page_source
    soup = bs4.BeautifulSoup(content, 'lxml')
    links= []
    for link in soup.findAll('a'):
        if(link.has_attr('href')):
            if('https://in.linkedin.com/in/' in link['href']):
               links.append(link['href'])

    for i in range(1):
        driver.get(links[0])
        content = driver.page_source
        soup = bs4.BeautifulSoup(content, 'lxml')

        temp = soup.prettify()
        with open('some_file.txt', 'w', encoding="utf-8") as f:
            f.write(temp)
        # print (soup.find(id='bpr-guid-585975'))
        # # element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'pv-skill-category-entity__name-text ')))
        # # print(element.text)



findingSkills('Web Developer')