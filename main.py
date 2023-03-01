import pygame as pg
import random

pg.init()  # инициализируем пайгейм
pg.font.init()  # инициализируем шрифт
# в будущем работа со звуком

TITLE = "PING_AND_PONG"  # название окна
WIDTH = 800  # длина
HEIGHT = 650  # высота
FPS = 60  # ЗНАЧЕНИЕ кадры в секунду

RED = (255, 0, 0)  # цвета
YELLOW = (255, 255, 0)  # цвета
GREEN = (0, 255, 0)  # цвета
BLACK = (0, 0, 0)  # цвета
BLUE = (0, 0, 200)  # цвета
PL_WIDTH = 100  # размеры платформы
PL_HEIGHT = 15  # размеры платформы
Pl_SPEED = 8  # скорость платформы
platform1_rect = pg.rect.Rect(WIDTH // 2 - PL_WIDTH // 2, HEIGHT - 2 * PL_HEIGHT, PL_WIDTH,
                              PL_HEIGHT)  # создаём платформу1

platform2_rect = pg.rect.Rect(WIDTH // 2 - PL_WIDTH // 2, 2 * PL_HEIGHT, PL_WIDTH,
                              PL_HEIGHT)  # создаём платформу1

CIRCLE_RADIUS = 15
CIRCLE_SPEED = 8
CIRCLE_NAPR = False
circle_x_speed = 0  # скорость шарика по иксу
circle_y_speed = CIRCLE_SPEED  # скорость шарика по игрику
circle_rect = pg.rect.Rect(WIDTH // 2 - CIRCLE_RADIUS, HEIGHT // 2 - CIRCLE_RADIUS, CIRCLE_RADIUS * 2,
                           CIRCLE_RADIUS * 2)  # КООРДИНАТЫ ШАРИКА
screen = pg.display.set_mode([WIDTH, HEIGHT])  # размеры экрана
pg.display.set_caption(TITLE)  # название окна на экран
ARIAL_FONT = pg.font.match_font('arial')  # ПУТЬ ДО ШРИФТА АРИАЛ
ARIAL_FONT_48 = pg.font.Font(ARIAL_FONT, 48)  # НЕПОСРЕДСТВЕННО САМ ШРИФТ И РАЗМЕР
ARIAL_FONT_36 = pg.font.Font(ARIAL_FONT, 36)  # ШРИФТ ПЕРЕЗАПУСК ИГРЫ
score1 = 0
score2 = 0
clock = pg.time.Clock()

game_over = False  # переменная конца игры
running = True  # начало игрового цикла
while running:
    for event in pg.event.get():  # выход из программы при нажатии заркыть окно
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:  # движение досок по нажатию кнопок
            if event.key == pg.K_ESCAPE:
                game_over = False
                score1 = 0
                score2 = 0
                circle_rect = pg.rect.Rect(WIDTH // 2 - CIRCLE_RADIUS, HEIGHT // 2 - CIRCLE_RADIUS, CIRCLE_RADIUS * 2,
                                           CIRCLE_RADIUS * 2)
                CIRCLE_SPEED = 8
                circle_y_speed = 8
                CIRCLE_NAPR = False
    screen.fill(BLACK)
    if not game_over:  # движение досок по нажатию кнопок
        keys = pg.key.get_pressed()  # список нажатых клавиш
        if keys[pg.K_a]:
            platform1_rect.x -= Pl_SPEED
        if keys[pg.K_d]:
            platform1_rect.x += Pl_SPEED
        if keys[pg.K_n]:
            platform2_rect.x -= Pl_SPEED
        if keys[pg.K_m]:
            platform2_rect.x += Pl_SPEED
        if platform1_rect.colliderect(circle_rect):
            score1 += 1
            if not CIRCLE_NAPR:
                if random.randrange(0, 1) == 0:
                    circle_x_speed = CIRCLE_SPEED
                else:
                    circle_x_speed = -CIRCLE_SPEED
                CIRCLE_NAPR = True
            circle_y_speed = -CIRCLE_SPEED
        if platform2_rect.colliderect(circle_rect):
            score2 += 1
            circle_y_speed = CIRCLE_SPEED


        pg.draw.rect(screen, RED, platform1_rect)  # рисуем платформу1
        pg.draw.rect(screen, BLUE, platform2_rect)  # рисуем платформу2
    circle_rect.x -= circle_x_speed  # перемешение шарика
    circle_rect.y += circle_y_speed  # перемешение шарика
    if circle_rect.bottom >= HEIGHT:  # ПРОВЕРКА НЕ ВЫХОДИТ ЛИ ШАРИК ЗА НИЖНЮЮ ГРАНИЦУ
        game_over = True
        circle_y_speed = 0
        circle_x_speed = 0
    elif circle_rect.top <= 0:  # ПРОВЕРКА НЕ ВЫХОДИТ ЛИ ШАРИК ЗА ВЕРХНЮЮ ГРАНИЦУ
        circle_y_speed = CIRCLE_SPEED
        game_over = True
        circle_y_speed = 0
        circle_x_speed = 0
    elif circle_rect.left <= 0:
        circle_x_speed = -CIRCLE_SPEED
    elif circle_rect.right >= WIDTH:
        circle_x_speed = CIRCLE_SPEED
    pg.draw.circle(screen, YELLOW, circle_rect.center, CIRCLE_RADIUS)
    score_surface1 = ARIAL_FONT_48.render(str(score1), True, GREEN)
    score_surface2 = ARIAL_FONT_48.render(str(score2), True, GREEN)
    if not game_over:
        screen.blit(score_surface1, [score_surface1.get_width() // 2, 15])
        screen.blit(score_surface1, [WIDTH - score_surface2.get_width() * 2, 15])
    else:
        retry_surface1 = ARIAL_FONT_36.render('PRESS ESCAPE TO RESTART', True, GREEN)
        screen.blit(score_surface1, [WIDTH // 2 - score_surface1.get_width() // 2, HEIGHT // 3])
        screen.blit(retry_surface1,
                    [WIDTH // 2 - retry_surface1.get_width() // 2, HEIGHT // 3 + score_surface1.get_height()])
        CIRCLE_SPEED = 0
    clock.tick(FPS)  # замедляем доску, на всех компьютерах одинаковая скорость перемещения
    pg.display.flip()  # смена кадра
pg.quit()
