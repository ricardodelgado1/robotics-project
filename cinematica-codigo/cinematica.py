import sympy as sp
import math
#import numpy as np
#import matplotlib.pyplot as plt
"""
variables articulares

"""
sq = sp.symbols(['q1','q2','q3´','q4´','q5´','q6','d2','d4','d6','L2'])

#se define las funciones para obtener matrices de transformacion simbolica 

def symTfromDH(theta, di, ai, alpha):
    #theta y alpha en radianes 
    #d y a en metros (o la medida que se necesite)
    Rz = sp.Matrix([[sp.cos(theta), -sp.sin(theta), 0, 0],
                    [sp.sin(theta), sp.cos(theta), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]) 

    tz = sp.Matrix([[1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [0, 0, 1, di],
                    [0, 0, 0, 1]])

    ta = sp.Matrix([[1, 0, 0, ai],
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]]) 

    Rx = sp.Matrix([[1, 0, 0, 0],
                    [0, sp.cos(alpha), -sp.sin(alpha), 0],
                    [0, sp.sin(alpha), sp.cos(alpha), 0],
                    [0, 0, 0, 1]])                                              

    T=Rz*tz*ta*Rx
    return T


#obtenemos la cinematica directa

#Aqui
#q3' = 90 + q3
#q4' = 180+ q4
#q5' = 180+ q5

#  Articulacion     |    theta      |       d       |       a       |  alpha      
#-----------------------------------------------------------------------------------
#       1           |     0+q1      |       0       |       0       |    0
#       2           |      0        |       d2      |       L2      |    90
#       3           |      q3'      |       0       |        0      |    90
#       4           |      q4´      |       d4      |        0      |    90   
#       5           |      q5'      |       0       |        0      |    90
#       6           |      q6       |       d6      |        0      |    0


#la matriz de transformacion homogenea desde la base 




T = sp.simplify(symTfromDH(sq[0],0,0,0)*
                symTfromDH(0,sq[4],sq[6],sp.pi/2)*
                symTfromDH(sq[2],0,0,sp.pi/2)*
                symTfromDH(sq[3],sq[7],0,sp.pi/2)*
                symTfromDH(sq[4],0,0,sp.pi/2)*
                symTfromDH(sq[5],sq[8],0,0) )


T              


# lo anterior sirve para multiplicar las matrices y utilizar el valor final para 
#calcular las posiciones final del robot
#ahora calculamos las posiciones 


#posiciones finales sera

#valores variables
#datos ingresados por el usuario desde la interfaz
#posiciones finales sera

#valores variables
L2= 3.5
d2=1.92
d4=2
d6=0
q1=45
q3=43.5
q4=-180
q5=-133.5
q6=45

pmx = L2*sp.cos(q1*math.pi/180)+d4*sp.sin(q3*math.pi/180)*sp.cos(q1*math.pi/180)+d6*((sp.sin(q1*math.pi/180)*sp.sin(q4*math.pi/180)+sp.cos(q1*math.pi/180)*sp.cos(q3*math.pi/180)*sp.cos(q4*math.pi/180))*sp.sin(q5*math.pi/180)-sp.sin(q3*math.pi/180)*sp.cos(q1*math.pi/180)*sp.cos(q5*math.pi/180))


pmy = L2*sp.sin(q1*math.pi/180)+d4*sp.sin(q1*math.pi/180)*sp.sin(q3*math.pi/180)+d6*((sp.sin(q1*math.pi/180)*sp.cos(q3*math.pi/180)*sp.cos(q4*math.pi/180)-sp.sin(q4*math.pi/180)*sp.cos(q1*math.pi/180))*sp.sin(q5*math.pi/180)-sp.sin(q1*math.pi/180)*sp.sin(q3*math.pi/180)*sp.cos(q5*math.pi/180))


pmz = d2-d4*sp.cos(q3*math.pi/180)+d6*(sp.sin(q3*math.pi/180)*sp.sin(q5*math.pi/180)*sp.cos(q4*math.pi/180)+sp.cos(q3*math.pi/180)*sp.cos(q5*math.pi/180))

pmx,pmy,pmz


#-----------------------------------------------------------------------------------------------------------------

#cinematica inversa
#Ecuaciones

#entradas desde la imterfaz pmx,pmy,pmz

pmx=3.5
pmy=3.5
pmz=4

a4=2
L2=3.5

#theta 1
q1i=math.atan(pmy/pmx)
q1=q1i*180/math.pi

#theta 3
q3i=math.acos((pmx*math.cos(q1*math.pi/180)+pmy*math.sin(q1*math.pi/180)-L2)/a4)
salidaq3=q3i*180/math.pi
q3=salidaq3+90

#d2
d2=pmz-a4*math.sin(q3*math.pi/180)

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




q1,q3,q4,q5,q6,d2