import PySimpleGUI as sg 
from FIFA import FIFA
from BASEBALL import BASE

sg.theme('Tan')
layout= [[sg.Text('que datos analizamos?', size=(45,4), text_color= ('blue'), font=('Fixedsys',10), justification= 'center')],
        [sg.Button('Fifa', size= (25,3))],
        [sg.Button('Baseball', size= (25,3))],
        [sg.Button('Salir', size= (25,3))]]

window = sg.Window('Actividad 1 x Python Plus - TEORIA -', layout, element_justification= 'center')

while True:
  event,values = window.read()
  if event == 'Salir' or event == sg.WINDOW_CLOSED:
    break
  elif event == 'Fifa':
    FIFA()
  elif event == 'Baseball':
    BASE()   
window.close()    