# capture user inputs
author1 = input("enter author's full name (name and surname)")
author2 = input("enter author's full name (name and surname)")
author3 = input("enter author's full name (name and surname)")
author4 = input("enter author's full name (name and surname)")
title = input("enter title")
organisation = input("enter name of organisation")
year = input("enter year of publication")
month = int(input("enter month of publication as a number"))
day = input("enter day of publication")

authors_list = [author1, author2, author3, author4] # to store all authors in a list

# function to change month number to month name
def month_func(month):
    if month == 1:
        month = "Jan."
    elif month == 2:
        month = "Feb."
    elif month == 3:
        month = "Mar."
    elif month == 4:
        month = "Apr."
    elif month == 5:
        month = "May."
    elif month == 6:
        month = "Jun."
    elif month == 7:
        month = "Jul."
    elif month == 8:
        month = "Aug."
    elif month == 9:
        month = "Sep."
    elif month == 10:
        month = "Oct."
    elif month == 11:
        month = "Nov."
    elif month == 12:
        month = "Dec."
    else:
        month = "error"
    return month

# function to loop through all authors and change order from name followed by surname to surname followed by name 
def author_func(authors_list):
    author = ""
    for x in authors_list:
        if x != "":
            author = author + str(x).split(" ")[1] + ", " + str(x).split(" ")[0] + ", "
    author = author[:-2] # remove last 2 characters from the string
    return author

# function to combine all user inputs and return it as a citation 
def combine_func(author, title, month_shortened):
    combined_list = [] # create a list to store author, title, etc
    combined_list.append(author + ". ")
    combined_list.append('"' + title + '." ')
    if day != "":
        combined_list.append(month_shortened + " ")
    else:
        combined_list.append(month_shortened + "")
    combined_list.append(day)
    combined_list.append(", " + year + ".")
    combined_list = "".join(combined_list) # convert list to string
    return combined_list


# run functions
month_shortened = month_func(month)
author = author_func(authors_list)
citation = combine_func(author, title, month_shortened)
print(citation)