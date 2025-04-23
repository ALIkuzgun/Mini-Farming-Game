import pygame, random, sys
from map import *

class Map():
    def __init__(self, x, y):        
        self.image = pygame.image.load('img/farmmap.png')
        self.rect = pygame.Rect(x, y, 2240, 2240)

    def draw(self):
        ekran.blit(self.image,self.rect)

class Wall():
    def __init__(self, x, y, en, boy):        
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.rect = pygame.Rect(x, y, self.en, self.boy)

    def draw(self):
        pygame.draw.rect(ekran,('#00C000'),self.rect)

class Soil():  
    def __init__(self, x, y, en, boy):  
        self.images = {
            'img': pygame.image.load('img/soilimgs.png'),
        }
        self.endimage = self.images["img"].subsurface(pygame.Rect(0, 0, 32, 32)) 
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.hoed = 0
        self.wet = 0
        self.potato = 0
        self.carrot = 0
        self.onion = 0
        self.animation_time = 0
        self.animation_frame = 0        
        self.time = 0    
        self.oniontime = 0
        self.potato_imgs = [(256, 0, 32, 32),(288, 0, 32, 32),(320, 0, 32, 32),(352, 0, 32, 32),(384, 0, 32, 32)]
        self.carrot_imgs = [(96, 0, 32, 32),(128, 0, 32, 32),(160, 0, 32, 32),(192, 0, 32, 32),(224, 0, 32, 32)]
        self.onion_imgs = [(416, 0, 32, 32),(448, 0, 32, 32),(480, 0, 32, 32),(512, 0, 32, 32),(544, 0, 32, 32)]

    def draw(self):
        if player.level == 5:
            self.time += 1
            if self.time < 70:
                player.number_carrot = 3
                player.player_move = 0
                player.carrot = 1
                text = pygame.font.Font(None, 50).render("Carrot Opened", True, (0,0,0))
                ekran.blit(text,(273,213))
            else:
                player.player_move = 1
        if player.level == 10:
            self.oniontime += 1
            if self.oniontime < 70:
                player.number_onion = 3
                player.player_move = 0
                player.onion = 1
                text = pygame.font.Font(None, 50).render("Onion Opened", True, (0,0,0))
                ekran.blit(text,(273,213))
            else:
                player.player_move = 1
        ekran.blit(self.endimage,self.rect)

