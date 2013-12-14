# -*- coding: utf-8 -*-
from visual import *
from math import *

scene.title = "Oscilações - Massa Mola"
scene.range = (16,12,12)
scene.center = (0,0,0)
scene.width = 800
scene.height = 600

parede1 = box(pos = (-12.5,3,0), size = (0.5,26,7))
parede2 = box(pos = (12.5,3,0), size = (0.5,26,7))

# Primeira linha
bloco1 = box (pos=(-5,9,0), size=(2,2,2),color=color.white)
bloco2 = box (pos=(0,9,0), size=(2,2,2),color=color.white)
bloco3 = box (pos=(5,9,0), size=(2,2,2),color=color.white)
 
mola1 = helix(pos=(-12,9,0),axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola2 = helix(pos=bloco1.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola3 = helix(pos=bloco2.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola4 = helix(pos=bloco3.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)

# Segunda linha
bloco4 = box (pos=(-5,6,0), size=(2,2,2),color=color.white)
bloco5 = box (pos=(0,6,0), size=(2,2,2),color=color.white)
bloco6 = box (pos=(5,6,0), size=(2,2,2),color=color.white)

mola5 = helix(pos=(-12,6,0),axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola6 = helix(pos=bloco4.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola7 = helix(pos=bloco5.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola8 = helix(pos=bloco6.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)

#Terceira linha
bloco7 = box (pos=(-5,3,0), size=(2,2,2),color=color.white)
bloco8 = box (pos=(0,3,0), size=(2,2,2),color=color.white)
bloco9 = box (pos=(5,3,0), size=(2,2,2),color=color.white)

mola9 = helix(pos=(-12,3,0),axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola10 = helix(pos=bloco7.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola11 = helix(pos=bloco8.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola12 = helix(pos=bloco9.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)

#Quarta linha
bloco10 = box (pos=(-5,0,0), size=(2,2,2),color=color.white)
bloco11 = box (pos=(0,0,0), size=(2,2,2),color=color.white)
bloco12 = box (pos=(5,0,0), size=(2,2,2),color=color.white)

mola13 = helix(pos=(-12,0,0),axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola14 = helix(pos=bloco10.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola15 = helix(pos=bloco11.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola16 = helix(pos=bloco12.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)

#Quinta linha
bloco13 = box (pos=(-5,-3,0), size=(2,2,2),color=color.white)
bloco14 = box (pos=(0,-3,0), size=(2,2,2),color=color.white)
bloco15 = box (pos=(5,-3,0), size=(2,2,2),color=color.white)

mola17 = helix(pos=(-12,-3,0),axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola18 = helix(pos=bloco13.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola19 = helix(pos=bloco14.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola20 = helix(pos=bloco15.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)

#Sexta linha
bloco16 = box (pos=(-5,-6,0), size=(2,2,2),color=color.white)
bloco17 = box (pos=(0,-6,0), size=(2,2,2),color=color.white)
bloco18 = box (pos=(5,-6,0), size=(2,2,2),color=color.white)

mola21 = helix(pos=(-12,-6,0),axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola22 = helix(pos=bloco16.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola23 = helix(pos=bloco17.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)
mola24 = helix(pos=bloco18.pos,axis=7, radius=0.5,coils=8,thickness=0.1,color=color.white)

x1 = 1.
x2 = 2.
x3 = -1.
x4 = 0.
x5 = 1.
x6 = 2.
x7 = -1.
x8 = 0.
x9 = 1.
x10 = 2.
x11 = -1.
x12 = 0.
x13 = 1.
x14 = 2.
x15 = -1.
x16 = 0.
x17 = 1.
x18 = 2.
x19 = -1.

k = 1.
m = 5.
dt = 0.1

v1 = 0.
v2 = 0.
v3 = 0.
v4 = 0.
v5 = 0.
v6 = 0.
v7 = 0.
v8 = 0.
v9 = 0.
v10 = 0.
v11 = 0.
v12 = 0.
v13 = 0.
v14 = 0.
v15 = 0.
v16 = 0.
v17 = 0.
v18 = 0.

while (1):
    rate (100)
    
    a1 = k/m*(x2 - 2*x1)
    a2 = k/m*(x3 - 2*x2 + x1)
    a3 = k/m*(x4 - 2*x3 + x2)
    a4 = k/m*(x5 - 2*x4 + x3)
    a5 = k/m*(x6 - 2*x5 + x4)
    a6 = k/m*(x7 - 2*x6 + x5)
    a7 = k/m*(x8 - 2*x7 + x6)
    a8 = k/m*(x9 - 2*x8 + x7)
    a9 = k/m*(x10 - 2*x9 + x8)
    a10 = k/m*(x11 - 2*x10 + x9)
    a11 = k/m*(x12 - 2*x11 + x10)
    a12 = k/m*(x13 - 2*x12 + x11)
    a13 = k/m*(x14 - 2*x13 + x12)
    a14 = k/m*(x15 - 2*x14 + x13)
    a15 = k/m*(x16 - 2*x15 + x14)
    a16 = k/m*(x17 - 2*x16 + x15)
    a17 = k/m*(x18 - 2*x17 + x16)
    a18 = k/m*(x19 - 2*x18 + x17)
    
    v1 += a1*dt
    v2 += a2*dt
    v3 += a3*dt
    v4 += a4*dt
    v5 += a5*dt
    v6 += a6*dt
    v7 += a7*dt
    v8 += a8*dt
    v9 += a9*dt
    v10 += a10*dt
    v11 += a11*dt
    v12 += a12*dt
    v13 += a13*dt
    v14 += a14*dt
    v15 += a15*dt
    v16 += a16*dt
    v17 += a17*dt
    v18 += a18*dt
        
    x1 += v1*dt
    x2 += v2*dt
    x3 += v3*dt
    x4 += v4*dt
    x5 += v5*dt
    x6 += v6*dt
    x7 += v7*dt
    x8 += v8*dt
    x9 += v9*dt
    x10 += v10*dt
    x11 += v11*dt
    x12 += v12*dt
    x13 += v13*dt
    x14 += v14*dt
    x15 += v15*dt
    x16 += v16*dt
    x17 += v17*dt
    x18 += v18*dt
    
    #Primeira linha
    bloco1.pos.x = x1-5
    bloco2.pos.x = x2
    bloco3.pos.x = x3+5
    
    mola2.pos = bloco1.pos
    mola3.pos = bloco2.pos
    mola4.pos = bloco3.pos
    
    mola1.axis = bloco1.pos.x-parede1.pos.x
    mola2.axis = bloco2.pos.x-bloco1.pos.x
    mola3.axis = bloco3.pos.x-bloco2.pos.x
    mola4.axis = parede2.pos.x-bloco3.pos.x
    
    #Segunda linha
    bloco4.pos.x = x4-5
    bloco5.pos.x = x5
    bloco6.pos.x = x6+5
    
    mola5.pos = bloco4.pos
    mola6.pos = bloco5.pos
    mola7.pos = bloco6.pos
    mola8.pos = (parede2.pos.x,bloco6.pos.y,0)
    
    mola5.axis = parede1.pos.x-bloco4.pos.x
    mola6.axis = bloco4.pos.x-bloco5.pos.x
    mola7.axis = bloco5.pos.x-bloco6.pos.x
    mola8.axis = bloco6.pos.x-parede2.pos.x
    
    #Terceira linha
    bloco7.pos.x = x7-5
    bloco8.pos.x = x8
    bloco9.pos.x = x9+5
    
    mola9.pos = bloco7.pos
    mola10.pos = bloco8.pos
    mola11.pos = bloco9.pos
    mola12.pos = (parede2.pos.x,bloco9.pos.y,0)
    
    mola9.axis = parede1.pos.x-bloco7.pos.x
    mola10.axis = bloco7.pos.x-bloco8.pos.x
    mola11.axis = bloco8.pos.x-bloco9.pos.x
    mola12.axis = bloco9.pos.x-parede2.pos.x
    
    #Quarta linha
    bloco10.pos.x = x10-5
    bloco11.pos.x = x12
    bloco12.pos.x = x12+5
    
    mola13.pos = bloco10.pos
    mola14.pos = bloco11.pos
    mola15.pos = bloco12.pos
    mola16.pos = (parede2.pos.x,bloco12.pos.y,0)
    
    mola13.axis = parede1.pos.x-bloco10.pos.x
    mola14.axis = bloco10.pos.x-bloco11.pos.x
    mola15.axis = bloco11.pos.x-bloco12.pos.x
    mola16.axis = bloco12.pos.x-parede2.pos.x
    
    #Quarta linha
    bloco13.pos.x = x13-5
    bloco14.pos.x = x14
    bloco15.pos.x = x15+5
    
    mola17.pos = bloco13.pos
    mola18.pos = bloco14.pos
    mola19.pos = bloco15.pos
    mola20.pos = (parede2.pos.x,bloco15.pos.y,0)
    
    mola17.axis = parede1.pos.x-bloco13.pos.x
    mola18.axis = bloco13.pos.x-bloco14.pos.x
    mola19.axis = bloco14.pos.x-bloco15.pos.x
    mola20.axis = bloco15.pos.x-parede2.pos.x
    
    #Quinta linha
    bloco16.pos.x = x16-5
    bloco17.pos.x = x17
    bloco18.pos.x = x18+5
    
    mola21.pos = bloco16.pos
    mola22.pos = bloco17.pos
    mola23.pos = bloco18.pos
    mola24.pos = (parede2.pos.x,bloco18.pos.y,0)
    
    mola21.axis = parede1.pos.x-bloco16.pos.x
    mola22.axis = bloco16.pos.x-bloco17.pos.x
    mola23.axis = bloco17.pos.x-bloco18.pos.x
    mola24.axis = bloco18.pos.x-parede2.pos.x