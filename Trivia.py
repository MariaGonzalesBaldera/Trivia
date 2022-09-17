import random
import time
from Preguntas import *
from Colores import *


puntuacion= random.randint(2,10)
ContinuarTrivia=True
intentos=1
punTotal=[]
print('===================================================')
print('    BIENVENIDO(A) A PREGUNTAS DE CULTURA GENERAL   ')
print('===================================================')
time.sleep(0.2)
nombre = input(GREEN+'>>> Antes de empezar indicate tu nombre: \n'+RESET).capitalize()
time.sleep(0.2)
meca(YELLOW+f'Bien {nombre} Te presentaré algunas preguntas para ver si puedes resolverlas \n'+RESET)

while ContinuarTrivia==True:
##--------------Pregunta1-----------------
    print(f'Intento N° {intentos}')
    time.sleep(0.2)
    print(f'Empezarás con una puntuación aleatoria de {puntuacion} puntos')
    
    #Contador
    print('Cargando pregunta')
    conta('1 2 3\n')

    txt1=BLUE+'¿Cuál es el animal nacional de Australia? \n'+RESET
    meca(txt1)

    for letra, alter in pregunta1.items():
        pru=print(CYAN+letra, '-', alter+RESET)
        time.sleep(0.2)

    rpt1=input(BLACK+'Elige "A", "B", "C" ó "D" \n'+RESET).upper()
    time.sleep(0.2)
    while rpt1 not in ('A','B','C','D','X'):
        rpt1=input(RED+f'{nombre}, Debes elegir una letra válida \n'+RESET)
        time.sleep(0.2)
    if rpt1=='B':
            print(YELLOW+F'Excelente {nombre}'+RESET)
            puntuacion+=10
            time.sleep(0.2)

    elif rpt1=='A' or rpt1=='C' or rpt1=='D' :
        for letra, alter in pregunta1.items():
            if rpt1==letra:
                print(RED+alter ,'no es el animal nacional de Australia '+RESET)
                puntuacion-=5  
                time.sleep(0.2)
    elif rpt1=='X':
        meca(MAGENTA+f'Hola {nombre}, Este es un atajo secreto \nPor descubrirlo, le llevaras 20 puntos adicionales\n'+RESET)
        puntuacion+=20
    
    print(YELLOW+f'Obtuviste un apuntuación de {puntuacion} puntos \n \n'+RESET)
    time.sleep(0.2)

##--------------Pregunta2-----------------
    print('Cargando pregunta')
    conta('1 2 3\n')
    txt2=BLUE+'¿Cuál es el país más grande del mundo? \n'+RESET
    
    meca(txt2)

    for letra, alter in pregunta2.items():
        print(CYAN+letra, '-', alter+RESET)
        time.sleep(0.2)

    rpt2=input(BLACK+'Elige "A", "B", "C" ó "D" \n'+RESET).upper()
    time.sleep(0.2)
    while rpt2 not in ('A','B','C','D','X'):
        rpt2=input(RED+f'{nombre}, Debes elegir una letra válida \n'+RESET)
        time.sleep(0.2)
    if rpt2=='A':
            print(YELLOW+f'Excelente {nombre}'+RESET)
            puntuacion+=10
            time.sleep(0.2)

    elif rpt2=='B' or rpt2=='C' or rpt2=='D' :
        for letra, alter in pregunta2.items():
            if rpt2==letra:
                print(RED+alter ,'no es el pais mas grande del mundo '+RESET)
                puntuacion-=5  
                time.sleep(0.2)

    elif rpt2=='X':
        meca(MAGENTA+f'Hola {nombre}, Este es un atajo secreto \n Por descubrirlo, le llevaras 20 puntos adicionales\n'+RESET)
        puntuacion+=20
    
    print(YELLOW+f'Obtuviste un apuntuación de {puntuacion} puntos \n \n'+RESET)
    time.sleep(0.2)

##--------------Pregunta3-----------------
    print('Cargando pregunta')
    conta('1 2 3\n')
    txt3=BLUE+'¿Cuál fue el primer metal que empleó el hombre? \n'+RESET
    
    meca(txt3)
    for letra, alter in pregunta3.items():
        print(CYAN+letra, '-', alter+RESET)
        time.sleep(0.2)

    rpt3=input(BLACK+'Elige "A", "B", "C" ó "D" \n'+RESET).upper()
    while rpt3 not in ('A','B','C','D','X'):
        rpt3=input(RED+f'{nombre}, Debes elegir una letra válida \n'+RESET)
        time.sleep(0.2)
    if rpt3=='D':
            print(YELLOW+f'Excelente {nombre}'+RESET)
            puntuacion+=10
            time.sleep(0.2)            

    elif rpt3=='A' or rpt3=='B' or rpt3=='C' :
        for letra, alter in pregunta3.items():
            if rpt3==letra:
                print(RED+alter ,'no fue el primer metal empleado por el hombre'+RESET)
                puntuacion-=5  
                time.sleep(0.2)
    elif rpt3=='X':
        meca(MAGENTA+f'Hola {nombre}, Este es un atajo secreto \n Por descubrirlo, le llevaras 20 puntos adicionales\n'+RESET)
        puntuacion+=20
    
    print(YELLOW+f'Obtuviste un apuntuación de {puntuacion} puntos \n \n'+RESET)
    time.sleep(0.2)

