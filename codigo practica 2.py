#Distancias 2 Practica
#A)-Graficar (x,y) los 2 puntos inicio y final
#matlotlib(x,y, puntos rojos)
#Recta entre dos puntos azul
#ejex_ejey-plt.legend
#ejes nombre
#activar rejilla
#B)Ingresar cuantas coordenadas
#x=input(input("ingresa un numero: "))
#agregar cada coordenada (x,y)manualmente (recomendacion ALMACENAR en una lista
#Graficar puntos de coordenadas-opcional
#Distancia euclidiana de cada linea aplicar for
#sumatoria dist eucl
#calcular el area con una funcion
##import matplotlib.pyplot as plt
##
##x= [2,4,6,8,10,12,14,16,18,19,20]
##x= [i for i in range (1,10)]
##y= [i*2 for i in range (1,10)]
##x2= [i*2 for i in range (0,10)]
##y2= [i*2 for i in range (0,10)]
##
##cuantos_ejex= len(x)
##cuantos_ejey= len(y)
##assert cuantos_ejex == cuantos_ejey
##
##
##plt.plot(x,y,color= "blue",label= "lineal")
##plt.plot(x2,y2, label= "lineal")
##plt.scatter(x2,y2, color="green",s= 14)
##plt.scatter(x,y,color= "red",s=25)
##plt.scatter(x,y,color= "red",s=25)
##plt.axhline(y= 0,color= "black")
##plt.axvline(x= 0,color= "black")
##plt.title("Distancias Practicas 2")
##plt.xlabel("ejex")
##plt.ylabel("ejey")
##plt.legend()
##plt.grid(True)
##plt.show()




######practica 2 Inicial calculada con distancias
##import matplotlib.pyplot as plt
##
##print("aqui inicia la practica")
##print("cantidad de coordenadas:")
##coord_totales= int(input())
##
##coordenadas=[]
##for i in range(0,coord_totales):
##    print("ingrese coordenada",i)
##    x=int(input("x:"))
##    y=int(input("y:"))
##    coordenadas.append((x,y))
##    
##print(coordenadas)#lista de coordenadas
##print(type(coordenadas[0][0]))
##from math import sqrt
##distancias=[]
##for j in range(0,coord_totales-1):
##    dx=(coordenadas[j][0]-coordenadas[j][0])
##    dy=(coordenadas[j][1]-coordenadas[j][1])
##    distancias.append(sqrt((dx**2)+(dy**2)))
##
##plt.axhline(x, color= "black")
##plt.axline(y, color= "black")
##plt.title("Mi inicial")
##plt.xlabel("x")
##plt.ylabel("y")
##plt.legend()
##plt.grid(True)
##plt.show
##
##print(distancias)
##
##    
##
import matplotlib.pyplot as plt
from math import sqrt

print("Aquí inicia la práctica")
print("Cantidad de coordenadas:")
coord_totales = int(input())

coordenadas = []
for i in range(0, coord_totales):
    print("Ingrese coordenada", i)
    x = int(input("x: "))
    y = int(input("y: "))
    coordenadas.append((x, y))

print(coordenadas)  # lista de coordenadas

distancias = []
for j in range(0, coord_totales - 1):
    dx = (coordenadas[j + 1][0] - coordenadas[j][0])
    dy = (coordenadas[j + 1][1] - coordenadas[j][1])
    distancias.append(sqrt((dx ** 2) + (dy ** 2)))

# Graficar las coordenadas
x_coords = [x[0] for x in coordenadas]
y_coords = [y[1] for y in coordenadas]
plt.plot(x_coords, y_coords, 'o-')

plt.title("Mi inicial")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

print(distancias)

