from settings import *
from obj.base_mesh import BaseMesh

class Cube(BaseMesh) :
    def __init__(self,app) -> None:
        super().__init__(app)
        
        self.app = app
        self.vertices = [
            (1 + offsetX,1,-1),(1 + offsetX,-1,-1),(-1 + offsetX,-1,-1),(-1 + offsetX,1,-1),
            (1 + offsetX,1,1),(1 + offsetX,-1,1),(-1 + offsetX,-1,1),(-1 + offsetX,1,1),
            
        ]
        self.triangles = [
            (0,1,2),(0,2,3),
            (4,5,6),(4,6,7),
            (3,2,7),(2,6,7),
            (4,5,0),(5,1,0),
            (1,5,2),(5,6,2),
            (4,0,3),(4,7,3),
            (5,4,6),(4,7,6),
            
        ]

        self.create_triangle_middlepoints()
        self.sort_triangles()