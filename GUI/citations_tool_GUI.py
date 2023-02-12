import customtkinter as ctk # to build GUI
import pyperclip as pc # to copy formatted citation to clipboard
import re # to split string using multiple delimiters

dict = {} # create an empty dictionary to store and manipulate user inputs (author, title, etc.)

# set GUI color settings
ctk.set_appearance_mode("default") # or choose 'dark' or 'light'
ctk.set_default_color_theme("dark-blue")

# set GUI size
root = ctk.CTk()
#root.geometry("500x700")
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# create text fields & buttons within GUI
label = ctk.CTkLabel(master=frame, text="Citation generator", font=("Roboto", 24))
#label.grid(row=0, column=0, columnspan=2, pady=10)
label.pack(pady=12, padx=10)
author1gui = ctk.CTkEntry(master=frame, placeholder_text="Author 1 name and surname (required)")
author1gui.pack(pady=12, padx=10)
author2gui = ctk.CTkEntry(master=frame, placeholder_text="Author 2 name and surname (required)")
author2gui.pack(pady=12, padx=10)
author3gui = ctk.CTkEntry(master=frame, placeholder_text="Author 3 name and surname (required)")
author3gui.pack(pady=12, padx=10)
author4gui = ctk.CTkEntry(master=frame, placeholder_text="Author 4 name and surname (required)")
author4gui.pack(pady=12, padx=10)
titlegui = ctk.CTkEntry(master=frame, placeholder_text="Title (required)")
titlegui.pack(pady=12, padx=10)
organisationgui = ctk.CTkEntry(master=frame, placeholder_text="Organisation (required)")
organisationgui.pack(pady=12, padx=10)
yeargui = ctk.CTkEntry(master=frame, placeholder_text="Year of publication (required)")
yeargui.pack(pady=12, padx=10)
monthgui = ctk.CTkEntry(master=frame, placeholder_text="Month (optional)")
monthgui.pack(pady=12, padx=10)
daygui = ctk.CTkEntry(master=frame, placeholder_text="Day (optional)")
daygui.pack(pady=12, padx=10)
checkbox = ctk.CTkCheckBox(master=frame, text="All authors in one line", onvalue="Yes", offvalue="No")
checkbox.pack(pady=12, padx=10)

# function to check if all required fields are filled in
def validation_func(dict):
    while any([dict['author1'] == "", dict['title'] == "", dict['organisation'] == "", dict['year'] == ""]):
        for x in ['author1', 'title', 'organisation', 'year']:
            if dict[x] == "":
                print("Please fill in all required fields.")
                dict[x] = str(input("Please enter " + x + ": "))
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

# function is only activated when user selects "Yes" in multi_authors tickbox in customtkinter GUI. This function won't work in here.
def multi_author_selector_func(dict):
    dict['multi_authors'] == "Yes"
    return dict

# when users input multiple names into 'author1' field, this funciton will split them into individual authors, then save result into dictionary under dict['author']
def multi_author_func(dict):
    if dict['multi_authors'] == "Yes":
        authors = re.split(r', and | and | & | , |, |,', str(dict['author1'])) # splits names using multiple delimiters (i.e. ' and ' ' & ' ' , ' etc)
        author = ""
        # swaps around names and surnames, then saves result into dictionary under dict['author']
        for x in authors:
            author = author + str(x).split(" ")[1] + ", " + str(x).split(" ")[0] + ", "
        dict['author'] = author[:-2] # remove last 2 characters from the 'author' string, then save it in 'dict' dictionary under 'author' key 
    return dict

# function to loop through all authors, same them as surname followed by first name, then save to dict dictionary as 'author' key
def author_func(dict):
    if dict['multi_authors'] == "Yes": # if multiple authors are entered in dict['author1'], then launches multi_author_func to parse those authors
        dict = multi_author_func(dict)
    else: # if a single author is entered in dict['author1'], then loops through all authors
        author = ""
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

def copy_to_clipboard(dict):
    pc.copy(dict['combined_list'])

def login(dict):
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
    copy_to_clipboard(dict) # copies data from dict['combined_list'] to clipboard
    # output final result
    output = ctk.CTkLabel(master=frame, text=dict['combined_list'], font=("Roboto", 10))
    output.pack(pady=4, padx=3)
    output = ctk.CTkLabel(master=frame, text='Your formatted citation has been copied to clipboard.', font=("Roboto", 10))
    output.pack(pady=1, padx=1)

button = ctk.CTkButton(master=frame, text="Submit", command=lambda: login(dict))
button.pack(pady=12, padx=10)

root.mainloop() # run the main customtkinter GUI loop endlessly

