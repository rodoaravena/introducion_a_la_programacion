def posicion_por_letras(letra):
  if letra == "A":
    return 0
  if letra == "B":
    return 1
  if letra == "C":
    return 2
  if letra == "D":
    return 3
  if letra == "E":
    return 4
  if letra == "F":
    return 5

def agregar_minas(tablero):
  codigo = input("Ingrese el código de posiciones: ")
  if len(codigo) == 6:
    contador_pos = 0
    pos = ""
    fila = 0
    columna = 0
    for caracter in codigo:
      pos += caracter
      contador_pos += 1
      if contador_pos == 2:
        fila = posicion_por_letras(pos[0])
        columna = int(pos[1]) - 1
        print("Posicion encontrada! ", pos) 
        
        tablero[fila][columna] = "*"
        contador_pos = 0
        pos = ""

  return tablero  
