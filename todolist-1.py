from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
import random
import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime



# Build Dashboard Screen
def build_dashboard_screen():
   
    layout = FloatLayout()

    # App Title
    title_label = Label(text="[color=00ff00][b]TO-DO LIST APP[/b][/color]", markup=True, font_size=24,
                        size_hint=(1, 0.1), pos_hint={'center_x': 0.5, 'top': 1})
    layout.add_widget(title_label)

    # Date and Day
    today = datetime.now()
    date_text = today.strftime("%A, %d %B %Y")
    date_label = Label(text=f"[b]{date_text}[/b]", markup=True,
                       size_hint=(1, 0.05), pos_hint={'center_x': 0.5, 'top': 0.93},
                       color=(1, 1, 0, 1))
    layout.add_widget(date_label)

  
    # Add Task Button
    add_btn = Button(text='Add Task',
                     size_hint=(0.3, 0.1),
                     pos_hint={'center_x': 0.5, 'y': 0.05})

    layout.add_widget(add_btn)

    
    return layout
# Build Add Task Screen
def build_add_task_screen():
   
    layout = FloatLayout()

    # Title
    title = Label(text="[color=00ff00][b]ADD NEW TASK[/b][/color]", markup=True, font_size=24,
                  size_hint=(0.8, 0.1), pos_hint={'center_x': 0.5, 'top': 1})
    layout.add_widget(title)

    # Input fields
    obj_label = Label(text="Objective", size_hint=(0.3, 0.08), pos_hint={'x': 0.05, 'top': 0.85})
    layout.add_widget(obj_label)
    obj_input = TextInput(size_hint=(0.6, 0.08), pos_hint={'x': 0.35, 'top': 0.85})
    layout.add_widget(obj_input)

    deadline_label = Label(text="Deadline", size_hint=(0.3, 0.08), pos_hint={'x': 0.05, 'top': 0.7})
    layout.add_widget(deadline_label)
    deadline_input = TextInput(size_hint=(0.6, 0.08), pos_hint={'x': 0.35, 'top': 0.7})
    layout.add_widget(deadline_input)

    priority_label = Label(text="Priority", size_hint=(0.3, 0.08), pos_hint={'x': 0.05, 'top': 0.55})
    layout.add_widget(priority_label)
    priority_input = Spinner(
        text='Select Priority',
        values=('High', 'Medium', 'Low'),
        size_hint=(0.6, 0.08),
        pos_hint={'x': 0.35, 'top': 0.55}
    )
    layout.add_widget(priority_input)

    # Save Task Button
    add_btn = Button(text="Save Task",
                     size_hint=(0.3, 0.1),
                     pos_hint={'center_x': 0.7, 'y': 0.05})
    
        # Back Button
    back_btn = Button(text="Back",
                      size_hint=(0.3, 0.1),
                      pos_hint={'x': 0.2, 'y': 0.05})


    layout.add_widget(add_btn)
    layout.add_widget(back_btn)
    return layout


# Build App
def build():
    return build_dashboard_screen()

class MyApp(App):
    def build(self):
        return build()

if __name__ == "__main__":
    MyApp().run()
