from turtle import *

def Restriciion1(Operacioncita):
    if Operacioncita==1:
        tipoDeOpe=("Función Cuadrática")
    if Operacioncita==2:
        tipoDeOpe=("Función Lineal")
    if Operacioncita==3:
        tipoDeOpe=("Circunferencia")
    if Operacioncita==4:
        return(0)
    restriccion1=int(input(f"¿Desde donde quieres que inicie tu {tipoDeOpe} Pon un número negativo: "))
    while restriccion1>=0:
        restriccion1=int(input(f"El valor que seleccionaste ({restriccion1}) no es un número negativo, intenta nuevamente: "))
    return(restriccion1)
    

def Restriccion2(Operacioncita,restriccion1):
    if Operacioncita==1:
        tipoDeOpe=("Función Cuadrática")
    if Operacioncita==2:
        tipoDeOpe=("Función Lineal")
    if Operacioncita==3:
        tipoDeOpe=("Circunferencia")
    if restriccion1==0:
        return(0)
    restriccion2=int(input(f"Hasta donde quieres que llegue tu {tipoDeOpe}? Pon un número mayor a {restriccion1}: "))
    while restriccion2<=restriccion1:
        restriccion2=int(input(f"El valor que seleccionaste ({restriccion2}) no es mayor a {restriccion1}, intenta nuevamente: "))
    return(restriccion2)

def operacion(x,Operacioncita,restriccion2):
    r=(restriccion2-x)/2
    if Operacioncita==1:
        return(1/2*x**2+1)
    if Operacioncita==2:
        return(3*x+1)
    if Operacioncita==3:
        return("circle")
    if Operacioncita==4:
        return("cerrar")

def cuadratica():
    coordenadaInicialX=0
    coordenadaInicialY=0
    Operacioncita=int(input("¿Que quieres dibujar hoy? \n Escribe 1 para graficar una función cuadrática \n Escribe 2 para graficar una función lineal \n Escribe 3 para graficar una circunferencia \n Escribe 4 para Cerrar \n: "))
    while Operacioncita!=1 and Operacioncita!=2 and Operacioncita!=3 and Operacioncita!=4:
        Operacioncita=int(input("El valor ingresado no es válido, recuerde, puede elegir 1,2,3 o 4. \n Estas son las opciones:\n Escribe 1 para graficar una función cuadrática \n Escribe 2 para graficar una función lineal \n Escribe 3 para graficar una circunferencia \n Escribe 4 para Cerrar \n: "))
    x1=Restriciion1(Operacioncita)
    evaluador=Restriccion2(Operacioncita,x1)
    x2=x1
    if operacion(x1,Operacioncita,evaluador)==("circle"):
        r=(evaluador-x1)/2
        y=pow((r**2-x1**2),0.5)
        penup()
        setpos(x1,y)
        pendown()
        while x1<=evaluador:
            y=pow((r**2-x1**2),0.5)
            setpos(x1,y)
            x1=x1+1
        y=(pow((r**2-x2**2),0.5))*-1
        penup()
        setpos(x2,y)
        pendown()
        while x2<=evaluador:
            y=(pow((r**2-x2**2),0.5))*-1
            setpos(x2,y)
            x2=x2+1
        done()
    elif operacion(x1,Operacioncita,evaluador)=="cerrar":
        print("ADIOS")
    else:
        penup()
        setpos(coordenadaInicialX+x1,coordenadaInicialY+operacion(x1,Operacioncita,evaluador))
        pendown()
        while x1<=evaluador:
            y=operacion(x1,Operacioncita,evaluador)
            setpos(coordenadaInicialX+x1,coordenadaInicialY+y)
            x1=x1+1
    done()  
cuadratica()
