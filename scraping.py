from fpdf import FPDF
import names
from time import sleep

from cleanDataset import cleanResume

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import html2text
import bs4

CHROME_PATH = '/Users/revathi/Library/Application Support/Google/Chrome/Default'
CHROMEDRIVER_PATH = '/Users/revathi/chromedriver'
WINDOW_SIZE = "1920,1080"

#chrome requirements
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

#pdf requirements
pdf = FPDF()

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options)
# driver = webdriver.Chrome('C:/Program Files/chromedriver')
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
                    # print('https://www.livecareer.com'+link['href'])
    for link in links:
        driver.get(link)
        elem = driver.find_element_by_id('document')
        resume = h.handle(elem.get_attribute('innerHTML')).encode('utf-8')
        resume = resume.decode('utf-8')
        resume = cleanResume(resume)

        pdf.add_page()
        pdf.set_font("Arial",size=12)
        pdf.cell(200, 10, txt=resume, ln=1)

        name = names.get_full_name()
        pdf.output('resumes/' + name +'.pdf')


# scraper('Python Developer')
