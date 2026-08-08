import engine_main
import engine_io
import engine_link
import engine

from engine_nodes import CameraNode, Sprite2DNode
from engine_resources import TextureResource
from engine_math import Vector2
import engine_draw

# 送受信バッファ
buffer = bytearray(8)

speed = 0.5
p1StartPos = Vector2(-10, 0)
p2StartPos = Vector2(10, 0)

# スプライト
p1Color = TextureResource(16, 16, engine_draw.blue)
p2Color = TextureResource(16, 16, engine_draw.red)
p1Sprite = Sprite2DNode(texture = p1Color, position = p1StartPos)
p2Sprite = Sprite2DNode(texture = p2Color, position = p1StartPos)

mySp = None
enSp = None

# 接続時のコールバック
def onConnected():
    print("onConnected")
    # 送受信をクリア
    engine_link.clear_send()
    engine_link.clear_read()
    if engine_link.is_host():
        # ホストが 1P (青、左側)
        mySp = p1Sprite
        enSp = p2Sprite
    else:
        # ゲストが 2P (赤、右側)
        mySp = p2Sprite
        enSp = p1Sprite
    
# 切断時のコールバック
def onDisconnected():
    print("onDisconnected")

# 接続、切断時のコールバック登録
engine_link.set_connected_cb(onConnected)
engine_link.set_disconnected_cb(onDisconnected)

camera = CameraNode()

while True:
    if engine.tick():
        # MENU 長押しで終了
        if engine_io.MENU.is_just_long_pressed:
            if engine_link.is_started():
                engine_link.stop()
            break
        
        # MENU で接続開始
        if not engine_link.is_started():
            if engine_io.MENU.is_just_pressed:
                # 接続開始
                engine_link.start()
        
        # 接続してなければ continue (PC に接続していても true になるので注意)
        if not engine_link.connected():
            continue
        
        # 受信 : 8 バイト以上届いていたら受信
        if engine_link.available() >= len(buffer):
            engine_link.read_into(buffer, len(buffer))
            # 最初の 4 バイト x
            enSp.position.x = (buffer[0] << 24) | (buffer[1] << 16) | (buffer[2] << 8) | buffer[3]
            # 続く 4 バイト y
            enSp.position.y = (buffer[4] << 24) | (buffer[5] << 16) | (buffer[6] << 8) | buffer[7]
            
        # キー入力による移動 (入力があれば要送信フラグを立てる)
        toSend = False
        if mySp is None:
            continue
        if engine_io.UP.is_pressed:
            mySp.position.y -= speed
            toSend = True
        elif engine_io.DOWN.is_pressed:
            mySp.position.y += speed
            toSend = True
        elif engine_io.LEFT.is_pressed:
            mySp.position.x -= speed
            toSend = True
        elif engine_io.RIGHT.is_pressed:
            mySp.position.x += speed
            toSend = True
            
        # 送信 : 位置(8 バイト) を送信
        if toSend:
            x = int(mySp.position.x)
            y = int(mySp.position.y)
            # 最初の 4 バイト x
            buffer[0] = (x >> 24) & 0b11111111
            buffer[1] = (x >> 16) & 0b11111111
            buffer[2] = (x >> 8) & 0b11111111
            buffer[3] = (x >> 0) & 0b11111111
            # 続く 4 バイト y
            buffer[4] = (y >> 24) & 0b11111111
            buffer[5] = (y >> 16) & 0b11111111
            buffer[6] = (y >> 8) & 0b11111111
            buffer[7] = (y >> 0) & 0b11111111
            engine_link.send(buffer)
            
