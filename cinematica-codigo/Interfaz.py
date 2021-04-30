import tkinter as tk
import sympy as sp
import math

raiz=tk.Tk()


raiz.title("Interfaz Robot Scara")
raiz.resizable(0,0)
raiz.geometry("1200x630")
raiz.config(bg="gray")

miFrame=tk.Frame(raiz)

#empaquetar frame
#miFrame.pack(side="top", anchor="s")---> para posicionar el frame
miFrame.pack(fill="both", expand="True")
#miFrame.config(bg="gray")#color del frame
miFrame.config(width="1200", height="630")

miFrame.config(bd=12)
miFrame.config(relief="sunken")
#miFrame.config(cursor="hand2")

#labels
miLabel= tk.Label(miFrame, text="Cinematica directa Robot Scara", fg="red", font=("Comic Sans MS", 10))
miLabel.place(x=30, y=20)

miLabeltheta1= tk.Label(miFrame, text="Dato Theta 1 : ")
miLabeltheta1.place(x=30, y=60)
#cuadro texto
cuadroTextotheta1=tk.Entry(raiz)
cuadroTextotheta1.place(x=130, y=70)
miLabeltheta3= tk.Label(miFrame, text="Dato Theta 3 : ")
miLabeltheta3.place(x=30, y=100)
cuadroTextotheta3=tk.Entry(raiz)
cuadroTextotheta3.place(x=130, y=110)
miLabeltheta4= tk.Label(miFrame, text="Dato Theta 4 : ")
miLabeltheta4.place(x=30, y=140)
cuadroTextotheta4=tk.Entry(raiz)
cuadroTextotheta4.place(x=130, y=150)
miLabeltheta5= tk.Label(miFrame, text="Dato Theta 5 : ")
miLabeltheta5.place(x=30, y=180)
cuadroTextotheta5=tk.Entry(raiz)
cuadroTextotheta5.place(x=130, y=190)
miLabeltheta6= tk.Label(miFrame, text="Dato Theta 6 : ")
miLabeltheta6.place(x=30, y=220)
cuadroTextotheta6=tk.Entry(raiz)
cuadroTextotheta6.place(x=130, y=230)
miLabeld2= tk.Label(miFrame, text="Dato d2 : ")
miLabeld2.place(x=30, y=260)
cuadroTextod2=tk.Entry(raiz)
cuadroTextod2.place(x=130, y=270)
#miLabel.pack()


#acciones boton calcular cinematica directa
def codigoBotonCalcularDirecta():
    #aqui van las ecuaciones de cinematica directa
    L2 = 3.5
    d6 = 0
    d4 = 2

    pmx = L2*sp.cos(float(cuadroTextotheta1.get())*math.pi/180)+d4*sp.sin(float(cuadroTextotheta3.get())*math.pi/180)*sp.cos(float(cuadroTextotheta1.get())*math.pi/180)+d6*((sp.sin(float(cuadroTextotheta1.get())*math.pi/180)*sp.sin(float(cuadroTextotheta4.get())*math.pi/180)+sp.cos(float(cuadroTextotheta1.get())*math.pi/180)*sp.cos(float(cuadroTextotheta3.get())*math.pi/180)*sp.cos(float(cuadroTextotheta4.get())*math.pi/180))*sp.sin(float(cuadroTextotheta5.get())*math.pi/180)-sp.sin(float(cuadroTextotheta3.get())*math.pi/180)*sp.cos(float(cuadroTextotheta1.get())*math.pi/180)*sp.cos(float(cuadroTextotheta5.get())*math.pi/180))
    pmy = L2*sp.sin(float(cuadroTextotheta1.get())*math.pi/180)+d4*sp.sin(float(cuadroTextotheta1.get())*math.pi/180)*sp.sin(float(cuadroTextotheta3.get())*math.pi/180)+d6*((sp.sin(float(cuadroTextotheta1.get())*math.pi/180)*sp.cos(float(cuadroTextotheta3.get())*math.pi/180)*sp.cos(float(cuadroTextotheta4.get())*math.pi/180)-sp.sin(float(cuadroTextotheta4.get())*math.pi/180)*sp.cos(float(cuadroTextotheta1.get())*math.pi/180))*sp.sin(float(cuadroTextotheta5.get())*math.pi/180)-sp.sin(float(cuadroTextotheta1.get())*math.pi/180)*sp.sin(float(cuadroTextotheta3.get())*math.pi/180)*sp.cos(float(cuadroTextotheta5.get())*math.pi/180))
    pmz = float(cuadroTextod2.get())-2*sp.cos(float(cuadroTextotheta3.get())*math.pi/180)+d6*(sp.sin(float(cuadroTextotheta3.get())*math.pi/180)*sp.sin(float(cuadroTextotheta5.get())*math.pi/180)*sp.cos(float(cuadroTextotheta4.get())*math.pi/180)+sp.cos(float(cuadroTextotheta3.get())*math.pi/180)*sp.cos(float(cuadroTextotheta5.get())*math.pi/180))

    posicionfinalx.set("posicion x : "+str(pmx)) 
    posicionfinaly.set("posicion y : "+str(pmy))  
    posicionfinalz.set("posicion z : "+str(pmz)) 

