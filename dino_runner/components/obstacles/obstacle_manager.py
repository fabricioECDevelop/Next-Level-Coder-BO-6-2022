import pygame
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS,BIRD

class Obstacle_manager():
     def __init__(self) :
          self.obstacles = []
          
     def update (self,game_speed,game):
          if len (self.obstacles)==0:
               self.obstacles.append(Cactus(SMALL_CACTUS))
               self.obstacles.append(Bird(BIRD))
               
          for obstacle in self.obstacles:
               obstacle.update(game_speed,self.obstacles)
               if game.player.dino_rect.colliderect(obstacle.rect):
                    pygame.time.delay(500)
                    game.playing = False
                    break
     def draw (self,screen):
          for obstacle in self.obstacles:
               obstacle.draw(screen)