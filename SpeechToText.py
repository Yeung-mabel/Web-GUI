# speech to text

import PySimpleGUI as sg                       

layout = [[sg.Text('Converter')],
          [sg.ReadButton('Speak'), sg.ReadButton('Stop')],
          [sg.Output(size=(80, 10))],
          [sg.Exit()]]

window = sg.Window('Speech To Text', layout)      

window.Close()

