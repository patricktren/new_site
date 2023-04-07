import tkinter as tk

# create the main window
window = tk.Tk(screenName = "BoxNovel Censor") # screenName does what? it doen't appear to change the window name..

# create a label for Book name
label = tk.Label(text = "Book name:")
label.pack()

# create a keyboard input widget and pack it into the window
bookEntry = tk.Entry(window)
bookEntry.pack()

# Create a function to be called when the user presses the Enter key
def on_enter(event):
    # retrieve the text from the widget
    book = bookEntry.get()
    url  = urlEntry.get()
    numChapters = chapEntry.get()
    print(book, "\n", url, "\n", numChapters)

# bind the "<Return>" key event to the on_enter function
bookEntry.bind('<Return>', on_enter)


# URL
label = tk.Label(window, text = "URL:")
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



# run the Tkinter event loop
window.mainloop()