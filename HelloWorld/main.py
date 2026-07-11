import engine_main
import engine
import engine_io
import engine_time
import engine_debug

from engine_nodes import CameraNode, Text2DNode
from engine_resources import FontResource
from engine_math import Vector2

screenSize = 128
fontSize = 12

hello = Text2DNode(text = "Hello World", scale = Vector2(2, 2))
#font = FontResource("/Games/HelloWorld/Portfolio6x8-1bit.bmp")
#hello = Text2DNode(text = "Hello World", font = font, scale = Vector2(2, 2))

# ファームウェア
firmware = Text2DNode(text = engine.firmware_date(), position = Vector2(0, -screenSize / 2 + fontSize / 2))
# バッテリー
batteryText = "plug={}, chg={}\n\nlv={}, volt={}".format(engine_io.is_plugged_in(), engine_io.is_charging(), engine_io.battery_level(), engine_io.battery_voltage())
battery = Text2DNode(text = batteryText, position = Vector2(0, -screenSize / 2 + fontSize / 2 + fontSize * 2))

cam = CameraNode()

#engine.start()

#engine_debug.enable_all()
#engine_debug.disable_all()

while True:
    if engine.tick():       
        if engine_io.MENU.is_just_long_pressed:
            break