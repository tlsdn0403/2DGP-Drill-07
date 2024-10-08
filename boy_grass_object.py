from pico2d import *
import random

# Game object class here
class Grass:
    #생성자를 이용해서 객체의 초기 상태를 정의
    def __init__(self): # self:모양이 전혀 없는 순수한 붕어빵이다
        self.image=load_image('grass.png')

    def update(self): #잔디는 움직이지않음으로
        pass

    def draw(self):
        self.image.draw(400,30)
    pass

class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame=0
        self.image=load_image('run_animation.png')
    
    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)
class Ball:
    def __init__(self):
        self.x,self.y=400,90
        self.image=load_image('ball21x21.png')
    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x,self.y)
        

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    grass.update()
    for boy in team:
        boy.update()
    ball.update()
    pass


def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    ball.draw()
    update_canvas()


def reset_world(): #초기화 함수
    global running
    global grass   #다른곳에서도 볼 수 있도록 글로벌 처리
    global team
    global ball
    running=True
    grass=Grass()#글래스라는 클래스를 이용해서 grass객체를 생성
    team=[Boy() for i in range(10)]
    ball=Ball()




open_canvas()

# initialization code 객체를 초기에 창조함
reset_world()


# game main loop code
while running:
    handle_events() #입력 이벤트 처리
    update_world()
    render_world()
    delay(0.05) 


# finalization code

close_canvas()
