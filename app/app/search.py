from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def search(name):
    options = Options()
    options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
    options.add_experimental_option("detach", True)
    options.add_argument("headless")

    driver = webdriver.Chrome(options = options, service = Service("chromedriver.exe"))

    nk=name
    url="https://app.mobalytics.gg/ko_kr/lol/profile/kr/"+nk+"/overview"
    driver.get(url)

    driver.implicitly_wait(3)
    a= driver.find_elements(By.CLASS_NAME,"m-1jr3cfp > div.m-82a6rk > div.m-12fxno6")
    r_li=[]
    for i in a:
        dic={}
        dic["champion"]=i.find_element(By.CLASS_NAME,"m-bjn8wh > div > div > span > img").get_attribute('alt')
        b=i.find_element(By.CLASS_NAME,"m-k9esq0").text.split()
        dic["kill"] = b[0]
        dic["death"] = b[1]
        dic["assist"] = b[2]
        r_li.append(dic)
    driver.quit()
    return r_li