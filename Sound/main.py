import engine_main
import engine
import engine_io
import engine_audio

from engine_math import Vector2

from engine_resources import ToneSoundResource, WaveSoundResource, RTTTLSoundResource
from engine_nodes import CameraNode, Text2DNode

import time

tone = ToneSoundResource()

pre = time.ticks_ms()
wave = WaveSoundResource("/Games/Sound/random.wav")
rtttl = RTTTLSoundResource("/Games/Sound/test.rtttl")
print("loaded in {} ms".format(time.ticks_ms() - pre))

#engine.fps_limit(60)
engine_audio.set_volume(5.0)

cam = CameraNode()
toneText = Text2DNode(text = "", position = Vector2(0, 0))

while True:
    if engine.tick():     
        if engine_io.A.is_just_pressed:
            # トーンをチャンネル0 ([0, 3]) でループ再生
            engine_audio.play(tone, 0, True)
        if engine_io.B.is_just_pressed:
            # ウェーブをチャンネル0 で非ループ再生
            engine_audio.play(wave, 0, False)
        
        # トーン再生時に周波数を変更可能にする
        if engine_io.LB.is_pressed:
            tone.frequency -= 10
        if engine_io.RB.is_pressed:
            tone.frequency += 10
        toneText.text = "Tone = {}".format(tone.frequency)
        
        if engine_io.MENU.is_just_long_pressed:
            break