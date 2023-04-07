
import webbrowser   # used to open chrome

import keyboard     # used to copy
import pyperclip    # used to paste into python strings
import time         # used to make the program wait for loading and whatnot before executing more code
import selenium     # used to navigate google chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# def launchChrome:
# # replace url with the page you want to start copying from
url = "https://boxnovel.com/novel/forty-millenniums-of-cultivation/chapter-1/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
driver.get('https://boxnovel.com/novel/forty-millenniums-of-cultivation/chapter-1/')
time.sleep(1)
driver.maximize_window()


# returns true if the "Next" button is present on the current page
def isPresent(driver_, className):
    if (driver_.find_elements(By.CLASS_NAME, className).size() > 0):
        return True
    else:
        return False
# while isPresent(driver, "Next")


# copy and paste
time.sleep(3)
keyboard.press_and_release("ctrl + a")
time.sleep(1)
keyboard.press_and_release("ctrl + c")
time.sleep(1)


# paste this chapter into a string
chapter = pyperclip.paste()
chapter = chapter.splitlines()


# click to the next chapter
button = driver.find_element(By.LINK_TEXT, "Next")
# button = driver.find_element(By.CLASS_NAME, "btn next_page")
button.click()

# delete text before chapter begins
x = 0
y = 0
while y < 2:
    if "Chapter" in chapter[x]:
        y = y + 1
    del chapter[x]


# if you try deleting elements from a list of size 10 by iterating through the list a number of times == the size of the list, you'll end up trying to access indices outside the list.
# my solution is to append the value of i to another list whenever you've found an element that you want to delete. Then, iterate through the new list backwards (so you don't cause the same problem as above)
# and delete the items in chapter[] like this: del chapter[otherlist[j]]
deleteIndexLiist = []
# iterate through each line and censor
for i in range(0, len(chapter)):
    # censoring:
    if "****" in chapter[i]:
        chapter[i] = chapter[i].replace("****", "replace with this text")


    # every add starts with "Sponsored by..." and is 7 lines in total; this code appends the indices to be deleted to deleteIndexList
    if "Sponsored" in chapter[i]:
        deleteIndexLiist.append(i)
        deleteIndexLiist.append(i + 1)
        deleteIndexLiist.append(i + 2)
        deleteIndexLiist.append(i + 3)
        deleteIndexLiist.append(i + 4)
        deleteIndexLiist.append(i + 5)
        deleteIndexLiist.append(i + 6)

# delete
i = len(deleteIndexLiist) - 1
while i >= 0:
    del chapter[deleteIndexLiist[i]]
    i = i - 1


# delete the extra text after the end of the chapter
i = len(chapter) - 1
while "Thank you for reading on myboxnovel.com" not in chapter[i]:
    del chapter[i]
    i = i - 1
if "Thank you for reading on myboxnovel.com" in chapter[i]:
    del chapter[i]

for i in range(0, len(chapter)):
    print(chapter[i])











