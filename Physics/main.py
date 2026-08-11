import engine_main

import engine
import engine_draw
import engine_io
import engine_physics
from engine_math import Vector2
from engine_nodes import Rectangle2DNode, Circle2DNode, CameraNode, PhysicsRectangle2DNode, PhysicsCircle2DNode
#import random
import math

engine.fps_limit(60)

ofs = 30
for j in range(1):
    for i in range(3):
        x = -64 + ofs/2 + ofs * i
        
        # 矩形
        physRect = PhysicsRectangle2DNode(width=15, height=15, position=Vector2(x, 0), rotation=math.radians(0), dynamic=True, bounciness=0.5)
        rect = Rectangle2DNode(width=physRect.width, height=physRect.height, outline=True)
        physRect.add_child(rect)
        
        # 円
        physCircle = PhysicsCircle2DNode(radius=10, position=Vector2(x + ofs/2, -30), dynamic=True, bounciness=0.5)
        circle = Circle2DNode(outline=True, radius=physCircle.radius)
        physCircle.add_child(circle)

# 床
physFloor = PhysicsRectangle2DNode(width=128, height=10, position=Vector2(0, 64), dynamic=False, bounciness=1.0)
floor = Rectangle2DNode(width=physFloor.width, height=physFloor.height, color=engine_draw.green, outline=True)
physFloor.add_child(floor)

cam = CameraNode()

while True:
    if engine.tick():
        if engine_io.MENU.is_just_long_pressed:
            break