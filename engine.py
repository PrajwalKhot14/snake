import pygame
from collections import defaultdict
import math

class GameObject:
    def __init__(self):
        pass

    def draw(self, window):
        raise Exception("not implemented")

    def update(self):
        raise Exception("not implemented")
    
    def get_registered_events(self):
        '''
        Returns:
            List<EventTypes>: List of events to listen to
        '''
        return []

    def notify_event(self, event):
        raise Exception("not implemented")

    def hit_box(self):
        raise Exception('not implemented')
        return (x, y, r)

class Game:
    def __init__(self, caption, window_height, window_width):
        pygame.init()
        self._window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption(caption)
        self._game_objects = []
        self._event_types_to_gos = defaultdict(list)

    def add_object(self, game_object):
        self._game_objects.append(game_object)
        events = game_object.get_registered_events()
        for event in events:
            self._event_types_to_gos[event].append(game_object)

    def run(self):
        running = True
        while running:

            # Clear and render
            self._window.fill(pygame.Color("white"))
            self.__draw_objects()

            # Find events and dispatch
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                interested_objects = self._event_types_to_gos[event.type]
                for obj in interested_objects:
                    obj.notify_event(event)

            # Update loop
            self.__update_objects()
            self.__detect_collission()

            pygame.display.flip()

            # Detect collission
            # Find object hit boxes
            # Find intersecting hit boxes
            # for ever intersecting hit box
            #   call collission_receiver.notify_collission(obj1, obj2)

        pygame.quit()

    def __detect_collission(self):
        corr = [(x.hit_box(), x) for x in self._game_objects]
        for i in range(len(corr)):
            hdi, obji = corr[i]
            x1, y1, r1 = hdi
            for j in range(i+1, len(corr)):
                hdj, objj = corr[j]
                x2, y2, r2 = hdj

                r = r1 + r2
                dist = math.sqrt(math.pow(x2-x1, 2)+ math.pow(y2-y1, 2))

                if dist <= r:
                    self.handle_collission(obji, objj)


    def handle_collission(self, obj1, obj2):
        pass

    def __draw_objects(self):
        for go in self._game_objects:
            go.draw(self._window)

    def __update_objects(self):
        for go in self._game_objects:
            go.update()

    def __game_score(self, count):
        pass



# r < sqrt((r.x-g.x)^2, (r.y))