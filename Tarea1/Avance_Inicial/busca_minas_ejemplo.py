from funciones import agregar_minas
  
tablero = [
  [0,0,0,0,0,0], #Fila A
  [0,0,0,0,0,0], #Fila B
  [0,0,0,0,0,0], #Fila C
  [0,0,0,0,0,0], #Fila D
  [0,0,0,0,0,0], #Fila E
  [0,0,0,0,0,0]  #Fila F
]
print("Tablero inicial: ")
for fila in tablero:
  print(fila)

tablero_nuevo = agregar_minas(tablero)
print("Tablero final: ")
for fila in tablero_nuevo:
  print(fila)