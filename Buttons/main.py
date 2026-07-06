import engine_main
import engine
import engine_io
import engine_draw
from engine_math import Vector2

from engine_nodes import CameraNode, Text2DNode

UP = Text2DNode(text = "o", position = Vector2(-32, 16 - 8))
DOWN = Text2DNode(text = "o", position = Vector2(-32, 16 + 8))
LEFT = Text2DNode(text = "o", position = Vector2(-32 - 8, 16))
RIGHT = Text2DNode(text = "o", position = Vector2(-32 + 8, 16))

A = Text2DNode(text = "o", position = Vector2(32 + 16, 8))
B = Text2DNode(text = "o", position = Vector2(32, 16))

LB = Text2DNode(text = "o", position = Vector2(-32, -32))
RB = Text2DNode(text = "o", position = Vector2(32, -32))

MENU = Text2DNode(text = "o", position = Vector2(-32 + 8, 16 + 24))

cam = CameraNode()

while True:
    if engine.tick():               
        # 長押し
        if engine_io.A.is_just_long_pressed:
            print("A long pressed")
        # 短押し
        if engine_io.A.is_just_short_released:
            print("A.short released")
        # 2回短押し
        if engine_io.A.is_just_double_released:
            print("A double released")
        # リピート
        if engine_io.A.is_pressed_autorepeat:
            print("A autorepeat")

        UP.color = engine_draw.white if engine_io.UP.is_pressed else engine_draw.darkgrey
        DOWN.color = engine_draw.white if engine_io.DOWN.is_pressed else engine_draw.darkgrey
        LEFT.color = engine_draw.white if engine_io.LEFT.is_pressed else engine_draw.darkgrey
        RIGHT.color = engine_draw.white if engine_io.RIGHT.is_pressed else engine_draw.darkgrey
        
        A.color = engine_draw.white if engine_io.A.is_pressed else engine_draw.darkgrey
        B.color = engine_draw.white if engine_io.B.is_pressed else engine_draw.darkgrey
        
        LB.color = engine_draw.white if engine_io.LB.is_pressed else engine_draw.darkgrey
        RB.color = engine_draw.white if engine_io.RB.is_pressed else engine_draw.darkgrey
        
        MENU.color = engine_draw.white if engine_io.MENU.is_pressed else engine_draw.darkgrey

        if engine_io.MENU.is_just_long_pressed:
            break
        
#         engine_io.UP.print_info()
#         engine_io.DOWN.print_info()
#         engine_io.LEFT.print_info()
#         engine_io.RIGHT.print_info()

#         engine_io.A.print_info()
#         engine_io.B.print_info()

#         engine_io.LB.print_info()
#         engine_io.RB.print_info()

#         engine_io.MENU.print_info()

