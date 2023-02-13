import customtkinter as ctk # to build GUI
import pyperclip as pc # to copy formatted citation to clipboard
import re # to split string using multiple delimiters
import os # to insert new line in a string

# types of Ctk widgets:
    # CTkLabel is a label
    # CTkButton is a button
    # CTkEntry is an entry field
    # CTkOptionMenu is a combo box: 
    # CTkCheckBox is a check box
    # CTkRadioButton is a radio button
    # CTkTextbox is a text box

dict = {} # create an empty dictionary to store and manipulate user inputs (author, title, etc.)

# set GUI color settings
ctk.set_appearance_mode("default") # or choose 'dark' or 'light'
ctk.set_default_color_theme("dark-blue")

# set GUI size
root = ctk.CTk() # create CTk root window
#root.geometry("500x700") # set window width and height
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# create text fields & buttons within GUI
label = ctk.CTkLabel(master=frame, text="Citation generator", font=("Roboto", 24)) # create label
#label.grid(row=0, column=0, columnspan=2, pady=3, padx=3)
label.pack(pady=3, padx=3) # show label
author1gui = ctk.CTkEntry(master=frame, placeholder_text="Author 1 name and surname (required)")
#author1gui.grid(row=0, column=1, pady=3, padx=3)
author1gui.pack(pady=3, padx=3)
author2gui = ctk.CTkEntry(master=frame, placeholder_text="Author 2 name and surname (required)")
author2gui.pack(pady=3, padx=3)
author3gui = ctk.CTkEntry(master=frame, placeholder_text="Author 3 name and surname (required)")
author3gui.pack(pady=3, padx=3)
author4gui = ctk.CTkEntry(master=frame, placeholder_text="Author 4 name and surname (required)")
author4gui.pack(pady=3, padx=3)
titlegui = ctk.CTkEntry(master=frame, placeholder_text="Title (required)")
titlegui.pack(pady=3, padx=3)
organisationgui = ctk.CTkEntry(master=frame, placeholder_text="Organisation (required)")
organisationgui.pack(pady=3, padx=3)
yeargui = ctk.CTkEntry(master=frame, placeholder_text="Year of publication (required)")
yeargui.pack(pady=3, padx=3)
monthgui = ctk.CTkEntry(master=frame, placeholder_text="Month (optional)")
monthgui.pack(pady=3, padx=3)
daygui = ctk.CTkEntry(master=frame, placeholder_text="Day (optional)")
daygui.pack(pady=3, padx=3)
checkbox = ctk.CTkCheckBox(master=frame, text="All authors in one line", onvalue="Yes", offvalue="No")
checkbox.pack(pady=3, padx=3)
submit_button = ctk.CTkButton(master=frame, text="Submit", command=lambda: login_func(dict, textbox, output_msg)) # Submit button
submit_button.pack(pady=3, padx=3)
clear_form_button = ctk.CTkButton(master=frame, text="Clear form", command=lambda: clear_form_func(dict)) # button to clear form
clear_form_button.pack(pady=3, padx=3)
output_msg = ctk.CTkLabel(master=frame, text='Your citation will appear here.', font=("Roboto", 10))
output_msg.pack(pady=1, padx=1)
textbox = ctk.CTkTextbox(master=frame, height=60, width=200, corner_radius=0)
textbox.pack(pady=3, padx=3)
clear_textbox_button = ctk.CTkButton(master=frame, text="Clear results", command=lambda: clear_textbox_func(dict, textbox)) # button to clear textbox/result
clear_textbox_button.pack(pady=3, padx=3)

# function to check if all required fields are filled in
def validation_func(dict):
    while any([dict['author1'] == "", dict['title'] == "", dict['organisation'] == "", dict['year'] == ""]):
        for x in ['author1', 'title', 'organisation', 'year']:
            if dict[x] == "":
                print("Please fill in all required fields.")
                dict[x] = str(input("Please enter " + x + ": "))
    #TODO add code to check if authors have both name and surname are filled in using split(" ") and using len() on the result to see if there are at least 2 items in that list
    return dict