#configuracion boton calcular cinematic directa
botonCalcularDirecta=tk.Button(miFrame, text="Calcular", command=codigoBotonCalcularDirecta)
botonCalcularDirecta.place(x=30, y=290)
botonCalcularDirecta.config(cursor="hand2")
botonCalcularDirecta.config(bg="gray")
#------------------------------------

#acciones boton calcular cinematica Inversa
def codigoBotonLimpiarDirecta():

    posicionfinalx.set("")
    posicionfinaly.set("")
    posicionfinalz.set("")

    cuadroTextotheta1.delete(0,"end")
    cuadroTextotheta3.delete(0,"end")
    cuadroTextotheta4.delete(0,"end")
    cuadroTextotheta5.delete(0,"end")
    cuadroTextotheta6.delete(0,"end")
    cuadroTextod2.delete(0,"end")
    cuadroTextotheta1.focus_set()

#configuracion boton Limpiar cinematic 
botonLimpiarDirecta=tk.Button(miFrame, text="Limpiar", command=codigoBotonLimpiarDirecta)
botonLimpiarDirecta.place(x=90, y=290)
botonLimpiarDirecta.config(cursor="hand2")
botonLimpiarDirecta.config(bg="gray")
#----------------------------------------------


#Resultado cinematica directa
miLabel= tk.Label(miFrame, text="Resultado", fg="red", font=("Comic Sans MS", 10))
miLabel.place(x=350, y=20)


posicionfinalx=tk.StringVar()
miLabelposicionx= tk.Label(miFrame, text="posicion x : ", textvariable=posicionfinalx)
miLabelposicionx.place(x=350, y=60)

posicionfinaly=tk.StringVar()
miLabelposiciony= tk.Label(miFrame, text="posicion y : ", textvariable=posicionfinaly)
miLabelposiciony.place(x=350, y=100)

posicionfinalz=tk.StringVar()
miLabelposicionz= tk.Label(miFrame, text="Posicion z : ", textvariable=posicionfinalz)
miLabelposicionz.place(x=350, y=140)


#cinematica inversa robot scara titulo,labels...
miLabel= tk.Label(miFrame, text="Cinematica Inversa Robot Scara", fg="red", font=("Comic Sans MS", 10))
miLabel.place(x=30, y=330)

miLabelposicionxe= tk.Label(miFrame, text="Dato posicion x : ")
miLabelposicionxe.place(x=30, y=370)
#entrada posicion x
cuadroTextoposicionxe=tk.Entry(raiz)
cuadroTextoposicionxe.place(x=135, y=380)
miLabelposicionye= tk.Label(miFrame, text="Dato posicion y : ")
miLabelposicionye.place(x=30, y=410)
#entrada posicion y
cuadroTextoposicionye=tk.Entry(raiz)
cuadroTextoposicionye.place(x=135, y=420)
miLabelposicionze= tk.Label(miFrame, text="Dato posicion z : ")
miLabelposicionze.place(x=30, y=450)
#entrada posicion z
cuadroTextoposicionze=tk.Entry(raiz)
cuadroTextoposicionze.place(x=135, y=460)

