import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from numpy import arange, sin, pi, tan, cos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure    
from PIL import ImageTk, Image
import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys

if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *

    
    
# Calculos y animaciones

#se usan para saber el rango de los valores que se debe mostrar en el plano cartesiano
XMAX=0
YMAX=XMAX
#numero de frames de la animacion
FRAMES=50
#tiempo de cada frame en la animacion
INTERVAL=2

#variables para las operaciones
ALFA=1
BETA=2
U=[1,4]
V=[-3,2]
T=[[-1,2],[0,3]]

#obtiene el maximo de una tupla de dos elementos
def maximo(lista):
    if(lista[0]>lista[1]):
        return lista[0]
    return lista[1]
#obtiene el valor de una subposicion dentro de un vector
def funcion(sumau,sumav,subposicion):
    h=sumau[0]*subposicion/FRAMES
    x=[0,0]
    y=[0,0]
    x[0]=h
    x[1]=sumav[0]+h
    nx=(sumau[0]/FRAMES)*subposicion
    v=sumau[0]
    if(sumau[0]==0):
        v=1
    ny=(sumau[1]/v*nx)
    y[0]=ny
    y[1]=sumav[1]+ny
    return [x,y]
#anima la suma
def animate(i,line,u,v):
    line.set_data([], [])
    punto=funcion(u,v,i)
    x=[punto[0][0],punto[0][1]]
    y=[punto[1][0],punto[1][1]]
    line.set_data(x, y)
    return line,
#anima la suma
def animate2(i,line,u,v):
    line.set_data([], [])
    punto=funcion(u,v,i)
    x=[punto[0][0],punto[0][1]]
    y=[punto[1][0],punto[1][1]]
    line.set_data(x, y)
    return line,
#multiplica la TL de una coordenada cartesiana
def transformar(matriz,puntos):
    resultado=[0,0]
    for fila in range(len(matriz)):
        for valor in range(len(matriz[fila])):
            resultado[fila]+=(matriz[fila][valor]*puntos[valor])
    return (resultado)
def multiplicar(puntos,alfa):
    resultado=[0,0]
    resultado[0]=puntos[0]*alfa
    resultado[1]=puntos[1]*alfa
    return resultado
#obtiene los valores de xmax y ymax
def getxymax():
    global XMAX,YMAX
    temp1=temp2=temp3=0
    u=v=alfau=betav=sumaalfabetauv=tu=tv=sumatuv=tau=tbv=stabuv=0
    u=maximo(U)
    v=maximo(V)
    temp1=multiplicar(U,ALFA)
    temp2=multiplicar(V,BETA)
    temp3=[temp1[0]+temp2[0],temp1[1]+temp2[1]]
    alfau=maximo(temp1)
    betav=maximo(temp2)
    sumaalfabetauv=maximo(temp3)
    temp1=transformar(T,U)
    temp2=transformar(T,V)
    tu=maximo(temp1)
    tv=maximo(temp2)
    temp1=multiplicar(temp1,ALFA)
    temp2=multiplicar(temp2,BETA)
    tau=maximo(temp1)
    tbv=maximo(temp2)
    temp3=[temp1[0]+temp2[0],temp1[1]+temp2[1]]
    stabuv=maximo(temp3)
    XMAX=max(u,v,alfau,betav,sumaalfabetauv,tu,tv,tau,tbv,stabuv)
    XMAX=XMAX+1
    YMAX=XMAX 
#obtiene el grafico para la parte uv
def uv(ALFA,BETA,U,V,T):
    figuraUV, axUV = plt.subplots()
    ux=[0,U[0]]
    uy=[0,U[1]]
    vx=[0,V[0]]
    vy=[0,V[1]]
    axUV.set_xlim([-1*XMAX, XMAX])
    axUV.set_ylim([-1*YMAX, YMAX])
    axUV.plot(ux,uy)
    axUV.plot(vx,vy)
    axUV.arrow(0, 0, U[0], U[1], head_width=.5, head_length=.5, fc='k', ec='k')
    axUV.arrow(0, 0, V[0], V[1], head_width=.5, head_length=.5, fc='k', ec='k')
    return figuraUV
#obtiene el grafico para la parte T(uv)
def tuv(ALFA,BETA,U,V,T):
    TU=transformar(T,U)
    TV=transformar(T,V)
    figuraTUV, axTUV = plt.subplots()
    axTUV.set_xlim([-1*XMAX, XMAX])
    axTUV.set_ylim([-1*YMAX, YMAX])
    tux=[0,TU[0]]
    tuy=[0,TU[1]]
    tvx=[0,TV[0]]
    tvy=[0,TV[1]]
    axTUV.plot(tux,tuy)
    axTUV.plot(tvx,tvy)
    axTUV.arrow(0, 0, tux[1], tuy[1], head_width=.5, head_length=.5, fc='k', ec='k')
    axTUV.arrow(0, 0, tvx[1], tvy[1], head_width=.5, head_length=.5, fc='k', ec='k')
    return figuraTUV
