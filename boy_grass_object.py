from pico2d import *

# Game object class here
class Grass:
    pass



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    pass


def render_world():
    clear_canvas()
    update_canvas()


def reset_world(): #초기화 함수
    global running
    global grass   #다른곳에서도 볼 수 있도록 글로벌 처리
    running=True
    grass=Grass()#글래스라는 클래스를 이용해서 grass객체를 생성




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
