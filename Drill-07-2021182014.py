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
        self.x,self.y=random.randint(0,200),90
        self.frame=random.randint(0,7)
        self.image=load_image('run_animation.png')
    
    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


class Ball:
    def __init__(self):
        self.x,self.y=random.randint(0,799),599
        self.down=random.randint(3,8)
        ran=random.randint(0,1)
        if ran==1:
            self.image=load_image('ball21x21.png')
        else:
            self.image=load_image('ball41x41.png')
        
    def update(self):
        if self.y>60:
            self.y-=self.down
    def draw(self):
        self.image.draw(self.x,self.y)
        


##################          함수       ######################


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
   for o in world:
       o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def reset_world(): #초기화 함수
    global running
    global grass   #다른곳에서도 볼 수 있도록 글로벌 처리
    global team
    global balls
    global world
    running=True
    world=[]
    grass=Grass()#글래스라는 클래스를 이용해서 grass객체를 생성
    world.append(grass)

    team=[Boy() for i in range(10)]
    world+=team

    balls=[Ball() for i in range(20)]
    world+=balls




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
