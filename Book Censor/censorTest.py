
import webbrowser   # used to open chrome
import keyboard     # used to copy
import pyperclip    # used to paste into python strings
import time         # used to make the program wait for loading and whatnot before executing more code

from selenium import webdriver # used to navigate google chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import tkinter as tk    # used to created the GUI


# GUI start

# Create a function to be called when the user presses the Enter key
def on_enter(event):
    # retrieve the text from the widget
    book = bookEntry.get()
    url  = urlEntry.get()
    numChapters = int(chapEntry.get())

    print(book)
    print(url)
    print(numChapters)

# create the main window
window = tk.Tk(screenName = "BoxNovel Censor")

# create a label for Book name
label = tk.Label(text = "Book name:")
label.pack()

# create a keyboard input widget and pack it into the window
bookEntry = tk.Entry(window)
bookEntry.pack()

# bind the "<Return>" key event to the on_enter function
bookEntry.bind('<Return>', on_enter)


# URL
label = tk.Label(window, text = "First Chapter's URL:")
label.pack()

urlEntry = tk.Entry(window)
urlEntry.pack()
urlEntry.bind("<Return>", on_enter)

# num of chapters
label = tk.Label(window, text = "Number of Chapters:")
label.pack()

chapEntry = tk.Entry(window)
chapEntry.pack()
chapEntry.bind("<Return>", on_enter)

# Create two buttons and place them in the window using absolute coordinates
def runButtonFunc():
    global book, url, numChapters
    book = bookEntry.get()
    url  = urlEntry.get()
    numChapters = int(chapEntry.get())

    window.destroy() # close the window, and continue on with the code after mainloop

runButton = tk.Button(window, text = "Run Program", command = runButtonFunc)
runButton.place(x = 600, y = 150)

# run the Tkinter event loop
window.mainloop()

# GUI end

# Chrome start, copy/paste chapters

# url = "https://boxnovel.com/novel/forty-millenniums-of-cultivation/chapter-1/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = options)
driver.get(url)
time.sleep(1)
driver.maximize_window()
# driver.execute_script("document.body.style.zoom='50%'")   # changes the zoom of the window; I hoped this would make it so I could click on stuff even if pop-ups appear, but for some reason it didn't click anything when I did this
time.sleep(1)
driver.execute_script("window.scrollTo(0, 250)")


# returns true if the "Next" button is present on the current page
def isPresent(driver_, xPath):
    elements = driver_.find_elements(By.XPATH, xPath)
    numElements = len(elements)
    if numElements > 0:
        return True
    if numElements == 0:
        return False

def countList(lst): # get the number of lists in a list of lists
    return len(lst)

# def censorText(delete, replace, a, b):
#     if delete in chapter_list[a][b]:
#         chapter_list[a][b] = chapter_list[a][b].replace(delete, replace)

# this code clicks through the chapters and copies them
chapter_list = [] # this will be a list of lists; the inner list is made up of each line in the chapter; each element in the outer list represents a chapter
# while isPresent(driver, "Next"):
numChapters = numChapters - 1
x = 0
while x < numChapters:
    # copy and paste
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 250)")
    time.sleep(1)
    keyboard.press_and_release("ctrl + a")
    time.sleep(0.5)
    keyboard.press_and_release("ctrl + c")
    time.sleep(0.5)


    # paste this chapter into a string
    content = pyperclip.paste()
    chapter = content.splitlines()
    chapter_list.append(chapter)
    time.sleep(0.5)

    if x == 0: # the "Next" button is different for Chapter 1 than all the other chapters
        # click to the next chapter
        button = driver.find_element(By.XPATH, '//*[@id="manga-reading-nav-head"]/div/div[3]/div/div/a') # not full XPATH
        button.click()
    if x > 0:
        # click to the next chapter
        button = driver.find_element(By.XPATH, '//*[@id="manga-reading-nav-head"]/div/div[3]/div/div[2]/a') # not full XPATH
        button.click()
    
    x = x + 1
# copy and paste the last chapter without trying to click "Next"
time.sleep(1)
driver.execute_script("window.scrollTo(0, 250)")
time.sleep(1)
keyboard.press_and_release("ctrl + a")
time.sleep(1)
keyboard.press_and_release("ctrl + c")
time.sleep(0.5)


# paste this chapter into a string
content = pyperclip.paste()
chapter = content.splitlines()
chapter_list.append(chapter)


# for k in range(len(chapter_list)):
#     # delete text before chapter begins
#     # x = 0
#     # y = 0
#     # while y < 2:
#     #     if "Chapter" in chapter_list[k][1]:
#     #         y = y + 1
#     #     if "Chapter" not in chapter_list[k][1]:
#     #         del chapter_list[k][1]

#     t = True
#     while t == True:
#         chapter_list[k][0]
#         if "Chapter" in chapter_list[k][0]:
#             t == False



for k in range(len(chapter_list)):

    # if you try deleting elements from a list of size 10 by iterating through the list a number of times == the size of the list, you'll end up trying to access indices outside the list.
    # my solution is to append the value of i to another list whenever you've found an element that you want to delete. Then, iterate through the new list backwards (so you don't cause the same problem as above)
    # and delete the items in chapter[] like this: del chapter[otherlist[j]]
    deleteIndexList = []

    x = 0
    while x < len(chapter_list[k]):
        if "Chapter" not in chapter_list[k][x]:
            deleteIndexList.append(x)
        if "Chapter" in chapter_list[k][x]:
            break

    # iterate through each line and censor
    for i in range(0, len(chapter_list[k])):
        # censoring:
        if "****" in chapter_list[k][i]:
            chapter_list[k][i] = chapter_list[k][i].replace("****", "replace with this text")


        # every add starts with "Sponsored by..." and is 7 lines in total; this code appends the indices to be deleted to deleteIndexList
        if "Sponsored" in chapter_list[k][i]:
            deleteIndexList.append(i)
            deleteIndexList.append(i + 1)
            deleteIndexList.append(i + 2)
            deleteIndexList.append(i + 3)
            deleteIndexList.append(i + 4)
            deleteIndexList.append(i + 5)
            deleteIndexList.append(i + 6)
        
        # sometimes this text appears on a line by itself, so delete it (add to delete list)
        if "boxn ovel. c0m" in chapter_list[k][i]:
            deleteIndexList.append(i)

    # delete
    i = len(deleteIndexList) - 1
    while i >= 0:
        del chapter_list[k][deleteIndexList[i]]
        i = i - 1


    # delete the extra text after the end of the chapter
    i = len(chapter_list[k]) - 1
    while "Thank you for reading on myboxnovel.com" not in chapter_list[k][i]:
        del chapter_list[k][i]
        i = i - 1
    if "Thank you for reading on myboxnovel.com" in chapter_list[k][i]:
        del chapter_list[k][i]

    for i in range(0, len(chapter_list[k])):
        print(chapter_list[k][i])


with open(book, "w", encoding = 'utf-8') as file: # "with open" will automatically close the file after the code block inside the "with open" statement has executed
    for k in range(0, len(chapter_list)):
        file.write("\n\n\n\n")
        for i in range(0, len(chapter_list[k])):
            file.write(chapter_list[k][i])
            file.write("\n")











