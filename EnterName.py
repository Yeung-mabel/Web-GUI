import PySimpleGUI as sg                       

# Define the window's contents
# layout = [  [sg.Text("What's your name?")],     
#             [sg.Input()],
#             [sg.Button('Ok')] ]

layout = [  [sg.Text('Row 1'), sg.Text("What's your name?")],
            [sg.Text('Row 2'), sg.Input()],
            [sg.Text('Row 3'), sg.Button('Ok')] ]

# Create the window
window = sg.Window('Please Enter Your Name', layout)      

# Display and interact with the Window
event, values = window.read()                   

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  