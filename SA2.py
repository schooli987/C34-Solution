from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup

import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- Color Theme ---
Window.clearcolor = (0.01, 0.09, 0.17, 1)  # Dark Navy Blue

PRIMARY_COLOR = (0.2, 0.6, 0.8, 1)  # Teal Blue
SECONDARY_COLOR = (0.1, 0.4, 0.6, 1)
TEXT_COLOR = (1, 1, 1, 1)
BUTTON_TEXT_COLOR = (1, 1, 1, 1)

email_input_signup = None
otp_input_signup = None

# --- Popup ---
def show_popup(title, message):
    popup = Popup(title=title, content=Label(text=message, color=TEXT_COLOR),
                  size_hint=(None, None), size=(300, 200),
                  background_color=SECONDARY_COLOR)
    popup.open()


# --- Send OTP Email ---
def send_otp(instance):
    global email_input_signup
    email = email_input_signup.text.strip()
    if not email:
        show_popup("Error", "Please enter a valid email.")
        return

    otp = str(random.randint(100000, 999999))
   

    sender_email = "sehar627@gmail.com"
    sender_password = "ssssjookrehsrjzj"  # App password (not your regular one)
    subject = "Your OTP Code"
    body = f"Your One-Time Password (OTP) is: {otp}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, msg.as_string())
        server.quit()
        show_popup("Success", f"OTP sent to {email}")
    except Exception as e:
        show_popup("Error", f"Failed to send email: {str(e)}")

# --- Signup Screen ---
def build_signup_screen():
    global email_input_signup, otp_input_signup

    layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
    layout.add_widget(Label(text='[b]Signup[/b]', markup=True, font_size=36,
                            size_hint=(1, None), height=60, color=TEXT_COLOR))

    float_layout = FloatLayout(size_hint=(1, 1))

    name_input = TextInput(hint_text='Name', multiline=False,
                           size_hint=(0.6, None), height=50,
                           pos_hint={'center_x': 0.5, 'center_y': 0.85},
                           background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    email_input_signup = TextInput(hint_text='Email', multiline=False,
                                   size_hint=(0.6, None), height=50,
                                   pos_hint={'center_x': 0.5, 'center_y': 0.70},
                                   background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    password_input = TextInput(hint_text='Password', password=True, multiline=False,
                               size_hint=(0.6, None), height=50,
                               pos_hint={'center_x': 0.5, 'center_y': 0.55},
                               background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    generate_otp_btn = Button(text='Generate OTP', size_hint=(0.4, None), height=40,
                              pos_hint={'center_x': 0.5, 'center_y': 0.40},
                              background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)
    generate_otp_btn.bind(on_press=send_otp)

    otp_input_signup = TextInput(hint_text='Enter OTP', multiline=False,
                                 size_hint=(0.6, None), height=50,
                                 pos_hint={'center_x': 0.5, 'center_y': 0.25},
                                 background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))

    verify_btn = Button(text='Verify OTP', size_hint=(0.4, None), height=50,
                        pos_hint={'center_x': 0.5, 'center_y': 0.10},
                        background_color=PRIMARY_COLOR, color=BUTTON_TEXT_COLOR)


    float_layout.add_widget(name_input)
    float_layout.add_widget(email_input_signup)
    float_layout.add_widget(password_input)
    float_layout.add_widget(generate_otp_btn)
    float_layout.add_widget(otp_input_signup)
    float_layout.add_widget(verify_btn)

    layout.add_widget(float_layout)

    switch_btn = Button(text='Already a user? Go to Login', size_hint=(1, None), height=50,
                        background_color=SECONDARY_COLOR, color=BUTTON_TEXT_COLOR)
    
    layout.add_widget(switch_btn)

    return layout


# --- App ---
class MyApp(App):
    def build(self):
        return build_signup_screen()

if __name__ == "__main__":
    MyApp().run()
