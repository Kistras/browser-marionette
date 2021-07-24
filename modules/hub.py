#There's two functions that must be present in any module:
#  "defineFuncs", which will give you a function to switch modules after finishing
#     (they execute in order those funtion were called) and a function that will
#     execute other module immediately
#  "action", which will... do stuff when module is called. It might return whatever 
#     you want to use with "execute" function
#You are able to just use a bit of code below and this will work probably
from time import sleep

global queue, execute
queue = None
execute = None
def defineFuncs(queue_, execute_):
    global queue, execute
    queue = queue_
    execute = execute_

global first_launch
first_launch = True
def action(browser):
    global queue, execute

    global first_launch
    if first_launch:
        #Open url
        browser.get("https://commons.wikimedia.org/wiki/Main_Page")
        #Get monthly photo challenges
        browser.find_element_by_xpath("//div/span/a/span[@role='button']/b[contains(text(),'month')]").click()
        #Get and store participants
        pics = browser.find_elements_by_xpath("//li[@class='gallerybox']/div/div/div/a[@class='image']/img")
        for pic in pics:
            pic.click()
            sleep(0.5)
            #Click on download button
            browser.find_element_by_xpath("//div/a[@role='button'][contains(@original-title,'Download')]").click()
            #Quick hack to get an item
            while True:
                a = browser.find_elements_by_xpath("//a[contains(text(),'View in browser')]")
                if len(a) > 0:
                    print(a[0].get_attribute("href"))
                    break
            #Close
            browser.find_element_by_xpath("//div/button[contains(@original-title,'Close this')]").click()
            sleep(0.25)



    #queue("hub") #Queue itself after finishing
    first_launch = False
