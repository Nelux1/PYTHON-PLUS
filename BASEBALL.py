import csv
import json

def BASE():
 '''seleccionaremos jugadores de baseball menores de 30 con la posicion catcher y 
    giardaremos su nombre a que equipo pertenece'''

 archivo= open('baseball.csv','r', encoding='UTF-8')
 csvreader = csv.reader(archivo, delimiter=',')
 encabezado= next (csvreader)
 Jugadores=[]
 Jugadores_Jovenes={}
 for linea in csvreader:  
     if float(linea[5]) < 30 and linea[2] == 'Catcher':
         print(linea[0],linea[1])
         print("=" *50)
         Jugadores.append(linea[0])
         Jugadores.append(linea[1])
         Jugadores_Jovenes={'Nombre_Equipo': Jugadores}
 with open('Jugadores_Jovenes.json','w')as file:
     json.dump(Jugadores_Jovenes,file) 
     

