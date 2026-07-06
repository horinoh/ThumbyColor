import engine_main
import engine

from engine_nodes import CameraNode, Text2DNode
from engine_resources import FontResource
from engine_math import Vector2

text = Text2DNode(text = "Hello World", scale = Vector2(2, 2))
#font = FontResource("/Games/HelloWorld/Portfolio6x8-1bit.bmp")
#text = Text2DNode(text = "Hello World", font = font, scale = Vector2(2, 2))

cam = CameraNode()

engine.start()