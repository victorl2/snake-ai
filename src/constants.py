from enum import Enum

class COLOR:
    BLUE = (8,115,229)
    LIGHT_BLUE = (56, 212, 218)
    LIGHT_GREY = (200, 200, 200)
    BLACK  = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    DARKER_GREEN = (74,117,45)
    DARK_GREEN = (87,138,53)
    MEDIUM_GREEN = (162,208,74)
    LIGHT_GREEN = (171,214,83)

class TILE:
    EMPTY = 0
    FRUIT = -1
    WALL = -2

dark = True

def flip_background_color():
    global dark
    dark = not dark

def tile_to_color(tile: int) -> tuple:
    if tile == TILE.EMPTY: 
        return COLOR.MEDIUM_GREEN if dark else COLOR.LIGHT_GREEN
    elif tile == TILE.WALL:
        return COLOR.DARK_GREEN
    elif tile == TILE.FRUIT:
        return COLOR.RED
    elif is_snake(tile):
        return COLOR.BLUE
    else:
        raise ValueError(f"invalid tile value: {tile}")

def is_snake(tile: int) -> bool:
    return tile > 0