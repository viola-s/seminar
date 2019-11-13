# Installation:
# Download a browser driver of your choice:
# Firefox	https://github.com/mozilla/geckodriver/releases
# Chrome	http://chromedriver.chromium.org/downloads
# Internet Explorer	https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver
# Microsoft Edge	https://blogs.windows.com/msedgedev/2015/07/23/bringing-automated-testing-to-microsoft-edge-through-webdriver/


# pip install selenium

import time
from selenium import webdriver

def executeSelenium(url):
    # Invoke a new Firefox Instance
    chrome_driver = webdriver.Chrome()

    # Blocking wait of 30 seconds in order to locate the element
    chrome_driver.implicitly_wait(30)
    chrome_driver.maximize_window()

    # Open the required page
    chrome_driver.get(url)

    # Sleep for 10 seconds in order to see the results
    time.sleep(10)

    # Close the Browser instance
    chrome_driver.close()


def executeSeleniumAdavnced(url):
    # open browser and demonstrate inspect
    # copy xpath

    mainHeadlineXpath   = '//*[@id="F_Content"]/div/div[3]/div[1]/div[1]/div[1]'
    secondHeadlineXpath = '//*[@id="F_Content"]/div/div[3]/div[1]/div[1]/div[2]'
    genericHeadlineXpath = '//*[@id="F_Content"]/div/div[3]/div[1]/div[1]/div[{}]'
    titleXpath       = '//*[@id="F_Content"]/div/div[3]/div[1]/div[1]/div[{}]/div/div[2]/a/div/div[1]'
    descriptionXpath = '//*[@id="F_Content"]/div/div[3]/div[1]/div[1]/div[{}]/div/div[2]/a/div/div[2]'
    start = 1

    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(30)
    chrome_driver.maximize_window()
    chrome_driver.get(url)

    data = list()

    while(True):
        try:
            print("####")
            titleElem = chrome_driver.find_element_by_xpath(titleXpath.format(start))
            print(titleElem.text)
            descriptionElem =chrome_driver.find_element_by_xpath(descriptionXpath.format(start))
            print(descriptionElem.text)
            data.append({"title": titleElem.text, "description": descriptionElem.text})
            start += 1
        except Exception as e:
            break

    chrome_driver.close()


if __name__ == "__main__":
    url = "https://www.ynet.co.il"
    executeSelenium(url)
    #executeSeleniumAdavnced(url)
