import pygame as pg
from math import *
import numpy as np
from numba import njit
from random import *
import win32api #type:ignore    scanerror of vscode
import win32con #type:ignore    
import win32gui #type:ignore

pg.font.init()
FONT = pg.font.SysFont('Arial', 30, bold=True)
FUCHSIA = (255, 0, 128) 
BG = pg.Color("darkslategray")

PLAYER_POS = (0,0,-2)
FORWARD = (0,0,1)
NEAR = 0.01
FAR = 10

offsetZ = 0
offsetY = 0
offsetX = 8

#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------  #  

@njit(fastmath=True)
def to_2d(x,y,z,screen_size: tuple,scale_size: int, value: int = 300) -> tuple:
    x *= scale_size
    y *= scale_size
    z *= scale_size
    
    """ converts 3d points to 2d screen space   ( i guess ) """
    
    z = value/((value + z) + .001)
    return (
     x * z + screen_size[0] // 2, y * z + screen_size[1] // 2
    )

#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------  #  

def if_outside_of_view(three_D_point:tuple, screen_size: tuple,scale_size: int, value: int = 300) -> bool:
    '''
        checks if a 3d point is inside of view and if not returns False otherwise returns the point in 2d screen space
    '''
    z = (value/((value + three_D_point[2] * scale_size) + .001))
    # print(f"Z: {z}")
    # print(z)
    if z >= -0.5 :
        
        return to_2d(three_D_point[0],three_D_point[1],three_D_point[2],screen_size,scale_size,value)
    
    else :
        
        return False
        
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------  #  
    

@njit(fastmath=True)
def rotateY(x,y,z,ang) :
    """ rotates vertex around the world origin """
    sin_var = sin(ang)
    cos_var = cos(ang)
    
    temp = (x * cos_var) - (z * sin_var)
    
    return (
        temp,
        y,
       (x * sin_var) + (z * cos_var) 
    )

#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------  #  

def to_mouse(vertices: list):
    new_verts = []
    for vertex in vertices :
        new_vert = [0,0,vertex[2]]
        new_vert[0] = vertex[0] + pg.mouse.get_pos()[0]
        new_vert[1] = vertex[1] + pg.mouse.get_pos()[1]
        new_verts.append(new_vert)
    return new_verts     

#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------  #

def near_far_plane(tri: list,vertices: list) -> bool:
    count = 0
    for vertex in tri :
        v = vertices[vertex]
        d1 = dist(PLAYER_POS,v)
        if d1 <= FAR :
            count += 1
    
    if count == 3 :
        return True
    else :
        return False
    
#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------  #  
            
def to_list(np_array: np.ndarray) :
    '''
        ! only use for vertices and triangles !
    '''
    list_of_items: list = []
    for item in np_array :
        print(type(item))
        a = int(item[0])
        b = int(item[1])
        c = int(item[2])
        print(type(a))
        list_of_items.append([a,b,c])
        
    print(list_of_items)
    
    return list_of_items

#  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------  #  

def translate(point, offset) :
    return point + offset
    