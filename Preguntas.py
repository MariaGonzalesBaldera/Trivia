import time
#¿Cuál es el animal nacional de Australia?
pregunta1={
    'A':'Conejo',
    'B':'Canguro',
    'C':'Gato',
    'D':'Vaca'
    }

#¿Cuál es el país más grande del mundo?
pregunta2={
    'A':'Rusia',
    'B':'Brasil',
    'C':'Argetina',
    'D':'Pánama'
    }
#¿Cuál fue el primer metal que empleó el hombre?
pregunta3={
    'A':'Aluminio',
    'B':'Plata',
    'C':'Oro',
    'D':'Cobre'
    }

#¿Quién pintó “la última cena”?
pregunta4={
    'A':'Pablo Picasso',
    'B':'Salvador Dalí',
    'C':'Leonardo da Vinci',
    'D':'Miguel Angel'
    }

#¿Quién inventó la bombilla?
pregunta5={
    'A':'Nikola Tesla',
    'B':'Thales de Mileto',
    'C':'Thomas Edison',
    'D':'Benjamin Franklin'
    }


#####creando una funcion para mostrar letra x letra
def meca(txt):
    for x in txt:
        print(x, end="", flush=True)
        time.sleep(0.03)


#letra x letra del cargando
def conta(txt):
    for x in txt:
        print(x, end="", flush=True)
        time.sleep(0.5)