#hace el grafico de la suma de alfau y betav
def sumauv(ALFA,BETA,U,V,T):
    figuraSUMAUV, axSUMAUV = plt.subplots()
    axSUMAUV.set_xlim([-1*XMAX, XMAX])
    axSUMAUV.set_ylim([-1*YMAX, YMAX])
    sumau=multiplicar(U,ALFA)
    sumav=multiplicar(V,BETA)
    ux=[0,sumau[0]]
    uy=[0,sumau[1]]
    vx=[0,sumav[0]]
    vy=[0,sumav[1]]
    sumax=[0,sumau[0]+sumav[0]]
    sumay=[0,sumau[1]+sumav[1]]
    axSUMAUV.plot(ux,uy)
    axSUMAUV.plot(vx,vy)
    axSUMAUV.arrow(0, 0, ux[1], uy[1], head_width=.5, head_length=.5, fc='k', ec='k')
    axSUMAUV.arrow(0, 0, sumax[1], sumay[1], head_width=.5, head_length=.5, fc='k', ec='k')
    axSUMAUV.arrow(0, 0, vx[1], vy[1], head_width=.5, head_length=.5, fc='k', ec='k')
    line,=axSUMAUV.plot([], [], lw=2)
    axSUMAUV.plot(sumax,sumay)
    animsumauv = animation.FuncAnimation(figuraSUMAUV, animate,fargs=(line, sumau,sumav),
                               frames=FRAMES, interval=INTERVAL, blit=True)
    
    return figuraSUMAUV
#hace el grafico de la animacion de la suma de las transformaciones

def tsumauv(ALFA,BETA,U,V,T):
    figuraTSUMAUV, axTSUMAUV = plt.subplots()
    axTSUMAUV.set_xlim([-1*XMAX, XMAX])
    axTSUMAUV.set_ylim([-1*YMAX, YMAX])
    tsumau=transformar(T,multiplicar(U,ALFA))
    tsumav=transformar(T,multiplicar(V,BETA))
    ux=[0,tsumau[0]]
    uy=[0,tsumau[1]]
    vx=[0,tsumav[0]]
    vy=[0,tsumav[1]]
    tsumax=[0,tsumau[0]+tsumav[0]]
    tsumay=[0,tsumau[1]+tsumav[1]]
    axTSUMAUV.plot(ux,uy)
    axTSUMAUV.plot(vx,vy)
    axTSUMAUV.arrow(0, 0, ux[1], uy[1], head_width=.5, head_length=.5, fc='k', ec='k')
    axTSUMAUV.arrow(0, 0, vx[1], vy[1], head_width=.5, head_length=.5, fc='k', ec='k')
    line,=axTSUMAUV.plot([], [], lw=2)
    axTSUMAUV.plot(tsumax,tsumay)
    axTSUMAUV.arrow(0, 0, tsumax[1], tsumay[1], head_width=.5, head_length=.5, fc='k', ec='k')
    animtsumauv = animation.FuncAnimation(figuraTSUMAUV, animate2,fargs=(line, tsumau,tsumav),
                               frames=FRAMES, interval=INTERVAL, blit=True)
    
    return figuraTSUMAUV

# Interfaz Grafica

root = Tk()
root.wm_title("Programa Dos")

root.geometry("800x670+0+0")

m = PanedWindow(root, orient = HORIZONTAL)
m.pack(fill=BOTH, expand=1)


m1 = PanedWindow(m, orient = VERTICAL)
m1.pack(expand = 1)
m.add(m1)

m2 = PanedWindow(m, orient = VERTICAL)
m2.pack(expand = 1)
m.add(m2)


# a tk.DrawingArea

##def on_key_event(event):
##    print('you pressed %s' % event.key)
##    key_press_handler(event, canvas, toolbar)
##
##canvas.mpl_connect('key_press_event', on_key_event)


alfaL = Label(m1, text="ALFA = ")
alfaL.place(x=0,y=610)

alfaT = Text(m1, height=1, width=2)
alfaT.place(x=45,y=610)
alfaT.insert(END, "0")

betaL = Label(m1, text="BETA = ")
betaL.place(x=80,y=610)

betaT = Text(m1, height=1, width=2)
betaT.place(x=125,y=610)
betaT.insert(END, "0")

uL = Label(m1, text="u = ")
uL.place(x=155,y=610)

parIzq1 = Label(m1, text = '(')
parIzq1.place(x=177,y=610)

uTX = Text(m1, height=1, width=2)
uTX.place(x=190,y=610)
uTX.insert(END, "0")

coma1 = Label(m1, text=',')
coma1.place(x = 210, y = 610)

uTY = Text(m1, height=1, width=2)
uTY.place(x=220,y=610)
uTY.insert(END, "0")

parDer1 = Label(m1, text = ')')
parDer1.place(x=244,y=610)