class Player():
    def __init__(self, x, y, en, boy, speed):  
        self.images = {
            'idle': pygame.image.load('img/playerıdle.png'),
            'walk': pygame.image.load('img/playerwalk.png'),
            'hoed': pygame.image.load('img/playerimgs.png'),
            'fishing': pygame.image.load('img/playerfishing.png'),
            'irrigation': pygame.image.load('img/playerirrigationleft.png')
        }
        self.endimage = self.images["idle"].subsurface(pygame.Rect(0, 0, 39, 42)) 
        self.x = x
        self.y = y
        self.en = en
        self.boy = boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.speed = speed
        self.bed = 0
        self.on_ground = False 
        self.move_direction = "stay"
        self.direction = "right"
        self.move_status = 0
        self.level, self.level_bar_width, self.level_bar_height = 1, 95, 24
        self.xp, self.max_xp = 0, 95
        self.animation_time = 0
        self.animation_frame, self.hoedanimation_frame, self.irrigationanimation_frame, self.fishing_rodanimation_frame= 0, 0, 0, 0
        self.money = 0
        self.game_click = 1
        self.fishing_rod_imgs = [(0, 33, 33, 42),(54, 18, 33, 42),(117, 24, 39, 42),(156, 30, 33, 39),(249, 21, 33, 39),(348, 0, 33, 42)]
        self.right_imgs,self.left_imgs = [(0, 0, 39, 42),(39, 0, 39, 42),(78, 0, 39, 42),(117, 0, 33, 42),(150, 0, 33, 42),(183, 0, 33, 42),(216, 0, 33, 42),(249, 0, 33, 42)],[(0, 126, 39, 42),(39, 126, 39, 42),(78, 126, 39, 42),(117, 126, 33, 42),(150, 126, 33, 42),(183, 126, 33, 42),(216, 126, 33, 42),(249, 126, 33, 42)]
        self.down_imgs,self.up_imgs = [(0, 42, 39, 42),(39, 42, 39, 42),(78, 42, 39, 42),(117, 42, 39, 42),(156, 42, 39, 42),(195, 42, 39, 42),(234, 42, 39, 42),(273, 42, 39, 42)],[(0, 84, 39, 42),(39, 84, 39, 42),(78, 84, 39, 42),(117, 84, 39, 42),(156, 84, 39, 42),(195, 84, 39, 42),(234, 84, 39, 42),(273, 84, 39, 42)]
        self.hoed_imgs, self.irrigation_imgs, self.irrigation_imgs2 = [(0, 0, 48, 42),(48, 0, 54, 48),(102, 0, 54, 38),(156, 0, 54, 38)],[(210, 0, 42, 39),(252, 0, 69, 39)],[(9, 0, 33, 39),(78, 0, 33, 39)]
        self.player_wall_hit = 0
        self.player_wall_hit = 0
        self.hoed, self.hoedtime = 0, 0
        self.tuş1, self.tuş2, self.tuş3, self.tuşp, self.tuşc, self.tuşo, self.tuşe = 0, 0, 0, 0, 0, 0, 0
        self.wet = 0
        self.irrigation,self.irrigationtime = 0,0
        self.fishing_rod, self.fishing_rodtime, self.fishing, self.fishing_hit = 0, 0, 0, 0
        self.player_move = 1
        self.fish_number = random.randint(1,100)
        self.player_number = random.randint(1,100)
        self.click = 0
        self.mini_game = 1
        self.player_point = 0
        self.fish_time = 0
        self.bagpack = 0
        self.item_1, self.item_2, self.item_3, self.item_4, self.item_5, self.item_6, self.item_7 = "", "", "", "", "", "", ""
        self.number__of_item_1, self.number__of_item_2, self.number__of_item_3, self.number__of_item_4, self.number__of_item_5, self.number__of_item_6, self.number__of_item_7 = 0, 0, 0, 0, 0, 0, 0
        self.fish_type = random.choice(['Perch','Angler','Perch','Perch','Perch','Perch','Perch','Tuna','Tuna','Tuna'])
        self.onion, self.carrot, self.potato = 0, 0, 0
        self.number_onion, self.number_carrot, self.number_potato = 0, 0, 3
        self.perch, self.angler, self.tuna = 0, 0, 0
        self.number_perch, self.number_angler, self.number_tuna = 0, 0, 0

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_p]:
            self.tuşp = 1
        else:
            self.tuşp = 0

        if key[pygame.K_e]:
            self.tuşe = 1
        else:
            self.tuşe = 0

        if key[pygame.K_c]:
            self.tuşc = 1
        else:
            self.tuşc = 0

        if key[pygame.K_o]:
            self.tuşo = 1
        else:
            self.tuşo = 0

        if key[pygame.K_1]:
            self.tuş1 = 1
            self.tuş2 = 0
            self.tuş3 = 0

        if key[pygame.K_2]:
            self.tuş2 = 1
            self.tuş1 = 0
            self.tuş3 = 0

        if key[pygame.K_3]:
            self.tuş3 = 1
            self.tuş1 = 0
            self.tuş2 = 0

        if key[pygame.K_SPACE] and self.hoed == 0 and self.irrigation == 0 and self.fishing_rod == 0:  
            if self.tuş1 == 1 and self.tuş2 == 0 and self.tuş3 == 0:
                self.hoed = 1
                self.animation_time = 0
                self.animation_frame = 0
            elif self.tuş2 == 1 and self.tuş1 == 0 and self.tuş3 == 0:
                self.hoed = 0
                irrigation.irrigationanimation_frame = 0
                irrigation.animation_time = 0
                irrigation.animation_frame = 0  
                self.irrigation = 1
                self.animation_time = 0
                self.animation_frame = 0
            elif self.tuş3 == 1 and self.tuş2 == 0 and self.tuş1 == 0:
                self.hoed = 0
                fishing_rod.fishing_rodanimation_frame = 0
                fishing_rod.animation_time = 0
                fishing_rod.animation_frame = 0  
                self.animation_time = 0
                self.animation_frame = 0
                self.fishing_rod = 1
                
        if self.player_move == 1:
            if key[pygame.K_d] or key[pygame.K_RIGHT]:
                self.rect.x += self.speed
                self.move_direction = "right"
                self.direction = "right"
                self.move_status = 1
                self.fishing_rod = 0
            elif key[pygame.K_a] or key[pygame.K_LEFT]:
                self.rect.x -= self.speed
                self.move_direction = "left"
                self.direction = "left"
                self.move_status = 1
                self.fishing_rod = 0
            elif key[pygame.K_w] or key[pygame.K_UP]:
                self.rect.y -= self.speed
                self.move_direction = "up"
                self.direction = "up"
                self.move_status = 1
                self.fishing_rod = 0
            elif key[pygame.K_s] or key[pygame.K_DOWN]:
                self.rect.y += self.speed
                self.move_direction = "down"
                self.direction = "down"
                self.move_status = 1
                self.fishing_rod = 0
            else:
                self.move_direction = "stay"
                self.move_status = 0

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= width - 350:
            self.rect.x = width - 350
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y >= height - 100:
            self.rect.y = height - 100

        if self.move_status == 1:
            self.animation_time += 1
            if self.move_direction == "right":
                if self.animation_time >= 12:
                    self.animation_frame = (self.animation_frame + 1) % len(self.right_imgs)
                    frame_rect = pygame.Rect(self.right_imgs[self.animation_frame])
                    self.endimage = self.images["walk"].subsurface(frame_rect)
                    self.animation_time = 0
            elif self.move_direction == "left":
                if self.animation_time >= 12:
                    self.animation_frame = (self.animation_frame + 1) % len(self.left_imgs)
                    frame_rect = pygame.Rect(self.left_imgs[self.animation_frame])
                    self.endimage = self.images["walk"].subsurface(frame_rect)
                    self.animation_time = 0
            elif self.move_direction == "down":
                if self.animation_time >= 12:
                    self.animation_frame = (self.animation_frame + 1) % len(self.down_imgs)
                    frame_rect = pygame.Rect(self.down_imgs[self.animation_frame])
                    self.endimage = self.images["walk"].subsurface(frame_rect)
                    self.animation_time = 0
            elif self.move_direction == "up":
                if self.animation_time >= 12:
                    self.animation_frame = (self.animation_frame + 1) % len(self.up_imgs)
                    frame_rect = pygame.Rect(self.up_imgs[self.animation_frame])
                    self.endimage = self.images["walk"].subsurface(frame_rect)
                    self.animation_time = 0
        if self.move_status == 0 and self.hoed == 0 and self.irrigation == 0 and self.fishing_rod == 0:
            if self.direction == "right":
                self.endimage = self.images["idle"].subsurface(pygame.Rect(0, 0, 33, 42))
            elif self.direction == "left":
                self.endimage = self.images["idle"].subsurface(pygame.Rect(0, 126, 33, 42))
            elif self.direction == "down":
                self.endimage = self.images["idle"].subsurface(pygame.Rect(0, 42, 39, 42))
            elif self.direction == "up":
                self.endimage = self.images["idle"].subsurface(pygame.Rect(0, 84, 39, 42))

        if self.hoed == 1 and self.move_status == 0:
            self.animation_time += 1
            if self.animation_time >= 12:  
                self.player_move = 0
                if self.animation_frame < len(self.hoed_imgs):  
                        frame_rect = pygame.Rect(self.hoed_imgs[self.animation_frame])
                        self.endimage = self.images["hoed"].subsurface(frame_rect)

                        if self.direction == "left":
                            self.endimage = pygame.transform.flip(self.endimage, True, False)

                        self.endimage = self.endimage
                        self.animation_frame += 1
                        self.hoedanimation_frame += 1
                        self.animation_time = 0

                        if self.hoedanimation_frame == 2:
                          if self.direction == "left":
                            hoedrect.rect.x = player.rect.x - 10  
                            hoedrect.rect.y = player.rect.y + 32
                            hoe.play()
                          if self.direction == "right" or self.direction == "down" or self.direction == "up":
                            hoedrect.rect.x = player.rect.x + 36 
                            hoedrect.rect.y = player.rect.y + 32
                            hoe.play()
                        elif self.hoedanimation_frame == 3:
                          if self.direction == "left":
                            hoedrect.rect.x = player.rect.x - 10
                            hoedrect.rect.y = player.rect.y + 32
                          if self.direction == "right" or self.direction == "down" or self.direction == "up":
                            hoedrect.rect.x = player.rect.x + 36 
                            hoedrect.rect.y = player.rect.y + 32
                            self.hoedanimation_frame = 0
                        else:
                            hoedrect.rect.x = 2000
                            hoedrect.rect.y = 2000
                else:
                        self.player_move = 1
                        self.hoed = 0  
                        self.animation_frame = 0  
                        self.hoedanimation_frame = 0  
                        hoedrect.rect.x = 2000
                        hoedrect.rect.y = 2000

        if self.fishing_rod == 1 and self.move_status == 0 and self.fishing_hit == 1:
            fishing_rod.animation_time += 1
            if fishing_rod.animation_time >= 16:  
                if fishing_rod.animation_frame < len(fishing_rod.fishing_rod_imgs):   
                    frame_rect = pygame.Rect(fishing_rod.fishing_rod_imgs[fishing_rod.animation_frame])
                    fishing_rod.endimage = fishing_rod.images["fishing"].subsurface(frame_rect)
                    fishing_rod.animation_time = 0
                    fishing_rod.animation_frame += 1
                    fishing_rod.fishing_rodanimation_frame += 1
                    if fishing_rod.fishing_rodanimation_frame == 1:
                        fishing_rod.rect.x = self.rect.x 
                        fishing_rod.rect.y = self.rect.y - 33
                    if fishing_rod.fishing_rodanimation_frame == 2:
                        fishing_rod.rect.x = self.rect.x - 21
                        fishing_rod.rect.y = self.rect.y - 18
                    if fishing_rod.fishing_rodanimation_frame == 3:
                        fishing_rod.rect.x = self.rect.x - 30
                        fishing_rod.rect.y = self.rect.y - 24
                    if fishing_rod.fishing_rodanimation_frame == 4:
                        fishing_rod.rect.x = self.rect.x + 33
                        fishing_rod.rect.y = self.rect.y - 30
                    if fishing_rod.fishing_rodanimation_frame == 5:
                        fishing_rod.rect.x = self.rect.x + 33
                        fishing_rod.rect.y = self.rect.y - 16
                    if fishing_rod.fishing_rodanimation_frame == 6:
                        fishing_rod.rect.x = self.rect.x + 33
                        fishing_rod.rect.y = self.rect.y 
                        self.fishing = 1   
                        fishing_rod.fishing_rodanimation_frame = 0
                        water.play()
            self.animation_time += 1
            if self.animation_time >= 16:  
                if self.animation_frame < len(self.fishing_rod_imgs):  
                    frame_rect = pygame.Rect(self.fishing_rod_imgs[self.animation_frame])
                    self.endimage = self.images["fishing"].subsurface(frame_rect)
                    self.animation_frame += 1
                    self.animation_time = 0
                    self.fishing_rodanimation_frame += 1
        else:
            fishing_rod.rect.x = 2000
            fishing_rod.rect.y = self.rect.y 
            self.fishing = 0

        if self.irrigation == 1 and self.move_status == 0:            
            irrigation.animation_time += 1
            if irrigation.animation_time >= 16:  
                if irrigation.animation_frame < len(irrigation.irrigation_imgs) and self.direction == "left":   
                    frame_rect2 = pygame.Rect(irrigation.irrigation_imgs[irrigation.animation_frame])
                    irrigation.endimage = irrigation.images["irrigation"].subsurface(frame_rect2)
                    irrigation.animation_frame += 1
                    irrigation.irrigationanimation_frame += 1
                    irrigation.animation_time = 0
                    if irrigation.irrigationanimation_frame == 1:
                        irrigation.rect.x = self.rect.x - 9
                        irrigation.rect.y = self.rect.y + 21
                    if irrigation.irrigationanimation_frame == 2:
                        irrigation.rect.x = self.rect.x - 36
                        irrigation.rect.y = self.rect.y + 21
                        irrigation.irrigationanimation_frame = 0

            self.animation_time += 1
            if self.animation_time >= 16:  
                self.player_move = 0
                if self.direction == "right" or self.direction == "down" or self.direction == "up":
                  if self.animation_frame < len(self.irrigation_imgs):  
                    frame_rect = pygame.Rect(self.irrigation_imgs[self.animation_frame])
                    self.endimage = self.images["hoed"].subsurface(frame_rect)
                    self.animation_frame += 1
                    self.irrigationanimation_frame += 1
                    self.animation_time = 0
                    if self.irrigationanimation_frame == 2:
                        irrigationrect.rect.x = player.rect.x + 48
                        irrigationrect.rect.y = player.rect.y + 32
                        self.irrigationanimation_frame = 0
                        water.play()
                  else:
                    self.player_move = 1
                    self.irrigation = 0  
                    self.animation_frame = 0
                    self.irrigationanimation_frame = 0
                    irrigationrect.rect.x = 2000  

                elif self.direction == "left":
                  if self.animation_frame < len(self.irrigation_imgs2):  
                    frame_rect = pygame.Rect(self.irrigation_imgs2[self.animation_frame])
                    self.endimage = self.images["irrigation"].subsurface(frame_rect)
                    self.animation_frame += 1
                    self.irrigationanimation_frame += 1
                    self.animation_time = 0            
                    if self.irrigationanimation_frame == 2:
                        irrigationrect.rect.x = player.rect.x - 30
                        irrigationrect.rect.y = player.rect.y + 32
                        self.irrigationanimation_frame = 0
                        water.play()
                  else:
                    self.player_move = 1
                    self.irrigation = 0  
                    self.animation_frame = 0
                    self.irrigationanimation_frame = 0
                    irrigationrect.rect.x = 2000  
        else:

            irrigation.rect.x = 2000
            irrigation.rect.y = self.rect.y 
        
        if self.fishing == 1 and self.fishing_rod == 1:
            if self.player_number == self.fish_number:
                self.player_move = 0
                self.fishing_mini_game()
                self.mini_game = 1
            else:
                self.fish_type = random.choice(['Perch','Angler','Perch','Perch','Perch','Perch','Tuna','Perch','Tuna','Tuna'])
                self.fish_number = random.randint(1,100)
                self.player_number = random.randint(1,100)
  
    def wall_hit(self):        
        self.player_wall_hit = 0
        for wallx in total_walls:
          for wall in wallx:
            if self.rect.colliderect(wall.rect):
                if self.move_direction == "right":
                    self.rect.right = wall.rect.left
                    self.player_wall_hit = 1
                elif self.move_direction == "left":
                    self.rect.left = wall.rect.right
                    self.player_wall_hit = 1
                if self.move_direction == "up":
                    self.rect.top = wall.rect.bottom
                    self.player_wall_hit = 1
                elif self.move_direction == "down":
                    self.rect.bottom = wall.rect.top
                    self.player_wall_hit = 1
                    
        for fishingwall in fishingwalls:
            if self.rect.colliderect(fishingwall.rect):
                self.fishing_hit = 1
            else:
                self.fishing_hit = 0

        if self.rect.colliderect(bed.rect):
            self.bed = 1
        else:
            self.bed = 0

    def soil_hit(self):        
        for soil in soils:
            if hoedrect.rect.colliderect(soil.rect):
                if self.hoed == 1 and soil.wet == 0:
                    soil.endimage = soil.images["img"].subsurface(pygame.Rect(32, 0, 32, 32)) 
                    soil.hoed = 1
            if irrigationrect.rect.colliderect(soil.rect):
                if soil.hoed == 1 and soil.carrot == 0 and soil.onion == 0 and soil.potato == 0: 
                    soil.wet = 1
                    soil.endimage = soil.images["img"].subsurface(pygame.Rect(64, 0, 32, 32)) 
            if self.rect.colliderect(soil.rect):
                if self.tuşp == 1 and soil.wet == 1 and soil.hoed == 1 and soil.carrot == 0 and soil.onion == 0 and soil.potato == 0 and self.number_potato > 0: 
                 if not hasattr(self, 'last_plant_time') or pygame.time.get_ticks() - self.last_plant_time > 20: 
                    plant.play()
                    soil.potato = 1       
                    soil.carrot = 0       
                    soil.onion = 0   
                    soil.endimage = soil.images["img"].subsurface(pygame.Rect(256, 0, 32, 32)) 
                    self.number_potato -= 1 
                    self.last_plant_time = pygame.time.get_ticks() 
                if self.tuşc == 1 and soil.wet == 1 and soil.hoed == 1 and soil.carrot == 0 and soil.onion == 0 and soil.potato == 0 and self.number_carrot > 0: 
                 if not hasattr(self, 'last_plant_time') or pygame.time.get_ticks() - self.last_plant_time > 20:
                    plant.play() 
                    soil.carrot = 1     
                    soil.potato = 0       
                    soil.onion = 0         
                    soil.endimage = soil.images["img"].subsurface(pygame.Rect(96, 0, 32, 32)) 
                    self.number_carrot -= 1 
                if self.tuşo == 1 and soil.wet == 1 and soil.hoed == 1 and soil.onion == 0 and soil.carrot == 0 and soil.potato == 0 and self.number_onion > 0: 
                 if not hasattr(self, 'last_plant_time') or pygame.time.get_ticks() - self.last_plant_time > 20:
                    plant.play() 
                    soil.onion = 1        
                    soil.carrot = 0       
                    soil.potato = 0      
                    soil.endimage = soil.images["img"].subsurface(pygame.Rect(416, 0, 32, 32)) 
                    self.number_onion -= 1 

            if soil.wet == 1 and soil.hoed == 1:
                    if soil.potato == 1:
                        soil.animation_time += 1  
                        if soil.animation_time >= 500:
                            if soil.animation_frame < len(soil.potato_imgs):  
                                frame_rect = pygame.Rect(soil.potato_imgs[soil.animation_frame])
                                soil.endimage = soil.images["img"].subsurface(frame_rect)
                                soil.animation_frame += 1
                                soil.animation_time = 0 

                    if soil.carrot == 1:
                        soil.animation_time += 1  
                        if soil.animation_time >= 500:
                            if soil.animation_frame < len(soil.carrot_imgs):  
                                frame_rect = pygame.Rect(soil.carrot_imgs[soil.animation_frame])
                                soil.endimage = soil.images["img"].subsurface(frame_rect)
                                soil.animation_frame += 1
                                soil.animation_time = 0 

                    if soil.onion == 1:
                        soil.animation_time += 1  
                        if soil.animation_time >= 500:
                            if soil.animation_frame < len(soil.onion_imgs):  
                                frame_rect = pygame.Rect(soil.onion_imgs[soil.animation_frame])
                                soil.endimage = soil.images["img"].subsurface(frame_rect)
                                soil.animation_frame += 1
                                soil.animation_time = 0 
                    
                    if self.rect.colliderect(soil.rect):
                      if soil.animation_frame == 5:
                        if self.tuşe == 1:
                            if soil.potato == 1:
                                self.xp += 20
                                self.potato = 1
                                self.number_potato += random.choice([1,2,2,1,1,1,1,1,3,1,1,2,1,1])
                                soil.potato = 0
                                soil.wet = 0
                                soil.hoed = 0
                                soil.animation_time = 0
                                soil.animation_frame = 0
                                soil.endimage = soil.images["img"].subsurface(pygame.Rect(0, 0, 32, 32)) 
                            if soil.carrot == 1:
                                self.xp += 30
                                self.carrot = 1
                                self.number_carrot += random.choice([1,1,2,2,1,1,1,1,1,1])
                                soil.carrot = 0
                                soil.wet = 0
                                soil.hoed = 0
                                soil.animation_time = 0
                                soil.animation_frame = 0
                                soil.endimage = soil.images["img"].subsurface(pygame.Rect(0, 0, 32, 32)) 
                            if soil.onion == 1:
                                self.xp += 40
                                self.onion = 1
                                self.number_onion += random.choice([1,2,2,1,1,1,1,1,1,1,1,1])
                                soil.onion = 0
                                soil.wet = 0
                                soil.hoed = 0
                                soil.animation_time = 0
                                soil.animation_frame = 0
                                soil.endimage = soil.images["img"].subsurface(pygame.Rect(0, 0, 32, 32)) 

    def signboard_hit(self):       
        if self.rect.colliderect(signboard.rect):
            textbox = pygame.image.load('img/textbox.png')
            ekran.blit(textbox,(294,194))
            text = pygame.font.Font(None, 30).render("To repair the ship you ", True, (255,255,255))
            ekran.blit(text,(321,202))
            text = pygame.font.Font(None, 30).render("need 5000g", True, (255,255,255))
            ekran.blit(text,(370,236))
            text = pygame.font.Font(None, 26).render("Pay", True, (255,255,255))
            ekran.blit(text,(411,277))

    def farmer_hit(self):       
        if self.rect.colliderect(farmer.rect):
            textbox = pygame.image.load('img/box.png')
            ekran.blit(textbox,(36,188))
            text = pygame.font.Font(None, 27).render(f"Patato {self.number_potato}x     Sell", True, (234,234,234))
            ekran.blit(text,(43,195))
            text = pygame.font.Font(None, 27).render(f"Carrot {self.number_carrot}x     Sell", True, (234,234,234))
            ekran.blit(text,(43,226))
            text = pygame.font.Font(None, 27).render(f"Onion {self.number_onion}x      Sell", True, (234,234,234))
            ekran.blit(text,(43,257))
            text = pygame.font.Font(None, 27).render(f"Perch {self.number_perch}x      Sell", True, (234,234,234))
            ekran.blit(text,(43,291))
            text = pygame.font.Font(None, 27).render(f"Tuna {self.number_tuna}x        Sell", True, (234,234,234))
            ekran.blit(text,(43,325))
            text = pygame.font.Font(None, 27).render(f"Angler {self.number_angler}x    Sell", True, (234,234,234))
            ekran.blit(text,(43,358))

    def fishing_mini_game(self):
        global box_x
        if self.mini_game == 1 and self.fishing == 1:
            if self.player_point != 5 and self.player_point < 5:
                self.fish_time = 0
                ekran.blit(fishing_box,(270,230))
                if fish.rect.x >= 505:
                    fish.direction = "left"
                    fish.image = pygame.transform.flip(fish.image, True, False)
                if fish.rect.x <= 290:
                    fish.direction = "right"
                    fish.image = pygame.transform.flip(fish.image, True, False)
                    
                if fish.direction == "left":
                  fish.rect.x-= random.choice([5,6,7,8,5,6,6,6,7,8,9])
                if fish.direction == "right":
                  fish.rect.x+= random.choice([5,6,7,8,5,6,6,6,7,8,9])

                text = pygame.font.Font(None, 30).render(f"Catch 5/{self.player_point}", True, (255,255,255))
                ekran.blit(text,(380,292))

            if self.player_point == 5:
                    self.game_click = 0
                    self.fish_time += 1
                    if self.fish_type == 'Perch':
                        ekran.blit(fishicon,(400,120)) 
                        text = pygame.font.Font(None, 30).render(f"+1 Perch", True, (0,0,0))
                        ekran.blit(text,(405,172))
                        self.perch = 1
                    if self.fish_type == 'Angler':
                        ekran.blit(anglerfishicon,(420,120)) 
                        text = pygame.font.Font(None, 30).render(f"+1 Angler", True, (0,0,0))
                        ekran.blit(text,(405,172))
                        self.angler = 1
                    if self.fish_type == 'Tuna':
                        ekran.blit(tunafishicon,(380,120)) 
                        text = pygame.font.Font(None, 30).render(f"+1 Tuna", True, (0,0,0))
                        ekran.blit(text,(400,172))
                        self.tuna = 1
                    if self.fish_time >= 120:
                        self.game_click = 1
                        if self.fish_type == 'Perch':
                            self.number_perch += 1
                            self.xp += 25
                        if self.fish_type == 'Angler':
                            self.number_angler += 1
                            self.xp += 65
                        if self.fish_type == 'Tuna':
                            self.number_tuna += 1 
                            self.xp += 35
                        self.fish_type = random.choice(['Angler','Perch','Angler','Perch''Tuna','Perch','Tuna','Tuna','Perch','Perch','Perch','Tuna','Tuna','Perch','Perch'])
                        self.mini_game = 0
                        box_x = random.randint(295,480)
                        box.rect.x = box_x
                        self.fishing = 0
                        self.fishing_rod = 0
                        self.player_point = 0  
                        self.player_move = 1

    def draw(self):
        ekran.blit(self.endimage,self.rect)

    def level_draw(self):
        textbox = pygame.image.load('img/level_bar.png')
        ekran.blit(textbox,(78,22))
        text = pygame.font.Font(None, 34).render(f"{self.level}", True, (0,0,0))
        ekran.blit(text,(93,33))
        level_bar_rect = pygame.Rect(123, 33, self.level_bar_width, self.level_bar_height)
        pygame.draw.rect(ekran, (34, 122, 37), level_bar_rect)
        level_percentage = max(0, self.xp) / self.max_xp
        self.level_bar_width = int(level_percentage * 95)
        if self.xp >= 95:
            self.level += 1
            self.xp = 0

    def inventory_system(self):
        # prech
        if self.perch == 1:
            if self.item_1 == "":
                self.item_1 = "Perch"
            elif self.item_1 == "Perch":
                self.number__of_item_1 = self.number_perch
            elif self.item_2 == "" and self.item_1 != "Perch":
                self.item_2 = "Perch"
            elif self.item_2 == "Perch":
                self.number__of_item_2 = self.number_perch
            elif self.item_3 == "" and self.item_2 != "Perch" and self.item_1 != "Perch":
                self.item_3 = "Perch"
            elif self.item_3 == "Perch":
                self.number__of_item_3 = self.number_perch
            elif self.item_4 == "" and self.item_3 != "Perch" and self.item_2 != "Perch" and self.item_1 != "Perch":
                self.item_4 = "Perch"
            elif self.item_4 == "Perch":
                self.number__of_item_4 = self.number_perch
            elif self.item_5 == "" and self.item_4 != "Perch" and self.item_3 != "Perch" and self.item_2 != "Perch" and self.item_1 != "Perch":
                self.item_5 = "Perch"
            elif self.item_5 == "Perch":
                self.number__of_item_5 = self.number_perch
        # tuna
        if self.tuna == 1:
            if self.item_1 == "":
                self.item_1 = "Tuna"
            elif self.item_1 == "Tuna":
                self.number__of_item_1 = self.number_tuna
            elif self.item_2 == "" and self.item_1 != "Tuna":
                self.item_2 = "Tuna"
            elif self.item_2 == "Tuna":
                self.number__of_item_2 = self.number_tuna
            elif self.item_3 == "" and self.item_2 != "Tuna" and self.item_1 != "Tuna":
                self.item_3 = "Tuna"
            elif self.item_3 == "Tuna":
                self.number__of_item_3 = self.number_tuna
            elif self.item_4 == "" and self.item_3 != "Tuna" and self.item_2 != "Tuna" and self.item_1 != "Tuna":
                self.item_4 = "Tuna"
            elif self.item_4 == "Tuna":
                self.number__of_item_4 = self.number_tuna
            elif self.item_5 == "" and self.item_4 != "Tuna" and self.item_3 != "Tuna" and self.item_2 != "Tuna" and self.item_1 != "Tuna":
                self.item_5 = "Tuna"
            elif self.item_5 == "Tuna":
                self.number__of_item_5 = self.number_tuna
        # angler
        if self.angler == 1:
            if self.item_1 == "":
                self.item_1 = "Angler"
            elif self.item_1 == "Angler":
                self.number__of_item_1 = self.number_angler
            elif self.item_2 == "" and self.item_1 != "Angler":
                self.item_2 = "Angler"
            elif self.item_2 == "Angler":
                self.number__of_item_2 = self.number_angler
            elif self.item_3 == "" and self.item_2 != "Angler" and self.item_1 != "Angler":
                self.item_3 = "Angler"
            elif self.item_3 == "Angler":
                self.number__of_item_3 = self.number_angler
            elif self.item_4 == "" and self.item_3 != "Angler" and self.item_2 != "Angler" and self.item_1 != "Angler":
                self.item_4 = "Angler"
            elif self.item_4 == "Angler":
                self.number__of_item_4 = self.number_angler
            elif self.item_5 == "" and self.item_4 != "Angler" and self.item_3 != "Angler" and self.item_2 != "Angler" and self.item_1 != "Angler":
                self.item_5 = "Angler"
            elif self.item_5 == "Angler":
                self.number__of_item_5 = self.number_angler
        # carrot
        if self.carrot == 1:
            if self.item_1 == "":
                self.item_1 = "Carrot"
            elif self.item_1 == "Carrot":
                self.number__of_item_1 = self.number_carrot
            elif self.item_2 == "" and self.item_1 != "Carrot":
                self.item_2 = "Carrot"
            elif self.item_2 == "Carrot":
                self.number__of_item_2 = self.number_carrot
            elif self.item_3 == "" and self.item_2 != "Carrot" and self.item_1 != "Carrot":
                self.item_3 = "Carrot"
            elif self.item_3 == "Carrot":
                self.number__of_item_3 = self.number_carrot
            elif self.item_4 == "" and self.item_3 != "Carrot" and self.item_2 != "Carrot" and self.item_1 != "Carrot":
                self.item_4 = "Carrot"
            elif self.item_4 == "Carrot":
                self.number__of_item_4 = self.number_carrot
            elif self.item_5 == "" and self.item_4 != "Carrot" and self.item_3 != "Carrot" and self.item_2 != "Carrot" and self.item_1 != "Carrot":
                self.item_5 = "Carrot"
            elif self.item_5 == "Carrot":
                self.number__of_item_5 = self.number_carrot
        # onion
        if self.onion == 1:
            if self.item_1 == "":
                self.item_1 = "Onion"
            elif self.item_1 == "Onion":
                self.number__of_item_1 = self.number_onion
            elif self.item_2 == "" and self.item_1 != "Onion":
                self.item_2 = "Onion"
            elif self.item_2 == "Onion":
                self.number__of_item_2 = self.number_onion
            elif self.item_3 == "" and self.item_2 != "Onion" and self.item_1 != "Onion":
                self.item_3 = "Onion"
            elif self.item_3 == "Onion":
                self.number__of_item_3 = self.number_onion
            elif self.item_4 == "" and self.item_3 != "Onion" and self.item_2 != "Onion" and self.item_1 != "Onion":
                self.item_4 = "Onion"
            elif self.item_4 == "Onion":
                self.number__of_item4 = self.number_onion
            elif self.item_5 == "" and self.item_4 != "Onion" and self.item_3 != "Onion" and self.item_2 != "Onion" and self.item_1 != "Onion":
                self.item_5 = "Onion"
            elif self.item_5 == "Onion":
                self.number__of_item_5 = self.number_onion

    def update(self):
        self.draw()
        self.move()
        self.soil_hit()
        self.wall_hit()
        self.signboard_hit()