# function to change month number to month name
def month_func(dict):
    if dict['month'] == "":
        dict['month_name'] = ""
    elif int(dict['month']) == 1:
        if dict['day'] == "":
            dict['month_name'] = "January"
        elif dict['day'] != 0:
            dict['month_name'] = "Jan."
    elif int(dict['month']) == 2:
        if dict['day'] == "":
            dict['month_name'] = "February"
        elif dict['day'] != 0:
            dict['month_name'] = "Feb."
    elif int(dict['month']) == 3:
        if dict['day'] == "":
            dict['month_name'] = "March"
        elif dict['day'] != 0:
            dict['month_name'] = "Mar."
    elif int(dict['month']) == 4:
        if dict['day'] == "":
            dict['month_name'] = "April"
        elif dict['day'] != 0:
            dict['month_name'] = "Apr."
    elif int(dict['month']) == 5:
        if dict['day'] == "":
            dict['month_name'] = "May"
        elif dict['day'] != 0:
            dict['month_name'] = "May"
    elif int(dict['month']) == 6:
        if dict['day'] == "":
            dict['month_name'] = "June"
        elif dict['day'] != 0:
            dict['month_name'] = "Jun."
    elif int(dict['month']) == 7:
        if dict['day'] == "":
            dict['month_name'] = "July"
        elif dict['day'] != 0:
            dict['month_name'] = "Jul."
    elif int(dict['month']) == 8:
        if dict['day'] == "":
            dict['month_name'] = "August"
        elif dict['day'] != 0:
            dict['month_name'] = "Aug."
    elif int(dict['month']) == 9:
        if dict['day'] == "":
            dict['month_name'] = "September"
        elif dict['day'] != 0:
            dict['month_name'] = "Sep."
    elif int(dict['month']) == 10:
        if dict['day'] == "":
            dict['month_name'] = "October"
        elif dict['day'] != 0:
            dict['month_name'] = "Oct."
    elif int(dict['month']) == 11:
        if dict['day'] == "":
            dict['month_name'] = "November"
        elif dict['day'] != 0:
            dict['month_name'] = "Nov."
    elif int(dict['month']) == 12:
        if dict['day'] == "":
            dict['month_name'] = "December"
        elif dict['day'] != 0:
            dict['month_name'] = "Dec."
    else:
        dict['month_name'] = "error"
    return dict

# function to loop through all authors, save them as surname followed by first name, then save to dict dictionary as 'author' key
def author_func(dict):
    if dict['multi_authors'] == "Yes": # when users input multiple names into 'author1' field, this will split them into individual authors, then save result into dictionary under dict['author']
        authors = re.split(r', and | and | & | , |, |,', str(dict['author1'])) # splits names using multiple delimiters (i.e. ' and ' ' & ' ' , ' etc)
        author = ""
        # swaps around names and surnames, then saves result into dictionary under dict['author']
        for x in authors:
            author = author + str(x).split(" ")[1] + ", " + str(x).split(" ")[0] + ", "
    else: # if a single author is entered in dict['author1'], then loops through all authors in author1, author2, author3 and author4
        author = ""
        # swaps around names and surnames, then saves result into dictionary under dict['author']
        for x in ['author1', 'author2', 'author3', 'author4']:
            if dict[x] != "":
                author = author + str(dict[x]).split(" ")[1] + ", " + str(dict[x]).split(" ")[0] + ", "
    dict['author'] = author[:-2] # remove last 2 characters from the 'author' string, then save it in 'dict' dictionary under 'author' key 
    return dict

# function to combine all user inputs and return it as a citation under 'combined_list' key in 'dict' dictionary
def combine_func(dict):
    combined_list = [] # create a list to store author, title, etc
    combined_list.append(dict['author'] + ". ")
    combined_list.append('"' + dict['title'] + '." ')
    combined_list.append(dict['organisation'] + ', ')
    if dict['day'] != "":
        combined_list.append(dict['month_name'] + " ")
    else:
        combined_list.append(dict['month_name'] + "")
    combined_list.append(dict['day'])
    combined_list.append(", " + dict['year'] + ".")
    dict['combined_list'] = "".join(combined_list) # convert list to string
    dict['combined_list'] = str(dict['combined_list']).replace(", ,", ",") # fixes issues where string contains ', ,' which happens if user doesn't enter month and day
    return dict

def copy_to_clipboard_func(dict):
    pc.copy(dict['combined_list'])

def clear_form_func(dict): # TODO no need to pass 'dict' to this function. No need to return 'dict' either
    author1gui.delete(0, 'end')
    author2gui.delete(0, 'end')
    author3gui.delete(0, 'end')
    author4gui.delete(0, 'end')
    titlegui.delete(0, 'end')
    organisationgui.delete(0, 'end')
    yeargui.delete(0, 'end')
    monthgui.delete(0, 'end')
    daygui.delete(0, 'end')
    checkbox.deselect()
    #dict = {}
    return dict

def clear_textbox_func(dict, textbox): # TODO no need to pass 'dict' to this function. No need to return 'dict' either
    textbox.delete("0.0", "end")
    return dict

def login_func(dict, textbox, output_msg):
    # save values inputted by user as variables
    dict['author1'] = author1gui.get()
    dict['author2'] = author2gui.get()
    dict['author3'] = author3gui.get()
    dict['author4'] = author4gui.get()
    dict['title'] = titlegui.get()
    dict['organisation'] = organisationgui.get()
    dict['year'] = str(yeargui.get())
    dict['month'] = str(monthgui.get())
    dict['day'] = str(daygui.get())
    dict['multi_authors'] = str(checkbox.get())

    # run functions
    dict = validation_func(dict) # checks if all required fields are filled in
    dict = month_func(dict) # adds letter name of the month to the dictionary
    dict = author_func(dict) # combines all authors into a single string with surname followed by first name
    dict = combine_func(dict) # combines all user inputs into a single string to show as a citation
    copy_to_clipboard_func(dict) # copies data from dict['combined_list'] to clipboard

    # output final result
    textbox.insert("end", text=str(dict['combined_list'] + os.linesep))
    output_msg.configure(text='Last formatted citation has been copied to clipboard.')



root.mainloop() # run the main customtkinter GUI loop endlessly

