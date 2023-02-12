import customtkinter as ctk

# build the GUI

ctk.set_appearance_mode("default") # or choose 'dark' or 'light'
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
#root.geometry("500x700")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Citation generator", font=("Roboto", 24))
label.grid(row=0, column=0, columnspan=2, pady=10)
label.pack(pady=12, padx=10)
author1gui = ctk.CTkEntry(master=frame, placeholder_text="Author 1 name and surname)")
author1gui.pack(pady=12, padx=10)
author2gui = ctk.CTkEntry(master=frame, placeholder_text="Author 2 name and surname)")
author2gui.pack(pady=12, padx=10)
author3gui = ctk.CTkEntry(master=frame, placeholder_text="Author 3 name and surname)")
author3gui.pack(pady=12, padx=10)
author4gui = ctk.CTkEntry(master=frame, placeholder_text="Author 4 name and surname)")
author4gui.pack(pady=12, padx=10)
titlegui = ctk.CTkEntry(master=frame, placeholder_text="Title")
titlegui.pack(pady=12, padx=10)
organisationgui = ctk.CTkEntry(master=frame, placeholder_text="Organisation")
organisationgui.pack(pady=12, padx=10)
yeargui = ctk.CTkEntry(master=frame, placeholder_text="Year of publication")
yeargui.pack(pady=12, padx=10)
monthgui = ctk.CTkEntry(master=frame, placeholder_text="Month")
monthgui.pack(pady=12, padx=10)
daygui = ctk.CTkEntry(master=frame, placeholder_text="Day (optional)")
daygui.pack(pady=12, padx=10)
checkbox = ctk.CTkCheckBox(master=frame, text="All authors in one line")
checkbox.pack(pady=12, padx=10)

dict = {} # create an empty dictionary to store and manipulate user inputs (author, title, etc.)

def login(dict):
    # save values inputted by user as variables
    dict['author1'] = author1gui.get()
    dict['author2'] = author2gui.get()
    dict['author3'] = author3gui.get()
    dict['author4'] = author4gui.get()
    dict['title'] = titlegui.get()
    dict['organisation'] = organisationgui.get()
    dict['year'] = str(yeargui.get())
    dict['month'] = int(monthgui.get())
    dict['day'] = str(daygui.get())
    # run functions
    dict = month_func(dict) # adds letter name of the month to the dictionary
    dict = author_func(dict) # combines all authors into a single string with surname followed by first name
    dict = combine_func(dict) # combines all user inputs into a single string to show as a citation
    # output final result
    output = ctk.CTkLabel(master=frame, text=dict['combined_list'], font=("Roboto", 10))
    output.pack(pady=12, padx=10)


# function to change month number to month name
def month_func(dict):
    if dict['month'] == 1:
        dict['month_name'] = "Jan."
    elif dict['month'] == 2:
        dict['month_name'] = "Feb."
    elif dict['month'] == 3:
        dict['month_name'] = "Mar."
    elif dict['month'] == 4:
        dict['month_name'] = "Apr."
    elif dict['month'] == 5:
        dict['month_name'] = "May."
    elif dict['month'] == 6:
        dict['month_name'] = "Jun."
    elif dict['month'] == 7:
        dict['month_name'] = "Jul."
    elif dict['month'] == 8:
        dict['month_name'] = "Aug."
    elif dict['month'] == 9:
        dict['month_name'] = "Sep."
    elif dict['month'] == 10:
        dict['month_name'] = "Oct."
    elif dict['month_name'] == 11:
        dict['month'] = "Nov."
    elif dict['month_name'] == 12:
        dict['month'] = "Dec."
    else:
        dict['month_name'] = "error"
    return dict

# function to loop through all authors, same them as surname followed by first name, then save to dict dictionary as 'author' key
def author_func(dict):
    author = ""
    for x in ['author1', 'author2', 'author3', 'author4']:
        if dict[x] != "":
            author = author + str(dict[x]).split(" ")[1] + ", " + str(dict[x]).split(" ")[0] + ", "
    dict['author'] = author[:-2] # remove last 2 characters from the string, then save it in 'dict' dictionary under 'author' key 
    return dict

# function to combine all user inputs and return it as a citation under 'combined_list' key in 'dict' dictionary
def combine_func(dict):
    combined_list = [] # create a list to store author, title, etc
    combined_list.append(dict['author'] + ". ")
    combined_list.append('"' + dict['title'] + '." ')
    if dict['day'] != "":
        combined_list.append(dict['month_name'] + " ")
    else:
        combined_list.append(dict['month_name'] + "")
    combined_list.append(dict['day'])
    combined_list.append(", " + dict['year'] + ".")
    dict['combined_list'] = "".join(combined_list) # convert list to string
    return dict

button = ctk.CTkButton(master=frame, text="Submit", command=lambda: login(dict))
button.pack(pady=12, padx=10)

root.mainloop() # run the main customtkinter GUI loop endlessly