class Attack():
    def __init__(self,x,y,en,boy):  
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)

    def draw(self):
        pygame.draw.rect(ekran,(0,220,0),self.rect)

class Fishing_Rod():
    def __init__(self,x,y,en,boy):  
        self.images = {
            'fishing': pygame.image.load('img/playerfishing.png'),
        }
        self.endimage = self.images["fishing"].subsurface(pygame.Rect(0, 0, 39, 42)) 
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.animation_time = 0
        self.animation_frame = 0
        self.fishing_rodanimation_frame = 0
        self.fishing_rod_imgs = [(0, 0, 32, 33),(33, 0, 21, 54),(87, 0, 69, 36),(189, 0, 60, 69),(282, 0, 66, 66),(381, 0, 54, 60)]

    def draw(self):
        ekran.blit(self.endimage,self.rect)

class İrrigation():
    def __init__(self,x,y,en,boy):  
        self.images = {
            'irrigation': pygame.image.load('img/playerirrigationleft.png'),
        }
        self.endimage = self.images["irrigation"].subsurface(pygame.Rect(0, 21, 9, 18)) 
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.animation_time = 0
        self.animation_frame = 0
        self.irrigationanimation_frame = 0
        self.irrigation_imgs = [(0, 21, 9, 18),(42, 21, 36, 18)]

    def draw(self):
        ekran.blit(self.endimage,self.rect)

