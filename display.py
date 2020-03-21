import sdl2
import sdl2.ext

class Display(object):
    def __init__(self, width, height):
        sdl2.ext.init()

        self.width = width
        self.height = height
        self.window = sdl2.ext.Window("crappySLAM", size=(width, height), position=(200,100))
        self.window.show()

    def paint(self, img):
        events = sdl2.ext.get_events()
        for event in events:
            if event.type ==sdl2.SDL_QUIT:
                exit(0)
            #print(dir(window))
        surf = sdl2.ext.pixels3d(self.window.get_surface())
        surf[:,:,0:3] = img.swapaxes(0,1)
        self.window.refresh()