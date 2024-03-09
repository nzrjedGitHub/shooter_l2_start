#Створи власний Шутер!

from pygame import *

# фонова музика
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

# нам потрібні такі картинки:
img_back = "galaxy.jpg"  # фон гри
img_hero = "rocket.png"  # герой

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, size_x, size_y, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y ))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для керування спрайтом стрілками клавіатури
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

# створюємо віконце
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# створюємо спрайти
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

# Основний цикл гри:
run = True  # прапорець скидається кнопкою закриття вікна
finish = False
clock = time.Clock()
FPS = 50

while run:
    # подія натискання на кнопку Закрити
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if not finish:
        # оновлюємо фон
        window.blit(background, (0, 0))

        # рухи спрайтів
        
        ship.update()
        
        ship.reset()

        display.update()


    clock.tick(FPS)