class Fish():
    def __init__(self,x,y,en,boy):  
        self.image = pygame.image.load('img/fish.png')
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.direction = "right"
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
    def draw(self):
        ekran.blit(self.image,self.rect)

class Bagpack():
    def __init__(self,x,y,en,boy):  
        self.image = pygame.image.load('img/bagpack.png')
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.direction = "right"
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
    def draw(self):
        ekran.blit(self.image,self.rect)

class Farmer():
    def __init__(self,x,y,en,boy):
        self.image = pygame.image.load('img/npc.png').subsurface(pygame.Rect(0, 0, 90, 48)) 
        self.x, self.y, self.en, self.boy = x, y, en, boy
        self.rect = pygame.Rect(self.x, self.y, self.en, self.boy)
        self.direction = "right"
        self.time, self.time2, self.stay = 0, 0, 0
        self.wall_hit = 0
        self.wall_time = 0
    def draw(self):
        if self.direction == "left":
            self.image = pygame.image.load('img/npc.png').subsurface(pygame.Rect(90, 0, 90, 48))
        if self.direction == "right":
            self.image = pygame.image.load('img/npc.png').subsurface(pygame.Rect(0, 0, 90, 48))
        ekran.blit(self.image,self.rect)
    def move(self):
        global hour,minute
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                self.wall_hit = 1
            else:
                self.wall_hit = 0
        if hour == 9:
          self.wall_time += 1
          if self.wall_time <= 294:
            if self.wall_hit == 0:
                self.rect.x -= 2
                self.direction = 'left'
        if hour == 11:
            self.rect.x += 2
            self.direction = 'right'
            self.wall_time = 0
    def update(self):
        if self.rect.x <= 1300:
            self.draw()
        self.move()

