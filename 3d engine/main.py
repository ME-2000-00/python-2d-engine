from settings import *
from world import World

class Engine:
    def __init__(self) -> None:
        
        """
            pygame 3d rendering engine made by ME-2000-00
        """
        
        # pg screen
        self.screen = pg.display.set_mode((0,0),pg.FULLSCREEN|pg.NOFRAME)    # 
        
        # window resolution
        self.WIN = self.width, self.height = (self.screen.get_width(),self.screen.get_height())
        self.H_WIN = (self.width // 2, self.height // 2)
    
        # clock
        self.clock = pg.time.Clock()
        self.dt = 0
        
        # world class
        self.world = World(self)
        
        self.fps = FONT.render(f"FPS: {self.clock.get_fps()}",True,pg.Color("white"))
        
        pg.event.set_grab(True)
    
        # Create layered window
        hwnd = pg.display.get_wm_info()["window"]
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                            win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        # Set window transparency color
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*FUCHSIA), 0, win32con.LWA_COLORKEY)
    
    def on_new_frame(self) :
        return 
        # set mouse to the middle of the screen
        if pg.mouse.get_pos() != self.H_WIN:
            pg.mouse.set_pos(self.H_WIN)
        
    def render(self) -> None:
        # fill screen in darkslategray
        self.screen.fill(BG)
        self.world.render()
        self.screen.blit(self.fps,(self.width - 150,10))
            
    def update(self) -> None:
        self.fps = FONT.render(f"FPS: {int(self.clock.get_fps())}",True,pg.Color("white"))
        # fps limit and screen update
        self.clock.tick(120)
        self.dt = self.clock.tick()
        # print(self.dt)
        pg.display.update()
        
        self.world.update()
    
    def events(self) -> None:
        # events
        for e in pg.event.get() :
            # quit event
            if e.type == pg.QUIT or e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE :
                quit()
    
    def run(self) -> None:
        # main loop
        while True :
            self.on_new_frame()
            self.render()
            self.update()
            self.events()

if __name__ == '__main__' :
    # initialise engine class and run engine class 
    app = Engine()
    app.run()
