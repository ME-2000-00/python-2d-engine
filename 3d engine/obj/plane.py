from settings import *
from obj.base_mesh import BaseMesh

class Plane(BaseMesh) :
    def __init__(self,app) -> None:
        super().__init__(app)
        self.size = 2.1
        self.subs = 5
        
        self.vertices = [
            (self.size ,2, self.size ),
            (-self.size ,2, self.size ),
            (-self.size ,2, -self.size ),
            (self.size ,2, -self.size )
        ]
        
        self.triangles = [
            (0,1,2),
            (0,2,3)
        ]
        
        self.create_triangle_middlepoints()
        self.sort_triangles()