width, height = 800, 576

pygame.init()
pygame.mixer.init()

ekran = pygame.display.set_mode((width, height))
pygame.display.set_caption("Farm Game")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

player = Player(x=350,y=250,en=39,boy=42,speed=3)
map = Map(0,0)
hoedrect = Attack(1000,2000,16,8)
irrigationrect = Attack(1000,2000,16,8)
fishing_rod = Fishing_Rod(1000,2000,39,42)
irrigation = İrrigation(1000,2000,9,18)
fishing_box = pygame.image.load('img/fishingbox.png')
fish = Fish(289,250,70,40)
box_x = random.randint(295,480)
box = Wall(box_x,242,35,36)
signboard = Wall(770,350,26,16)
fishicon = pygame.image.load('img/fishicon.png')
anglerfishicon = pygame.image.load('img/Anglerfishicon.png')
tunafishicon = pygame.image.load('img/tunafishicon.png')
bagpack = Bagpack(10,10,58,62)
farmer = Farmer(1400,480,90,42)
sell_buton1 = Wall(151,195,35,16)
sell_buton2 = Wall(151,226,35,16)
sell_buton3 = Wall(151,257,35,16)
sell_buton4 = Wall(151,291,35,16)
sell_buton5 = Wall(151,325,35,16)
sell_buton6 = Wall(151,358,35,16)
bed = Wall(96,72,40,46)
hour = 6
minute = 0
second = 0
time_farmer = 0
fade_surface = pygame.Surface((width, height))
fade_surface.fill((0, 0, 0)) 
alpha = 0
pygame.mixer.music.load("müzik.mp3") 
pygame.mixer.music.play(-1)
hoe = pygame.mixer.Sound("hoe.wav")
plant = pygame.mixer.Sound("plant.wav")
water = pygame.mixer.Sound("water.mp3")
game_menu = 1 
total_walls = []
butonplay = Wall(357,241,82,40)
butonkeys = Wall(353,313,92,40)
butonexit = Wall(357,384,82,40)
butonback = Wall(681,520,82,40)
butonpay = Wall(404,272,48,27)
bg = pygame.image.load('img/bg.png')
text_y = 600
end = 0

