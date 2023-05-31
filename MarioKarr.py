import sqlite3
import customtkinter as ctk
from PIL import Image, ImageTk


#functions
#on score button click
def scoreButton(score):
    print(f"{score} button pressed")


#database
#Creates a connection to the database and grabs the data
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#Grabs data for Sarah and Kush's tables
cursor.execute("SELECT * FROM Kush")
kush_data = cursor.fetchall()
cursor.execute("SELECT * FROM Sarah")
sarah_data = cursor.fetchall()


#interface
#sets up the basics of the interface
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("800x480")

#makes frame for sarah and kush's scores and an input button
frame_sarah = ctk.CTkScrollableFrame(master=root)
frame_sarah.pack(side = "left", fill="both", expand = True)
label = ctk.CTkLabel (master = frame_sarah, text = "Sarah", font=("Roboto",24))
label. pack(pady = 12, padx = 10)

frame_kush = ctk.CTkScrollableFrame(master=root)
frame_kush.pack(side = "right", fill="both", expand = True)
label = ctk.CTkLabel (master = frame_kush, text = "Kush", font=("Roboto",24))
label. pack(pady = 12, padx = 10)

#loads images
winImage= ImageTk.PhotoImage(Image.open("win.png").resize((16, 16)))

#populates the frames with buttons
for sarah_entry, kush_entry in zip(sarah_data, kush_data):
    
    sarah_score = sarah_entry[1]
    kush_score = kush_entry[1]
    
    #if sarah wins
    if sarah_entry[3] == 1:
        button_sarah = ctk.CTkButton(master = frame_sarah, image = winImage, text = sarah_score, command = lambda s=sarah_score: scoreButton(s))
        button_sarah.pack(pady=5, padx=5, fill = ctk.X)
    else: 
        button_sarah = ctk.CTkButton(master = frame_sarah, text = sarah_score, command = lambda s=sarah_score: scoreButton(s))
        button_sarah.pack(pady=5, padx=5, fill = ctk.X)
    #if kush wins
    if kush_entry[3] == 1:
        button_kush = ctk.CTkButton(master = frame_kush, image = winImage, text = kush_score, command = lambda s=kush_score: scoreButton(s))
        button_kush.pack(pady=5, padx=5, fill = ctk.X)
    else:
        button_kush = ctk.CTkButton(master = frame_kush, text = kush_score, command = lambda s=kush_score: scoreButton(s))
        button_kush.pack(pady=5, padx=5, fill = ctk.X)


#runs the program then close the cursor and connection
root.mainloop()
cursor.close()
conn.close()