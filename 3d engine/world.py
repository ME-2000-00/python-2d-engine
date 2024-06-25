from settings import *
from obj.cube import Cube
from obj.plane import Plane

class World :
    def __init__(self,app) -> None:
        self.cube = Cube(app)
        self.plane = Plane(app)
        self.app = app
        
        # self.cube_2d = []
        # for point in self.cube.vertices :
        #     self.cube_2d.append((point[0] * 10,point[2] * 10))
            
        # self.plane_2d = []
        # for point in self.cube.vertices :
        #     self.plane_2d.append((point[0] * 10,point[2] * 10)) 
        
        self.size = 30   
        self.draw_2d = False

    def render(self) -> None:
        self.plane.render()
        self.cube.render()  
        
        if self.draw_2d :
        
            for point in self.cube.vertices :
                pg.draw.circle(self.app.screen,(255,255,255),(translate(point[0] * self.size,self.app.H_WIN[0]),translate(point[2] * self.size,self.app.H_WIN[1])),5)

            
            pg.draw.circle(self.app.screen,pg.Color('yellow'),(translate(PLAYER_POS[0] * self.size,self.app.H_WIN[0]),translate(PLAYER_POS[2] * self.size,self.app.H_WIN[1])),10)
            pg.draw.line(self.app.screen,pg.Color('orange'),
                         (translate(PLAYER_POS[0] * self.size,self.app.H_WIN[0]),translate(PLAYER_POS[2] * self.size,self.app.H_WIN[1])),
                         (translate(PLAYER_POS[0] * self.size,self.app.H_WIN[0]),translate(PLAYER_POS[2] * self.size,self.app.H_WIN[1]) + self.size)
                         ,2)
            
                
            for point in self.plane.vertices :
                pg.draw.circle(self.app.screen,(255,255,255),(translate(point[0] * self.size,self.app.H_WIN[0]),translate(point[2] * self.size,self.app.H_WIN[1])),5)
            

    def update(self) -> None:
        self.plane.update()
        self.cube.update()