sprities = []
sprities_list = []

def create_walls(wall_map):
    walls = []
    cell_size = 32
    for y, row in enumerate(wall_map):
        for x, value in enumerate(row):
            if value == 1: 
                wall = Wall(x * cell_size, y * cell_size+16, cell_size, cell_size)
                walls.append(wall)
            if value == 2: 
                wall = Wall(x * cell_size+17, y * cell_size, cell_size, cell_size)
                walls.append(wall)
            if value == 3: 
                wall = Wall(x * cell_size, y * cell_size, cell_size, cell_size)
                walls.append(wall)
            if value == 4: 
                wall = Wall(x * cell_size, y * cell_size, cell_size-16, cell_size)
                walls.append(wall)
            if value == 5: 
                wall = Wall(x * cell_size+16, y * cell_size, cell_size-16, cell_size)
                walls.append(wall)
            if value == 6: 
                wall = Wall(x * cell_size-4, y * cell_size-12, cell_size+8, cell_size-10)
                walls.append(wall)
            if value == 7: 
                wall = Wall(x * cell_size+16, y * cell_size-12, cell_size-16, cell_size-10)
                walls.append(wall)
            if value == 8: 
                wall = Wall(x * cell_size, y * cell_size-12, cell_size-16, cell_size-10)
                walls.append(wall)
            if value == 11: 
                wall = Wall(x * cell_size+8, y * cell_size-8, cell_size-16, cell_size)
                walls.append(wall)
            if value == 12: 
                wall = Wall(x * cell_size+10, y * cell_size-4, cell_size, cell_size-16)
                walls.append(wall)
            if value == 13: 
                wall = Wall(x * cell_size+4, y * cell_size-4, cell_size-16, cell_size-16)
                walls.append(wall)
            if value == 15: 
                wall = Wall(x * cell_size+17, y * cell_size-12, cell_size, cell_size-16)
                walls.append(wall)
            if value == 16: 
                wall = Wall(x * cell_size+1, y * cell_size-12, cell_size+8, cell_size-10)
                walls.append(wall)
    return walls

