from engine import Game, GameObject
import pygame

class Snake(GameObject):
    def __init__(self, x, y, speed_x, speed_y):
         self._x = x
         self._y = y
         self._speed_x = speed_x
         self._speed_y = speed_y
         

    def draw(self, window):
        pygame.draw.circle(window, pygame.Color(255,0,0), (self._x , self._y), 2)

    def update(self):
        self._y += self._speed_y
        self._x += self._speed_x

    def get_registered_events(self):
        return [pygame.KEYDOWN]

    def notify_event(self, event):
        
        if event.type != pygame.KEYDOWN:
            print("fatal: invalid event received")
            return
        if event.key == pygame.K_LEFT:
            self._speed_x = -1 
            self._speed_y = 0
        elif event.key == pygame.K_RIGHT:
            self._speed_x = 1 
            self._speed_y = 0
        elif event.key == pygame.K_UP:
            self._speed_x = 0 
            self._speed_y = -1
        elif event.key == pygame.K_DOWN:
            self._speed_x = 0 
            self._speed_y = 1

class GreenDot(GameObject):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def draw(self, window):
        pygame.draw.circle(window, pygame.Color(0, 255, 0), (self._x, self._y), 2)

    def update(self):
        pass


class SnakeGame(Game):
    def __init__(self):
        Game.__init__(self, "Snake", 500, 500)
        self._snake = Snake(250, 250, 0, -1) 
        self._dot = GreenDot(200, 200)
        # self.eng.add_object(self._snake)
        self.add_object(self._snake)
        self.add_object(self._dot)
        

    def handle_collission(self, obj1, obj2):
        self._point.change_location()
