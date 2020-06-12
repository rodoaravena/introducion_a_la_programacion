n=6 #dimensión del tablero
m=3 #número de minas

#Crea del Tablero:
T = []
i = 1
while (i<=n):
    F = ['.'] * n
    T.append(F)
    i = i+1

#Llena el Tablero con las Minas:
strPos = input('Ingresa el string con las posiciones de las minas: ')
strPos = strPos.upper()
i=0
while i<2*m:
    T[ord(strPos[i])-65][int(strPos[i+1])-1] = '*'
    i=i+2

#Imprime el Tablero:
#Imprime los títulos de cada columna (números):
print('', end='  ')
j=0
while j<n:
    print(j+1, end=' ')
    j=j+1
    
print('', end='\n')

#Imprime el tablero con letras mayúsculas al principio de cada fila:
i=0
while i<n:
    j=0
    print(chr(i+65), end=' ')
    while j<n:
        if T[i][j] == '*':
            print('.', end=' ')
        else:
            print(T[i][j], end=' ')
        j=j+1
    print('', end='\n')
    i=i+1

    
#Cuenta las minas reales y posiciones sin minas:
numNoMinasSinDescubrir = 0
numMinas = 0
i=0
while i<n:
    j=0
    while j<n:
        if T[i][j] == '*':
            numMinas += 1
        else:
            numNoMinasSinDescubrir += 1
        j=j+1
    i=i+1

#INICIO DEL JUEGO:
ganaste = False
perdiste = False
while perdiste == False and ganaste == False:

    #Pide posición de Juego (letra y luego número):
    strPos = input('Ingresa la casilla del tablero que quieres abrir: ')
    strPos = strPos.upper()
    
    x = ord(strPos[0])-65
    y = int(strPos[1])-1

    if 0<=x<n and 0<=y<n:
        #cuenta las minas entorno
        contMinas = 0
        if T[x][y] == '*':
            perdiste = True
        elif T[x][y] == '.':
            if x>0 and y>0 and T[x-1][y-1] == '*': #ARRIBA-IZQUIERDA
                contMinas += 1
            if x>0 and T[x-1][y] == '*': #ARRIBA
                contMinas += 1
            if x>0 and y<n-1 and T[x-1][y+1] == '*': #ARRIBA-DERECHA
                contMinas += 1
            if y>0 and T[x][y-1] == '*': #IZQUIERDA
                contMinas += 1
            if y<n-1 and T[x][y+1] == '*': #DERECHA
                contMinas += 1
            if x<n-1 and y>0 and T[x+1][y-1] == '*': #ABAJO-IZQUIERDA
                contMinas += 1
            if x<n-1 and T[x+1][y] == '*': #ABAJO
                contMinas += 1
            if x<n-1 and y<n-1 and T[x+1][y+1] == '*': #ABAJO-DERECHA
                contMinas += 1
            T[x][y] = str(contMinas)
            numNoMinasSinDescubrir -= 1        

    #Analiza si abrió todas las casillas sin minas:
    if numNoMinasSinDescubrir == 0:
        ganaste = True

    #Imprime el Tablero:
    #Imprime los títulos de cada columna (números):
    print('', end='  ')
    j=0
    while j<n:
        print(j+1,end=' ')
        j=j+1
        
    print('', end='\n')

    #Imprime el tablero con letras mayúsculas al principio de cada fila:        
    i=0
    while i<n:
        j=0
        print(chr(i+65), end=' ')
        while j<n:
            if perdiste == True or ganaste == True:
                print(T[i][j], end=' ')
            else:
                if T[i][j] == '*':
                    print('.', end=' ')
                else:
                    print(T[i][j], end=' ')
            j=j+1
        print('', end='\n')
        i=i+1
        
    #Mensaje de cierre de jugo:            
    if ganaste == True:
        print('GANASTE')
    if perdiste == True:
        print('PERDISTE')        

#FIN DEL JUEGO