#acciones boton calcular cinematica Inversa
def codigoBotonCalcularInversa():
    #aqui van las ecuaciones de cinematica Inversa
    a4 = 2
    L2 = 3.5
    pmx=float(cuadroTextoposicionxe.get())
    pmy=float(cuadroTextoposicionye.get())
    pmz=float(cuadroTextoposicionze.get())

    #theta 1
    q1i=math.atan(pmy/pmx)
    q1=q1i*180/math.pi

    #theta 3
    q3i=math.acos((pmx*math.cos(q1*math.pi/180)+pmy*math.sin(q1*math.pi/180)-L2)/a4)
    salidaq3=q3i*180/math.pi
    q3=salidaq3+90

    #d2
    d2=pmz-a4*math.sin(salidaq3*math.pi/180)

    #theta 5
    q5i=math.acos(-math.cos(q3*math.pi/180))
    salidaq5i=q5i*180/math.pi

    q5=salidaq5i-180

    #theta 4

    q4i=math.acos(math.sin(q3*math.pi/180)/math.sin(q5*math.pi/180))
    salidaq4i=q4i*180/math.pi

    q4=salidaq4i-180

    #theta 6

    q6i=math.acos(math.sin(q1*math.pi/180)*math.sin(q3*math.pi/180)/math.sin(q5*math.pi/180))
    q6=q6i*180/math.pi

    theta1.set("theta 1 : "+str(q1)) 
    theta3.set("theta 3 : "+str(q3))  
    theta4.set("theta 4 : "+str(q4)) 
    theta5.set("theta 5 : "+str(q5)) 
    theta6.set("theta 6 : "+str(q6)) 
    valord2.set("d2 : "+str(d2)) 





#configuracion boton calcular cinematic Inversa
botonCalcularInversa=tk.Button(miFrame, text="Calcular", command=codigoBotonCalcularInversa)
botonCalcularInversa.place(x=30, y=480)
botonCalcularInversa.config(cursor="hand2")
botonCalcularInversa.config(bg="gray")
#----------------------------------------------

#acciones boton calcular cinematica Inversa
def codigoBotonLimpiarInversa():

    theta1.set("")
    theta3.set("")
    theta4.set("")
    theta5.set("")
    theta6.set("")
    valord2.set("")
    cuadroTextoposicionxe.delete(0,"end")
    cuadroTextoposicionye.delete(0,"end")
    cuadroTextoposicionze.delete(0,"end")
    cuadroTextoposicionxe.focus_set()

#configuracion boton Limpiar cinematic 
botonLimpiarInversa=tk.Button(miFrame, text="Limpiar", command=codigoBotonLimpiarInversa)
botonLimpiarInversa.place(x=90, y=480)
botonLimpiarInversa.config(cursor="hand2")
botonLimpiarInversa.config(bg="gray")
#----------------------------------------------


#Resultado cinematica inversa
miLabel= tk.Label(miFrame, text="Resultado", fg="red", font=("Comic Sans MS", 10))
miLabel.place(x=350, y=330)


theta1=tk.StringVar()
miLabel2= tk.Label(miFrame, text="Theta 1 : ", textvariable=theta1)
miLabel2.place(x=350, y=370)

theta3=tk.StringVar()
miLabel3= tk.Label(miFrame, text="Theta 3 : ", textvariable=theta3)
miLabel3.place(x=350, y=410)

theta4=tk.StringVar()
miLabel4= tk.Label(miFrame, text="Theta 4 : ", textvariable=theta4)
miLabel4.place(x=350, y=450)

theta5=tk.StringVar()
miLabel5= tk.Label(miFrame, text="Theta 5 : ", textvariable=theta5)
miLabel5.place(x=350, y=490)

theta6=tk.StringVar()
miLabel6= tk.Label(miFrame, text="Theta 6 : ", textvariable=theta6)
miLabel6.place(x=350, y=530)

valord2=tk.StringVar()
miLabel7= tk.Label(miFrame, text="d2 : ", textvariable=valord2)
miLabel7.place(x=350, y=560)






#para poner imagen del robot
miImagen=tk.PhotoImage(file="robot.png")
miImagenLabel=tk.Label(miFrame, image=miImagen)
miImagenLabel.place(x=540, y=80)
miImagenLabel.config(bd=6)
miImagenLabel.config(relief="sunken")


raiz.mainloop()