def create_fishingwalls(wall_map):
    fishingwalls = []
    cell_size = 32
    for y, row in enumerate(wall_map):
        for x, value in enumerate(row):
            if value == 14: 
                fishingwall = Wall(x * cell_size, y * cell_size-14, cell_size, cell_size)
                fishingwalls.append(fishingwall)
    return fishingwalls

def create_soils(wall_map):
    soils = []
    cell_size = 32
    for y, row in enumerate(wall_map):
        for x, value in enumerate(row):
            if value == 9: 
                soil = Soil(x * cell_size, y * cell_size, cell_size, cell_size)
                soils.append(soil)
    return soils

walls = create_walls(wall_map)
total_walls.append(walls)
fishingwalls = create_fishingwalls(wall_map)
sprities_list.append(walls)
sprities_list.append(fishingwalls)
soils = create_soils(wall_map)
sprities_list.append(soils)
sprities.append(map)
sprities.append(farmer)
sprities.append(signboard)

def camera():
    if player.player_wall_hit == 0:
        if player.move_direction == "right" and player.rect.x > 300:
            for spritie in sprities_list:
              for spritiex in spritie:
                spritiex.rect.x -= player.speed
            for spritie in sprities:
                spritie.rect.x -= player.speed
        if player.move_direction == "left" and map.rect.x != 0:
            for spritie in sprities_list:
              for spritiex in spritie:
                spritiex.rect.x += player.speed
            for spritie in sprities:
                spritie.rect.x += player.speed
        if player.move_direction == "down" and player.rect.y > 300:
            for spritie in sprities_list:
              for spritiex in spritie:
                spritiex.rect.y -= player.speed
            for spritie in sprities:
                spritie.rect.y -= player.speed
        if player.move_direction == "up" and map.rect.y != 0:
            for spritie in sprities_list:
              for spritiex in spritie:
                spritiex.rect.y += player.speed
            for spritie in sprities:
                spritie.rect.y += player.speed

def time():
    global second,minute,hour,time_farmer
    second += 0.5
    if second >= 60:
        minute += 10
        time_farmer += 2
        second = 0
    if minute >= 60:
        hour += 1 
        minute = 0
        time_farmer = 0
    if hour == 24:
        hour = 0

    if hour <= 9 and minute == 0:
        text = pygame.font.Font(None, 30).render(f"Hour 0{hour}:0{minute}", True, (255,255,255))
        ekran.blit(text,(690,10))
    if hour > 9 and minute == 0:
        text = pygame.font.Font(None, 30).render(f"Hour {hour}:0{minute}", True, (255,255,255))
        ekran.blit(text,(690,10))
    if hour <= 9 and minute != 0:
        text = pygame.font.Font(None, 30).render(f"Hour 0{hour}:{minute}", True, (255,255,255))
        ekran.blit(text,(690,10))
    if hour > 9 and minute != 0:
        text = pygame.font.Font(None, 30).render(f"Hour {hour}:{minute}", True, (255,255,255))
        ekran.blit(text,(690,10))
    
    if player.bed == 1:
       if hour >= 20 or hour < 6:
         player.rect.x = bed.rect.x + 4
         player.rect.y = bed.rect.y + 2
         player.move_status = 0
         second += 7.4
       else:
           player.move_status = 1