vL = Label(m1, text="v = ")
vL.place(x=274,y=610)

parIzq2 = Label(m1, text = '(')
parIzq2.place(x=294,y=610)

vTX = Text(m1, height=1, width=2)
vTX.place(x=307,y=610)
vTX.insert(END, "0")

coma2 = Label(m1, text=',')
coma2.place(x = 327, y = 610)

vTY = Text(m1, height=1, width=2)
vTY.place(x=337,y=610)
vTY.insert(END, "0")

parDer2 = Label(m1, text = ')')
parDer2.place(x=359,y=610)

tL = Label(m2,text = "T = ")
tL.place(x=0,y=610)

parIzqMat1 = Label(m2, text = '/')
parIzqMat1.place(x = 30,y = 600)
parIzqMat2 = Label(m2, text = "\\")
parIzqMat2.place(x = 30,y = 620)

M11 = Text(m2, height=1,width=2)
M11.place(x = 45,y = 600)
M11.insert(END, "1")
M12 = Text(m2, height=1,width=2)
M12.place(x = 75,y = 600)
M12.insert(END, "0")
M21 = Text(m2, height=1,width=2)
M21.place(x = 45,y = 620)
M21.insert(END, "0")
M22 = Text(m2, height=1,width=2)
M22.place(x = 75,y = 620)
M22.insert(END, "1")
parIzqMat1 = Label(m2, text = '\\')
parIzqMat1.place(x = 100,y = 600)
parIzqMat2 = Label(m2, text = "/")
parIzqMat2.place(x = 100,y = 620)

def _calcularYgraficar():
    inputALFA = alfaT.get("1.0",END)
    inputBETA = betaT.get("1.0",END)
    inputUX = uTX.get("1.0",END)
    inputUY = uTY.get("1.0",END)
    inputVX = vTX.get("1.0",END)
    inputVY = vTY.get("1.0",END)

    inputM11 = M11.get("1.0",END)
    inputM12 = M12.get("1.0",END)
    inputM21 = M21.get("1.0",END)
    inputM22 = M22.get("1.0",END)

    inputALFA = int(inputALFA)
    inputBETA = int(inputBETA)
    inputUX = int(inputUX)
    inputUY = int(inputUY)
    inputVX = int(inputVX)
    inputVY = int(inputVY)
    inputM11 = int(inputM11)
    inputM12 = int(inputM12)
    inputM21 = int(inputM21)
    inputM22 = int(inputM22)

    print(inputALFA)
    print(inputBETA)
    print(inputUX)
    print(inputUY)
    print(inputVX)
    print(inputVY)
    print(inputM11)
    print(inputM12)
    print(inputM21)
    print(inputM22)

##    ALFA = inputALFA
##    BETA = inputBETA
##    U = [inputUX,inputUY]
##    V = [inputVX,inputVY]
##    T = [[inputM11,inputM12],[inputM21,inputM22]]
##
##    p = tsumauv(ALFA,BETA,U,V,T)
##    canvas = FigureCanvasTkAgg(p, master = m1)
##    canvas.show()
##    canvas.get_tk_widget().pack()
    f0 = Figure(figsize=(4, 3), dpi=100)
    a0 = f0.add_subplot(111)
    t0 = arange(0.0, 3.0, 0.01)
    s0 = (2*pi*t0)

    a0.plot(t0, s0)

    canvas0 = FigureCanvasTkAgg(f0, master = m1)
    canvas0.show()
    canvas0.get_tk_widget().pack()



    f = Figure(figsize=(4, 3), dpi=100)
    a = f.add_subplot(111)
    t = arange(0.0, 3.0, 0.01)
    s = tan(2*pi*t)

    a.plot(t, s)

    canvas = FigureCanvasTkAgg(f, master = m1)
    canvas.show()
    canvas.get_tk_widget().pack()



    f2 = Figure(figsize=(4, 3), dpi=100)
    a2 = f2.add_subplot(111)
    t2 = arange(0.0, 3.0, 0.01)
    s2 = sin(2*pi*t2)

    a2.plot(t2, s2)

    canvas2 = FigureCanvasTkAgg(f2, master = m2)
    canvas2.show()
    canvas2.get_tk_widget().pack()


    f3 = Figure(figsize=(4, 3), dpi=100)
    a3 = f3.add_subplot(111)
    t3 = arange(0.0, 3.0, 0.01)
    s3 = cos(2*pi*t3)

    a3.plot(t3, s3)

    canvas3 = FigureCanvasTkAgg(f3, master = m2)
    canvas3.show()
    canvas3.get_tk_widget().pack()

button = Button(master = m, text='CALCULAR Y GRAFICAR', command=_calcularYgraficar)
button.pack(side = BOTTOM)

##    root.quit()     # stops mainloop
##    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

mainloop()
# If you put root.destroy() here, it will cause an error if
# the window is closed with the window manager.
