import sys
import pygame 
from scripts.entities import PhysicsEntity
from scripts.utils import load_image
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.collision_area = pygame.Rect(50, 50, 300, 50)

        self.movements = [False, False]

        self.assets = {
       'player': load_image('entities/player.png')
        }


        self.player = PhysicsEntity(self, 'player', (50,50), (8, 15))

    def run(self):
        while True:
            self.screen.fill((14, 219, 248))

            self.player.update((self.movements[1] - self.movements[0], 0))
            self.player.render(self.screen)

         
          
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movements[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movements[1] = False

            pygame.display.update()
            self.clock.tick(60)

Game().run()