def inventory():
   envanter_box = pygame.image.load('img/envanter_box.png')
   fontx = pygame.font.Font(None,28)
   text_1 = fontx.render("[1] Hoe", True, (0,0,0))
   text_2 = fontx.render("[2] Watering Can", True, (0,0,0))
   text_3 = fontx.render("[3] Fishin rod", True, (0,0,0))
   text_4 = fontx.render("[4] Axe", True, (0,0,0))
   text_5 = fontx.render(f"[5] Potato {player.number_potato}x", True, (0,0,0))
   text_6 = fontx.render(f"[6] {player.item_1} {player.number__of_item_1}x", True, (0,0,0))
   text_7 = fontx.render(f"[7] {player.item_2} {player.number__of_item_2}x", True, (0,0,0))
   text_8 = fontx.render(f"[8] {player.item_3} {player.number__of_item_3}x", True, (0,0,0))
   text_9 = fontx.render(f"[9] {player.item_4} {player.number__of_item_4}x", True, (0,0,0))
   text_10 = fontx.render(f"[10] {player.item_5} {player.number__of_item_5}x", True, (0,0,0))
   text_11 = fontx.render(f"[11] {player.item_6} {player.number__of_item_6}x", True, (0,0,0))
   ekran.blit(envanter_box,(8,8))
   ekran.blit(text_1,(23,22))
   ekran.blit(text_2,(23,53))
   ekran.blit(text_3,(23,84))
   ekran.blit(text_4,(23,115))
   ekran.blit(text_5,(23,146))
   if player.item_1 != "":
     ekran.blit(text_6,(23,177))
   if player.item_2 != "":
     ekran.blit(text_7,(23,208))
   if player.item_3 != "":
     ekran.blit(text_8,(23,239))
   if player.item_4 != "":
     ekran.blit(text_9,(23,270))
   if player.item_5 != "":
     ekran.blit(text_10,(23,301))
   if player.item_6 != "":
     ekran.blit(text_11,(23,332))

def menu():
   fontx = pygame.font.Font('Jersey15-Regular.ttf',54)
   ekran.blit(bg,(-20,0))
   text = pygame.font.Font('Jersey15-Regular.ttf',120).render("Farm Game", True, (0,0,0))
   text_1 = fontx.render("Play", True, (0,0,0))
   text_2 = fontx.render("Keys", True, (0,0,0))
   text_3 = fontx.render("Exit", True, (0,0,0))
   ekran.blit(text,(170,60))
   ekran.blit(text_1,(358,232))
   ekran.blit(text_2,(353,303))
   ekran.blit(text_3,(360,374))

def keys_menu():
   fontx = pygame.font.Font('Jersey15-Regular.ttf',44)
   ekran.blit(bg,(-20,0))
   text_1 = fontx.render("p : planting potatoes", True, (0,0,0))
   text_2 = fontx.render("c : planting carrots", True, (0,0,0))
   text_3 = fontx.render("o : planting onions", True, (0,0,0))
   text_4 = fontx.render("1 : hoed", True, (0,0,0))
   text_5 = fontx.render("2 : irrigation", True, (0,0,0))
   text_6 = fontx.render("3 : fishing_rod", True, (0,0,0))
   text_7 = fontx.render("space : using tools", True, (0,0,0))
   text_8 = fontx.render("wasd : direction", True, (0,0,0))
   text_9 = fontx.render("Back", True, (0,0,0))
   ekran.blit(text_1,(253,120))
   ekran.blit(text_2,(253,160))
   ekran.blit(text_3,(253,200))
   ekran.blit(text_4,(253,240))
   ekran.blit(text_5,(253,280))
   ekran.blit(text_6,(253,320))
   ekran.blit(text_7,(253,360))
   ekran.blit(text_8,(253,400))
   ekran.blit(text_9,(683,515))

def end_menu():
    global text_y, game_menu
    fontx = pygame.font.Font('Jersey15-Regular.ttf',44)
    text_1 = fontx.render("Thank you for playing the game", True, (0,0,0))
    ekran.blit(text_1, (143, text_y))
    if text_y >= 120:
     text_y -= 1
     game_menu = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                      
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if player.game_click == 1:
            if player.mini_game == 1 and player.fishing == 1:
                if fish.rect.colliderect(box.rect):
                    player.player_point += 1
                else:
                    player.fish_type = random.choice(['Angler','Perch','Angler','Perch''Tuna','Perch','Tuna','Tuna','Perch','Perch','Perch','Tuna','Tuna','Perch','Perch'])
                    player.mini_game = 0
                    player.fishing_rod = 0
                    player.player_point = 0   
                    player.player_move = 1
                    player.fish_number = 0
                    player.player_number = 1
                    box_x = random.randint(295,480)

            if event.button == 1:
              if game_menu == 1:
                if butonpay.rect.collidepoint(event.pos) and player.rect.colliderect(signboard.rect) and player.money >= 5000:
                    end = 1
                if butonplay.rect.collidepoint(event.pos):
                    game_menu = 0
                if butonkeys.rect.collidepoint(event.pos):
                    game_menu = 2
                if butonexit.rect.collidepoint(event.pos):
                    running = False     
              if game_menu == 2:
                if butonback.rect.collidepoint(event.pos):
                    game_menu = 1             
              if bagpack.rect.collidepoint(event.pos):
                player.bagpack = 1
              else: 
                player.bagpack = 0
              if sell_buton1.rect.collidepoint(event.pos) and player.number_potato > 0:
                  player.number_potato -= 1
                  player.money += 20
              if sell_buton2.rect.collidepoint(event.pos) and player.number_carrot > 0:
                  player.number_carrot -= 1
                  player.money += 35
              if sell_buton3.rect.collidepoint(event.pos) and player.number_onion > 0:
                  player.number_onion -= 1
                  player.money += 25
              if sell_buton4.rect.collidepoint(event.pos) and player.number_perch > 0:
                  player.number_perch -= 1
                  player.money += 30
              if sell_buton5.rect.collidepoint(event.pos) and player.number_tuna > 0:
                  player.number_tuna -= 1
                  player.money += 40
              if sell_buton6.rect.collidepoint(event.pos) and player.number_angler > 0:
                  player.number_angler -= 1
                  player.money += 60

    ekran.fill((78,149,169))
    if game_menu == 2:
      keys_menu()
    if end == 1:
      end_menu()
    if game_menu == 1:
      menu()
    if game_menu == 0:
        map.draw()
        text = pygame.font.Font(None, 30).render(f"Money {player.money}G", True, (255,255,255))
        ekran.blit(text,(680,550))
        text = pygame.font.Font(None, 30).render(f"Fps {clock}G", True, (255,255,255))
        ekran.blit(text,(20,550))
        for soil in soils:
            soil.draw()
        fishing_rod.draw()
        irrigation.draw()
        player.update()
        player.farmer_hit()
        if player.fishing == 1 and player.fishing_rod == 1 and player.mini_game == 1 and player.player_point != 5 and player.player_number == player.fish_number and player.player_point < 5:
            box.draw()
            fish.draw()
        farmer.update()
        time()
        camera()
        bagpack.draw()
        current_time = pygame.time.get_ticks()
        player.level_draw()
        if player.bagpack == 1:
          inventory()        
        if alpha < 255:
            if hour >= 7:
                alpha += 0.0014
            if hour >= 15:
                alpha += 0.007
            if hour == 6:     
                alpha = 0
        ekran.blit(fade_surface, (0, 0))
        fade_surface.set_alpha(alpha) 
        player.inventory_system()
    pygame.display.flip()
    clock.tick()

pygame.quit()
sys.exit()