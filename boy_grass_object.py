from pico2d import *

# Game object class here

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

open_canvas()

# initialization code 객체를 초기에 창조함
running=True


# game main loop code
while running:
    handle_events() #입력 이벤트 처리
    update_world()
    render_world()
    delay(0.05) 


# finalization code

close_canvas()
