import os
import pygame as pg
import random
from pygame.compat import geterror

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "data")


def load_image(name, colorkey=None):
    fullname = os.path.join(data_dir, name)
    image = pg.image.load(fullname)
    try:
        image = pg.image.load(fullname)
    except pg.error:
        print("Cannot load image:", fullname)
        raise SystemExit(str(geterror()))
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pg.RLEACCEL)
    return image, image.get_rect()


def load_sound(name):
    class NoneSound:
        def play(self):
            pass

    if not pg.mixer or not pg.mixer.get_init():
        return NoneSound()
    fullname = os.path.join(data_dir, name)
    sound = pg.mixer.Sound(fullname)
    try:
        sound = pg.mixer.Sound(fullname)
    except pg.error:
        print("Cannot load sound: %s" % fullname)
        raise SystemExit(str(geterror()))
    return sound


pg.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 720
screen = pg.display.set_mode((screen_width, screen_height))
# 게임이름
pg.display.set_caption("Test")

# images
# 클래스로 구현하는걸 권장합니당.
background_image, background_image_size = load_image('test_background_image.png')
bullet_image, bullet_image_size = load_image('test_bullet_image.png')
character_image, character_image_size = load_image('test_character_image.png')
enemy_image, enemy_image_size = load_image('test_enemy_image.png')

character_image_width = character_image_size.size[0]
character_image_height = character_image_size.size[1]
enemy_image_width = enemy_image_size.size[0]
enemy_image_height = enemy_image_size.size[1]
bullet_image_width = bullet_image_size.size[0]

character_x_pos = 0
character_y_pos = screen_height - character_image_height

base_speed = 1

character_delta_x = 0
character_delta_y = 0
character_speed = 1

enemy_delta_y = 0
enemy_x_pos = screen_width - enemy_image_width
enemy_y_pos = screen_height / 2

bullets = []
bullet_speed = 1

enemys = []

enemys.append([enemy_x_pos, enemy_y_pos])
# 타임
pg_font = pg.font.Font(None, 48)
total_time = 10
start_time = pg.time.get_ticks()  # 시작 시간 정의

# 스코어
total_score = 0

def character_keydown_move(event_key, *args):
    """
    process character move
    """
    global character_speed, base_speed, character_delta_x, character_delta_y
    if event.key == pg.K_LEFT:
        character_delta_x -= base_speed * character_speed
    elif event.key == pg.K_RIGHT:
        character_delta_x += base_speed * character_speed
    elif event.key == pg.K_UP:
        character_delta_y -= base_speed * character_speed
    elif event.key == pg.K_DOWN:
        character_delta_y += base_speed * character_speed
def character_keyup_move(event_key, *args):
    """
    process character move
    """
    global character_speed, base_speed, character_delta_x, character_delta_y
    if event.key == pg.K_LEFT:
        character_delta_x = 0
    elif event.key == pg.K_RIGHT:
        character_delta_x = 0
    elif event.key == pg.K_UP:
        character_delta_y = 0
    elif event.key == pg.K_DOWN:
        character_delta_y = 0
def character_check_move(*args):
    global character_x_pos, character_y_pos
    if character_x_pos < 0:
        character_x_pos = 0
    if character_x_pos >= screen_width - character_image_width:
        character_x_pos = screen_width - character_image_width
    if character_y_pos < 0:
        character_y_pos = 0
    if character_y_pos >= screen_height - character_image_height:
        character_y_pos = screen_height - character_image_height
def bullet_make(bullets, *args):
    bullet_x_pos = character_x_pos + character_image_width - bullet_image_width // 2
    bullet_y_pos = character_y_pos + character_image_height // 2
    bullets.append([bullet_x_pos, bullet_y_pos])

# 이벤트
running = True
while running:
    for event in pg.event.get():
        # 종료 이벤트
        if event.type == pg.QUIT:
            running = False

        # 키 이벤트
        if event.type == pg.KEYDOWN:
            character_keydown_move(event.key)
            # 총알 발사
            if event.key == pg.K_SPACE:
                bullet_make(bullets)
        if event.type == pg.KEYUP:
            character_keyup_move(event.key)

    # 캐릭터 체크 무브
    character_check_move()

    # 캐릭터 이동
    character_x_pos += character_delta_x
    character_y_pos += character_delta_y

    # 충돌처리
    character_rect = character_image_size
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy_image_size
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print('Game Over')
        running = False

    for bullet in bullets:
        bullet_rect = bullet_image_size
        bullet_rect.left = bullet[0]
        bullet_rect.top = bullet[1]
        if bullet_rect.colliderect(enemy_rect):
            total_score += 10
            bullets.remove(bullet)
            for enemy in enemys:
                enemy_rect.left = enemy[0]
                enemy_rect.top = enemy[1]
                enemys.remove(enemy)
            random_y_pos = random.randint(0, screen_height-enemy_image_height)
            enemys.append([screen_width-enemy_image_width, random_y_pos])

    # 총알 이동
    bullets = [[bullet_x + bullet_speed, bullet_y] for bullet_x, bullet_y in bullets]
    # bullet 리스트는 늘기만 하여 메모리를 잡음 나중에 제거해줘야함

    # 배경
    screen.blit(background_image, (0, 0))

    # 시간
    delta_time = (pg.time.get_ticks() - start_time) // 1000
    remain_time = total_time - delta_time
    if remain_time <= 0:
        print('Time Over')
        running = False
    timer = pg_font.render(f"Time : {remain_time}", True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # 스코어
    score = pg_font.render(f'Score : {total_score}', True, (255, 255, 255))
    screen.blit(score, (10, 60))

    # 총알
    for bullet_x_pos, bullet_y_pos in bullets:
        screen.blit(bullet_image, (bullet_x_pos, bullet_y_pos))

    # 우리팀
    screen.blit(character_image, (character_x_pos, character_y_pos))

    # 적팀
    for enemy_x_pos, enemy_y_pos, in enemys:
        screen.blit(enemy_image, (enemy_x_pos, enemy_y_pos))

    # 업데이트
    pg.display.update()

pg.time.delay(2000)
pg.quit()