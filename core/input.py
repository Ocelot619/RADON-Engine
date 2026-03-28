import pygame

class Input(object):

    def __init__(self):

        # has the user quit the app?
        self.quit = False

    def update(self):
        # to iterate over user input
        #   that occured since last time events checked 
        for event in pygame.event.get():
            #quit event occurs by clicking button to close the window
            if event.type == pygame.QUIT:
                self.quit = True
                