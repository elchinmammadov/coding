import customtkinter as ctk
ctk.set_appearance_mode("dark") # default
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.geometry("500x500")

def login():
    print("Test")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ctk.CTkLabel(master=frame, text="Login system", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = ctk.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text="Submit", command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text="Authors in one line")
checkbox.pack(pady=12, padx=10)
