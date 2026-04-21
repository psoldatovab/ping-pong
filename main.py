import pygame
from random import randint

class Sprite():
    def __init__(self, center, image):
        self.image = image
        self.rect = image.get_frect(center=center)

    def render(self):
        surface.blit(self.image, self.rect)

class Player(Sprite):
    def __init__(self, center, image, btn_up, btn_down, speed):
        super().__init__(center, image)
        self.btn_up = btn_up
        self.btn_down = btn_down
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.btn_up]:
            self.rect.y -= self.speed
        if keys[self.btn_down]:
            self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
        
class Ball(Sprite):
    def __init__(self, center, image, speed):
        super().__init__(center, image)
        self.speed = speed
        self.direction = pygame.Vector2(1, 0)
    def update(self):
        self.rect.move_ip(self.direction * self.speed)
        
        if self.rect.top < 0:
            self.rect.top = 0
            self.direction.y = -self.direction.y

        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.direction.y = -self.direction.y

def restart():
    ball.rect.center = [400, 300]
    ball.speed = 7
    ball. direction.update(1,0)
    left_player.rect.center = [780, 300]
    right_player.rect.center = [20, 300]

pygame.init()

window = pygame.Window('PingPong', [800,600])
surface = window.get_surface()
clock = pygame.Clock()
font = pygame.sysfont.SysFont('Arial', 32)

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

ball_image = pygame.image.load('ball.png').convert_alpha()
ball_image = pygame.transform.scale(ball_image, [50, 50])
ball = Ball([400, 300], ball_image, 7)

player_image = pygame.image.load('racket.png').convert_alpha()
player_image = pygame.transform.scale(player_image, [100, 100])
right_player = Player([20, 300], player_image, pygame.K_w, pygame.K_s, 12)
player_image = pygame.transform.flip(player_image, True, False)
left_player = Player([780, 300], player_image, pygame.K_UP, pygame.K_DOWN, 12)

background_image = pygame.image.load('background.png').convert_alpha()
background_image = pygame.transform.scale(background_image, [800, 600])

running = True

score = {
    "left": 0,
    "right": 0
}

while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
    
    right_player.update()
    left_player.update()
    ball.update()

    if right_player.rect.colliderect(ball.rect):
        ball.direction.x = -ball.direction.x
        ball.direction.rotate_ip(randint(-20, 20))
        ball.speed += 0.5

    if left_player.rect.colliderect(ball.rect):
        ball.direction.x = -ball.direction.x
        ball.direction.rotate_ip(randint(-20, 20))
        ball.speed += 0.5

    if ball.rect.left > 800:
        score['left'] += 1
        restart()
    if ball.rect.left < 0:  
        score['right'] += 1
        restart() 

    surface.fill('white')
    surface.blit(background_image, [0, 0])

    right_player.render()
    left_player.render()
    ball.render()

    sc1 = f'{score["left"]}|{score["right"]}'
    sc2 = font.render(sc1,True,"green")
    surface.blit(sc2, sc2.get_rect(midtop = [400, 10]))

    window.flip()
    clock.tick(60)