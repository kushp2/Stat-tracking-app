# Stat-tracking-app


Tables: 
    Kush, Sarah
Variables: 
    id INTEGER PRIMARY KEY
    score INTEGER,
    numberOfRaces INTEGER
    win BOOLEAN
    turnAssist BOOLEAN
    highScore BOOLEAN
    lowScore BOOLEAN




UI Example of login code
label = customtkinter.CTkLabel (master = frame, text = "Login System", font=("Roboto",24))
label. pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text= "Username")
entry1.pack(pady = 12, padx = 10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text= "Password", show = "*")
entry2.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = "Lognin", command = outpu)
button.pack(pady = 12, padx = 10)

checkbox = customtkinter.CTkCheckBox(master = frame, text = "remember me")
checkbox.pack(pady = 12, padx = 10)
