import csv
import json 


def FIFA():
     '''Elegiremos jugadores con rating alto de pie habil derecho y 
     guardaremos su nombre y posicion en el campo de juego'''
     
     archivo= open('fifa.csv','r',encoding='UTF-8')
     csvreader = csv.reader(archivo, delimiter=',')
     encabezado = next(csvreader)
     print(encabezado)
     print("=" * 50)
     Jugadores=[]
     Jugadores_Elegidos={}
     for linea in csvreader:  
        if int(linea[2].strip()) >= 85 and linea[5].strip() == 'Right': #Uso strip porque el datasets tenia delimitador de "," y espacio
           print(linea[1], linea[3])
           print("=" *50)
           Jugadores.append(linea[1])
           Jugadores.append(linea[3])
           Jugadores_Elegidos={'Nombre_Posicion': Jugadores}
     with open('Jugadores_Seleccionados.json','w')as file:
      json.dump(Jugadores_Elegidos,file) 
     

     