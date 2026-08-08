import engine_main
import engine
import engine_draw
import engine_io
import framebuf
from engine_resources import TextureResource

import random

engine.fps_limit(60)

# BG カラー
engine_draw.set_background_color(engine_draw.skyblue)

# BG をテクスチャにする場合に備えて読み込んでおく (RGB565 128x128 BMP でないとダメなので注意)
bgTex = TextureResource("/Games/Draw/image_16bit_128x128.bmp", in_ram=True)

# フレームバッファへの描画
def draw(fb):
    fb.text("Hello World", 0, 0, engine_draw.white.value)
    fb.rect(16, 16, 128 - 32, 128 - 32, engine_draw.blue.value, False)
    fb.line(16, 16, 128 - 16, 128 - 16, engine_draw.red.value)
    for i in range(100):
        fb.pixel(random.randint(0, 128), random.randint(0, 128), engine_draw.orange.value)
    
while True:
    if engine.tick():
        if engine_io.MENU.is_just_long_pressed:
            break

        if engine_io.A.is_just_pressed:
            # BG をテクスチャにします
            engine_draw.set_background(bgTex)
            
        # (バック) フレームバッファへ描画
        # 基本的にバックバッファへ操作を行う (フロントバッファの直接操作は基本的にしない)
        draw(engine_draw.back_fb())

        
        