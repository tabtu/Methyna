import time, random
from pygame.locals import *
import pygame


class Bullet:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load("./images/pd.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 10
        if self.y <= -20:
            return True


class EnemyBullet:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load("./images/epd.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 8
        if self.y >= 520:
            return True

class HeroPlane:
    def __init__(self, screen):
        self.x = 200
        self.y = 400
        self.screen = screen
        self.image = pygame.image.load("./images/me.png")
        self.bullet_list = []
        self.d = 21

    def display(self):
        for a in self.bullet_list:
            a.display()
            if a.move():
                self.bullet_list.remove(a)
        self.screen.blit(self.image, (self.x, self.y))

    def move_l(self):
        self.x -= 5
        if self.x <= 0:
            self.x = 0

    def move_r(self):
        self.x += 5
        if self.x >= 406:
            self.x = 406

    def move_u(self):
        self.y -= 5
        if self.y <= 0:
            self.y = 0

    def move_d(self):
        self.y += 5
        if self.y >= 492:
            self.y = 492

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x + 53, self.y))

    def dead(self):
        self.d -= 1


class EnemyPlane:
    def __init__(self, screen):
        self.x = random.choice(range(408))
        self.y = -85
        self.screen = screen
        self.image = pygame.image.load("./images/e2.png")
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, hero):
        self.y += 4
        if self.y >= 700:
            return True
        for a in hero.bullet_list:
            if self.x+12 < a.x < self.x+92 and self.y + 20 < a.y < self.y + 60:
                hero.bullet_list.remove(a)
                return True

# 爆炸类
class Boom:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.n = 0
        self.screen = screen
        self.image = None

    def display(self):
        self.image = pygame.image.load("./images/bomb" + str(int(self.n / 5)) + ".png")
        self.screen.blit(self.image, (self.x, self.y))
        self.n += 1

def get_key(hero):
    for e in pygame.event.get():
        if e.type == QUIT:
            print("exit")
            exit()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        hero.move_l()
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        hero.move_r()

    if pressed_keys[K_UP] or pressed_keys[K_w]:
        hero.move_u()
    elif pressed_keys[K_DOWN] or pressed_keys[K_s]:
        hero.move_d()

    if pressed_keys[K_SPACE]:
        hero.fire()


def main():
    screen = pygame.display.set_mode((512, 568), 0, 0)

    bg = pygame.image.load("./images/bg2.jpg")
    hero = HeroPlane(screen)

    m = -968
    enemy_list = []
    enemy_bullet_list = []
    boom_list = []
    while 1:

        screen.blit(bg, (0, m))
        hero.display()
        if random.choice(range(30)) == 10:
            enemy_list.append(EnemyPlane(screen))
        for em in enemy_list:
            em.display()
            # 新的敌机子弹（飞机消失后子弹还在~）
            if random.choice(range(60)) == 0:
                enemy_bullet_list.append(EnemyBullet(screen, em.x + 51, em.y + 57))
            if em.move(hero):
                boom_list.append(Boom(screen, em.x, em.y))
                enemy_list.remove(em)

        # 子弹显示及碰撞判定
        for ea in enemy_bullet_list:
            ea.display()
            if hero.x + 12 < ea.x + 1 < hero.x + 94 and hero.y + 12 < ea.y + 17 < hero.y + 32:
                # 添加英雄死亡爆炸~
                enemy_bullet_list.remove(ea)
                boom_list.append(Boom(screen, hero.x, hero.y))
                hero.dead()
                print("游戏结束")
            ea.move()
        
        # 飞机爆炸显示
        for b in boom_list:
            b.display()
            if b.n > 19:
                boom_list.remove(b)

        pygame.display.update()
        
        # 英雄死亡画面
        if hero.d < 21:
            hero.dead()
            if hero.d == 0:
                exit()
        get_key(hero)

        m += 2
        if m >= -200:
            m = -968
        time.sleep(0.02)


if __name__ == "__main__":
    main()
