import random
import string
import time
import json
from selenium import webdriver

def get_sites():
    alphabets = string.ascii_lowercase
    website = "https://www.drugs.com/alpha/"
    sites = []
    for i in alphabets:
        sites.append(website + i + ".html")

def get_drugs_links_to_json(sites):
    driver = webdriver.Chrome('D:/PythonProjects/chromedriver.exe')
    drugs = {}
    for site in sites:
        driver.get(site)
        print("Site opend")
        time.sleep(2)
        ul = driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul')
        lists = ul.find_elements_by_tag_name("li")
        for li in lists:
            med = li.text
            link = (li.find_element_by_tag_name('a')).get_attripbute("href")
            drugs[med] = link
            # print(med,link)
        print("*************done with {} site*********".format(site))
        time.sleep(random.randint(2, 5))
    driver.close()
    with open('drugs_data.json', 'w') as fp:
        json.dump(drugs, fp)

def get_drug_info():
    driver = webdriver.Chrome('D:/PythonProjects/chromedriver.exe')
    f = open('drugs_data.json', )
    data = json.load(f)
    med_info = {}
    for i in data:
        path = str(data[i])
        print(path)
        driver.get(path)
        ul = driver.find_element_by_xpath('//*[@id="content"]/div[2]')
        time.sleep(5)
        x = ([my_elem.text for my_elem in ul.find_elements_by_css_selector("h2")])
        ul2 = driver.find_element_by_xpath('html/body')
        y = ul2.text
        med_info[i] = ((y.split(x[0]))[1].split(x[1])[0])
        print("Data done for ", i)
        time.sleep(random.randint(2, 5))
    for key in med_info:
        med_info[key] = med_info[key].strip('\n')
    with open('med_info.json', 'w') as fp:
        json.dump(med_info, fp)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sites=get_sites()
    print("links scraped")
    get_drugs_links_to_json(sites)
    print("drugs scarped")
    get_drug_info()
    print("drugs information scaraped")




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