##--------------Pregunta4-----------------
    print('Cargando pregunta')
    conta('1 2 3\n')
    txt4=BLUE+'¿Quién pintó “la última cena”? \n'+RESET
    
    meca(txt4)

    for letra, alter in pregunta4.items():
        print(CYAN+letra, '-', alter+RESET)
        time.sleep(0.2)

    rpt4=input(BLACK+'Elige "A", "B", "C" ó "D" \n'+RESET).upper()
    time.sleep(0.2)
    while rpt4 not in ('A','B','C','D','X'):
        rpt4=input(RED+f'{nombre}, Debes elegir una letra válida \n'+RESET)
        time.sleep(0.2)
    if rpt4=='C':
            print(YELLOW+f'Excelente {nombre}'+RESET)
            puntuacion+=10
            time.sleep(0.2)

    elif rpt4=='A' or rpt4=='B' or rpt4=='D' :
        for letra, alter in pregunta4.items():
            if rpt4==letra:
                print(RED+alter ,'no pintó la última cena'+RESET)
                puntuacion-=5  
                time.sleep(0.2)

    elif rpt4=='X':
        meca(MAGENTA+f'Hola {nombre}, Este es un atajo secreto \n Por descubrirlo, le llevaras 20 puntos adicionales\n'+RESET)
        puntuacion+=20
    
    print(YELLOW+f'Obtuviste un apuntuación de {puntuacion} puntos \n \n'+RESET)
    time.sleep(0.2)


##--------------Pregunta5-----------------
    print('Cargando pregunta')
    conta('1 2 3\n')
    txt5=BLUE+'¿Quién inventó la bombilla? \n'+RESET
    
    meca(txt5)

    for letra, alter in pregunta5.items():
        print(CYAN+letra, '-', alter+RESET)
        time.sleep(0.2)

    rpt5=input(BLACK+'Elige "A", "B", "C" ó "D" \n'+RESET).upper()
    time.sleep(0.2)
    while rpt5 not in ('A','B','C','D','X'):
        rpt5=input(RED+f'{nombre}, Debes elegir una letra válida \n'+RESET)
        time.sleep(0.2)
    if rpt5=='C':
            print(YELLOW+f'Excelente {nombre}'+RESET)
            puntuacion+=10
            time.sleep(0.2)

    elif rpt5=='A' or rpt5=='B' or rpt5=='D' :
        for letra, alter in pregunta5.items():
            if rpt5==letra:
                print(RED+alter ,'no invento la bombilla '+RESET)
                puntuacion-=5  
                time.sleep(0.2)

    elif rpt5=='X':
        meca(MAGENTA+f'Hola {nombre}, Este es un atajo secreto \n Por descubrirlo, le llevaras 20 puntos adicionales\n'+RESET)
        puntuacion+=20
    
    print(YELLOW+f'Obtuviste un apuntuación de {puntuacion} puntos \n \n'+RESET)
    time.sleep(0.2)

##BonusTrack
    meca("BonusTrack")
    meca('\nPor llegar a este punto se te asignara automaticamente uno de estos puntajes "5", "10", "20", "30","40" ')
    extra=[5,10,20,30,40]
    bonus=random.choice(extra)
    puntuacion+=bonus
    meca(f'\nTu puntuación es {puntuacion}\n')

##FINAL
    respuestaTrivia= input(MAGENTA+f'{nombre}, Llegamos al final de la trivia, si desea repetir responde "si",\n caso contrario presione enter \n'+RESET).lower()
    time.sleep(0.2)
    if respuestaTrivia!='si':
        ContinuarTrivia=False
        meca(GREEN+'Gracias por participar \n'+RESET)
        punTotal.append(puntuacion)
          
    else:
        punTotal.append(puntuacion)
        intentos+=1
        puntuacion=0
time.sleep(0.2)
meca(GREEN+f'Puntajes acumulados en cada intento {punTotal} \n \n'+RESET)

