import sqlite3
import customtkinter as ctk
from PIL import Image, ImageTk


#functions
#clears the UI and adds a back button
def clearUI():
    for widget in root.winfo_children():
        widget.pack_forget()
    createBackButton()

#on score button click
def scoreButton(match):
    clearUI()

    #fills out the frame
    label.configure(text=f"Race {match[0]} \n {match[1]} points, {match[2]} races", font=("Roboto",24))
    label.pack(pady=10, padx=10)

#creates the back button
def createBackButton():
    global back_button
    back_button = ctk.CTkButton(master=root, text="Back", command=showOriginalView)
    back_button.pack(pady=10, padx=10, anchor="nw")

#goes back to the base frame
def showOriginalView():
    #removes all UI
    for widget in root.winfo_children():
        widget.pack_forget()

    #adds back the base frames
    frame_input.pack(side = "bottom", expand = False)
    frame_sarah.pack(side="left", fill="both", expand=True)
    frame_kush.pack(side="right", fill="both", expand=True)

    #removes the back button
    back_button.pack_forget()

#sets up the interface for a user to insert a new race
def inputData():
    clearUI()

    #submit button
    submit_button = ctk.CTkButton(master=root, text="Submit")
    submit_button.pack(side="bottom", pady=10, padx=10)

    #sarah's input
    frame_leftInput = ctk.CTkScrollableFrame(master=root)
    frame_leftInput.pack(side = "left", fill="both", expand = True)

    Linput_label = ctk.CTkLabel(master=frame_leftInput, text="Enter Sarah's Data", font=("Roboto", 20))
    Linput_label.pack(pady=10)

    #text input
    Lpoints_label = ctk.CTkLabel(master=frame_leftInput, text="Points:")
    Lpoints_label.pack()

    Lpoints_entry = ctk.CTkEntry(master=frame_leftInput)
    Lpoints_entry.pack(pady=10)

    Lraces_label = ctk.CTkLabel(master=frame_leftInput, text="Races:")
    Lraces_label.pack()

    Lraces_entry = ctk.CTkEntry(master=frame_leftInput)
    Lraces_entry.pack(pady = 10)

    #boolean inputs
    Lcheckbox_win = ctk.IntVar()
    LwinButton = ctk.CTkCheckBox(master=frame_leftInput, text="Win", variable=Lcheckbox_win)
    LwinButton.pack(pady=10)

    Lcheckbox_turnAssist = ctk.IntVar()
    LassistButton = ctk.CTkCheckBox(master=frame_leftInput, text="Turn Assist", variable=Lcheckbox_turnAssist)
    LassistButton.pack(pady=10)


    #kush's input
    frame_rightInput = ctk.CTkScrollableFrame(master=root)
    frame_rightInput.pack(side = "right", fill="both", expand = True)
    
    Rinput_label = ctk.CTkLabel(master=frame_rightInput, text="Enter Kush's Data", font=("Roboto", 20))
    Rinput_label.pack(pady=10)
    
    #text inputs
    Rpoints_label = ctk.CTkLabel(master=frame_rightInput, text="Points:")
    Rpoints_label.pack()

    Rpoints_entry = ctk.CTkEntry(master=frame_rightInput)
    Rpoints_entry.pack(pady = 10)

    Rraces_label = ctk.CTkLabel(master=frame_rightInput, text="Races:")
    Rraces_label.pack()

    Rraces_entry = ctk.CTkEntry(master=frame_rightInput)
    Rraces_entry.pack(pady = 10)

    #boolean inputs
    Rcheckbox_win = ctk.IntVar()
    RwinButton = ctk.CTkCheckBox(master=frame_rightInput, text="Win", variable=Rcheckbox_win)
    RwinButton.pack(pady = 10)

    Rcheckbox_turnAssist = ctk.IntVar()
    RassistButton = ctk.CTkCheckBox(master=frame_rightInput, text="Turn Assist", variable=Rcheckbox_turnAssist)
    RassistButton.pack(pady = 10) 



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
back_button = None
label = ctk.CTkLabel(master=root)
label.pack_forget()

#makes frame for the scores, and the input and stats buttons
frame_input = ctk.CTkFrame(master=root)
frame_input.pack(side = "bottom", expand = False)

frame_sarah = ctk.CTkScrollableFrame(master=root)
frame_sarah.pack(side = "left", fill="both", expand = True)
sarah_label = ctk.CTkLabel (master = frame_sarah, text = "Sarah", font=("Roboto",24))
sarah_label. pack(pady = 12, padx = 10)

frame_kush = ctk.CTkScrollableFrame(master=root)
frame_kush.pack(side = "right", fill="both", expand = True)
kush_label = ctk.CTkLabel (master = frame_kush, text = "Kush", font=("Roboto",24))
kush_label. pack(pady = 12, padx = 10)

#loads images
winImage= ImageTk.PhotoImage(Image.open("win.png").resize((16, 16)))

#populates the frames with buttons
for sarah_entry, kush_entry in zip(sarah_data, kush_data):
    
    #if sarah wins, the button will have an image attatched
    if sarah_entry[3] == 1:
        button_sarah = ctk.CTkButton(master = frame_sarah, image = winImage, text = sarah_entry[1], command = lambda s=sarah_entry: scoreButton(s))
        button_sarah.pack(pady=5, padx=5, fill = ctk.X)
    else: 
        button_sarah = ctk.CTkButton(master = frame_sarah, text = sarah_entry[1], command = lambda s=sarah_entry: scoreButton(s))
        button_sarah.pack(pady=5, padx=5, fill = ctk.X)

    #if kush wins the button will have an image attatched
    if kush_entry[3] == 1:
        button_kush = ctk.CTkButton(master = frame_kush, image = winImage, text = kush_entry[1], command = lambda s=kush_entry: scoreButton(s))
        button_kush.pack(pady=5, padx=5, fill = ctk.X)
    else:
        button_kush = ctk.CTkButton(master = frame_kush, text = kush_entry[1], command = lambda s=kush_entry: scoreButton(s))
        button_kush.pack(pady=5, padx=5, fill = ctk.X)

input_button = ctk.CTkButton(master=frame_input, text="Input Data", width = 300, command = inputData)
input_button.pack(side="right", pady=10, padx=10, fill = ctk.X)
stats_button = ctk.CTkButton(master=frame_input, text="Stats", width = 300)
stats_button.pack(side="left", pady=10, padx=10, fill = ctk.X)



#runs the program then close the cursor and connection
root.mainloop()
cursor.close()
conn.close()