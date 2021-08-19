#Web scrapping to get lastest mookit lectures data
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
usernameText = input("Enter your username: ")
passwordText = input("Enter your password: ")
course = input("Enter the course code: ")
n = int(input("Enter the number of lectures to be scraped: "))
driver = webdriver.Chrome()

driver.get('https://hello.iitk.ac.in/index.php/user/login')
actions = ActionChains(driver)
username = driver.find_element_by_class_name('username')
password  = driver.find_element_by_class_name('password')
actions.click(on_element=username).send_keys(usernameText)
actions.click(on_element=password).send_keys(passwordText)
login = driver.find_element_by_name('op')
actions.click(on_element=login).perform()
try:
    url = 'https://hello.iitk.ac.in/'+course+'21/'
    driver.get(url)
    c = driver.page_source
    soup = BeautifulSoup(c,'lxml')
    lec_names = []
    weeks = []
    links = []
    durations = []
    wItem = soup.findAll('div',{'class':'weekItem'})
    wDetails = soup.findAll('div',{'class':'weekDetailsBox'})
    for i in range(len(wItem)):
        lecs = wDetails[i].findAll('div',{'class':'lectureInfoBoxText'})

        week = wItem[i].find('div',{'class':'weekWrapper'}).text.strip()
        dur = wDetails[i].findAll('div',{'class':'lectureInfoBoxLength'})
        
        for l,t in zip(lecs, dur):
            durations.append(t.text.strip())
            weeks.append(week)
            lec_names.append(l.text.strip())
            links.append(url+l.find_parent('a').get('href'))

    df = pd.DataFrame({'Lecture Name':lec_names,'Length':durations, 'Link':links})
    df.index = weeks
    if(n>len(df)):
        n = len(df)
    df = df[len(weeks)-n:len(weeks)+1]
    df.to_csv(course+'_'+str(n)+'.csv')

except(Exception):
    print("Error occured!")
finally:
    driver.close()




