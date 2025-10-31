import asyncio
import curses
import itertools
import os
import random
import time

from animations.gun_shot import fire
from animations.spaceship.curses_tools import draw_frame, read_controls, get_frame_size

from dotenv import load_dotenv


load_dotenv()


TIC_TIMEOUT = 0.1
STARS_COUNT = int(os.getenv('STARS_COUNT', 200))
SPACESHIP_SPEED = int(os.getenv('SPACESHIP_SPEED', 2))


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(random.randint(0, 20)):
            await asyncio.sleep(0)
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)


async def animate_spaceship(canvas, coroutines):
    height, width = canvas.getmaxyx()
    
    with open('animations/spaceship/rocket_frame_1.txt', 'r') as file_content:
        frame_1 = file_content.read()
    
    with open('animations/spaceship/rocket_frame_2.txt', 'r') as file_content:
        frame_2 = file_content.read()
    
    frames = [frame_1, frame_2]
    
    ship_height, ship_width = get_frame_size(frame_1)

    ship_row = height // 2
    ship_column = width // 2 - ship_width // 2

    for frame in itertools.cycle(frames):
        rows_dir, cols_dir, space_pressed = read_controls(canvas)

        ship_row += rows_dir * SPACESHIP_SPEED
        ship_column += cols_dir * SPACESHIP_SPEED

        ship_row = max(1, min(ship_row, height - ship_height - 1))
        ship_column = max(1, min(ship_column, width - ship_width - 1))

        if space_pressed:
            fire_row = ship_row
            fire_col = ship_column + ship_width // 2
            coroutines.append(fire(canvas, fire_row, fire_col))
        
        draw_frame(canvas, ship_row, ship_column, frame)
        await asyncio.sleep(0)
        draw_frame(canvas, ship_row, ship_column, frame, negative=True)

    
def draw(canvas):
    canvas.border()
    curses.curs_set(False)
    canvas.nodelay(True)
    
    coroutines = []
    
    height, width = canvas.getmaxyx()
    symbols = ['*', '+', '.', ':']
    for _ in range(STARS_COUNT):
        row = random.randint(1, height - 2)
        column = random.randint(1, width - 2)
        symbol = random.choice(symbols)
        coroutines.append(blink(canvas, row, column, symbol))
    
    coroutines.append(animate_spaceship(canvas, coroutines))

    while coroutines:
        for coroutine in coroutines.copy():
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)

        canvas.refresh()
        time.sleep(TIC_TIMEOUT)

        
if __name__ == '__main__':
    curses.wrapper(draw)