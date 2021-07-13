# 모듈 불러오기

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

# 윈도우 만들기

app = Ursina()

# 카메라 설정

camera.orthographic = True
camera.fov = 20

# Background 만들기

background = Entity(
    model = 'cube',
    texture = 'main_backgorund_img.jpg',
    scale = (40, 20, 1),
    z = 2
)

# Ground 만들기

ground = Entity(
    model = 'cube',
    color = color.rgb(50, 180, 50),
    z = 0.1,
    y = -8,
    scale = (100, 5, 10),
    collider ='box'
)

# Wall 만들기

wall = Entity(
    model = 'cube',
    # color = color.black,
    collider = 'box',
    position = (-3, 0),
    scale = (6, 3),
    texture = 'jump_wall.png'
)

# 플레이어 만들기 / 큐브 모양, 오렌지색, 높이 2

# player = Entity(
#     model = 'cube',
#     color = color.orange,
#     scale_y = 1,
#     position = (-15, -5)
# )
player = PlatformerController2d(
    position = (-15, -5),
    color = color.white,
    scale = 1,
    max_jumps = 2,
    texture = 'main_bosh_image.png'
)

# spike 생성

spikes = []

# for i in range(5):
#     spike = Entity(
#         model = 'cube',
#         # color = color.white,
#         collider = 'box',
#         position = (random.randint(-10, 10), -5),
#         scale = 2,
#         texture = 'bosh_spike_2.png'
#     )
#     spikes.append(spike)
for i in range(5):
    spike = Entity(
        model = 'cube',
        # color = color.black,
        collider = 'box',
        position = (random.randint(-10, 10), -5),
        scale = 2,
        texture = 'spike.png'
    )
    spikes.append(spike)

# 업데이트 함수 만들기 / d누르면 우측으로 이동, a누르면 좌측으로 이동

def update():
    # player.x += held_keys['d']*time.dt
    # player.x -= held_keys['a']*time.dt
    
    hit_info = player.intersects()
    
    if hit_info.hit:
        if hit_info.entity in spikes:
            player.position = (-15, -5)

# 입력 함수 만들기 / space누르면 위로 이동, 0.25초 이후에 아래로 이동

# def input(key):
#     if key == 'space':
#         player.y += 1
#         invoke(setattr, player, 'y', player.y-1, delay = 0.25)
       
# 게임 실행하기
       
app.run()