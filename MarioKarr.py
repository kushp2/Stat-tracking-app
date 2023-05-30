import kivy
kivy.require("2.1.0")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
import sqlite3





# Functions
#makes the individual buttons layout
def makeButton(data, button_layout):
    button = Button(text=f"{data[1]}", size_hint=(None, 1), width=300, background_color = (0, 1, 1, 1))
    button_layout.add_widget(button)

    if data[3] == 1:
        icon = Image(source="win.png", size_hint=(None, 1), width=30)
        button_layout.add_widget(icon)
    
    return button_layout

# Creates the layout for Sarah's buttons
def sarahButton(sarah_scroll_layout):
    sarah_label = Label(text="Sarah's Data")
    sarah_scroll_layout.layout.add_widget(sarah_label)
    
    #makes a button for every match
    for data in sarah_data:
        button_layout = BoxLayout(orientation='horizontal')
        button_layout = makeButton(data, button_layout)
        sarah_scroll_layout.layout.add_widget(button_layout)
    
    return sarah_scroll_layout

# Creates the layout for Kush's buttons
def kushButton(kush_scroll_layout):
    kush_label = Label(text="Kush's Data")
    kush_scroll_layout.layout.add_widget(kush_label)
    
    for data in kush_data:
        button_layout = BoxLayout(orientation='horizontal')
        button_layout = makeButton(data, button_layout)
        kush_scroll_layout.layout.add_widget(button_layout)
    
    return kush_scroll_layout
#end of fuctions




#Creates a connection to the database and grabs the data
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#Grabs data for Sarah and Kush tables
cursor.execute("SELECT * FROM Kush")
kush_data = cursor.fetchall()
cursor.execute("SELECT * FROM Sarah")
sarah_data = cursor.fetchall()

#changes the window color
Window.clearcolor = (.5, .5, .5, 1)

class ScrollableBoxLayout(ScrollView):
    def __init__(self, **kwargs):
        super(ScrollableBoxLayout, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

class MarioKarrApp(App):
    def build(self):
        # Create a scrollable box layout for Sarah's data
        sarah_scroll_layout = ScrollableBoxLayout()
        sarah_scroll_layout = sarahButton(sarah_scroll_layout)

        # Create a scrollable box layout for Kush's data
        kush_scroll_layout = ScrollableBoxLayout()
        kush_scroll_layout = kushButton(kush_scroll_layout)

        # Create a scroll view for Sarah's data
        sarah_scroll_view = ScrollView()
        sarah_scroll_view.add_widget(sarah_scroll_layout)

        # Create a scroll view for Kush's data
        kush_scroll_view = ScrollView()
        kush_scroll_view.add_widget(kush_scroll_layout)

        # Synchronize scrolling of the two scroll views
        def sync_scroll_pos(dt):
            sarah_scroll_view.scroll_y = kush_scroll_view.scroll_y

        sarah_scroll_view.bind(scroll_y=lambda instance, value: Clock.schedule_once(sync_scroll_pos, 0))
        kush_scroll_view.bind(scroll_y=lambda instance, value: Clock.schedule_once(sync_scroll_pos, 0))

        # Create a root box layout to hold the two scroll views side by side
        root_layout = BoxLayout(orientation='horizontal')
        root_layout.add_widget(sarah_scroll_view)
        root_layout.add_widget(kush_scroll_view)

        return root_layout


# Close the cursor and connection and run the app
cursor.close()
conn.close()
MarioKarrApp().run()
