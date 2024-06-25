from settings import *

class BaseMesh :
    def __init__(self,app) -> None:
        self.app = app
        self.screen = app.screen
        self.vertices: list = []
        self.triangles: list = []
        self.ang: float = 0.005
        self.wire_frame: bool = True
        self.distances: list = []
        
        self.offsets = (0,0,0)
        
        self.local_coords: list = [
            (0,0,0),
            (2,0,0),
            (0,-2,0),
            (0,0,2),
        ]
        self.local_lines: list = [
            (0,1,"red"),
            (0,2,"green"),
            (0,3,"blue")
        ]
        
        self.colors = [
            pg.Color("orange")
        ]
        
        self.tri_mids: list = []
        self.draw: list = [False,False]
        
    def create_triangle_middlepoints(self) :
        self.tri_mids: list = []
        for tri in self.triangles :
            x = (self.vertices[tri[0]][0] + self.vertices[tri[1]][0] + self.vertices[tri[2]][0]) / 3
            y = (self.vertices[tri[0]][1] + self.vertices[tri[1]][1] + self.vertices[tri[2]][1]) / 3
            z = (self.vertices[tri[0]][2] + self.vertices[tri[1]][2] + self.vertices[tri[2]][2]) / 3
            
            self.tri_mids.append((x,y,z,self.triangles.index(tri)))

    def render(self) : 
        for tri in self.triangles :
            points = []
            count = 0
            for vert in tri :
                out = if_outside_of_view(self.vertices[vert],self.app.WIN,100,300)
                # print(out)
                if not out :
                    count += 1
                else :
                    points.append(out)
            
            if len(points) >= 3 and count == 0 and near_far_plane(tri,self.vertices):
                pg.draw.polygon(
                    self.screen,
                    pg.Color("orange"),
                    points,
                )
            
                pg.draw.polygon(
                    self.screen,
                    pg.Color("black"),
                    points,
                    1
                )
        
        if self.draw[0] :
            for vert in self.tri_mids :
                pg.draw.circle(self.screen,(255,255,255),to_2d(vert[0],vert[1],vert[2],self.app.WIN,100,300),5)
                    
        if self.draw[1] :
            for vert in self.vertices :
                pg.draw.circle(self.screen,(255,255,255),to_2d(vert[0],vert[1],vert[2],self.app.WIN,100,300),5)                  
                    

    def update(self) :
        self.sort_triangles()
        # rotation of object and coordinatesystem 
        for vertex in self.vertices :
            self.vertices[self.vertices.index(vertex)] = rotateY(vertex[0],vertex[1],vertex[2],self.ang)
        for vertex in self.local_coords :
            self.local_coords[self.local_coords.index(vertex)] = rotateY(vertex[0],vertex[1],vertex[2],self.ang)
    
    njit(fastmath=True)
    def sort_triangles(self) :
        # TODO: fix this mess
        self.distances: list = []
        old_tris: list = []
        self.create_triangle_middlepoints()
        
        for mid in self.tri_mids :
            self.distances.append([dist(PLAYER_POS,mid[:3]),mid[-1]])
        
        self.distances.sort(reverse=True)
        
        old_tris = self.triangles
        
        self.triangles = []
        for dis in self.distances :
            self.triangles.append(old_tris[dis[-1]])    
