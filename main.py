import pygame

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
        
pygame.init()

window = pygame.Window('PingPong', [800,600])
surface = window.get_surface()
clock = pygame.Clock()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
player_image = pygame.image.load('racket.png').convert_alpha()
player_image = pygame.transform.scale(player_image, [100, 100])
right_player = Player([20, 300], player_image, pygame.K_w, pygame.K_s, 12)
player_image = pygame.transform.flip(player_image, True, False)
left_player = Player([780, 300], player_image, pygame.K_UP, pygame.K_DOWN, 12)

background_image = pygame.image.load('background.png').convert_alpha()
background_image = pygame.transform.scale(background_image, [800, 600])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
    
    right_player.update()
    left_player.update()

    surface.fill('white')
    surface.blit(background_image, [0, 0])
    right_player.render()
    left_player.render()

    window.flip()
    clock.tick(60)