import engine_main
import engine
import engine_io
import engine_time
import engine_debug
import engine_save
import engine_draw
from engine_math import Vector2, Vector3

engine_save._init_saves_dir("/Games/Save")
engine_save.set_location("save.data")

class Data:
    def __init__(self):
        self.clear()
    # キャッシュへの書き込み
    def write(self):
        self.stringData = "Hello World"
        self.intData = 128
        self.floatData = 3.14
        self.vector2Data = Vector2(1, 1)
        self.vector3Data = Vector3(1, 1, 1)
        self.colorData = engine_draw.red.value
        self.byteArrayData = bytearray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # キャッシュのクリア
    def clear(self):
        self.stringData = ""
        self.intData = 0
        self.floatData = 0
        self.vector2Data = Vector2(0, 0)
        self.vector3Data = Vector3(0, 0, 0)
        self.colorData = engine_draw.black.value
        self.byteArrayData = bytearray(0)
    # セーブ
    def save(self):
        engine_save.save("string", self.stringData)
        engine_save.save("int", self.intData)
        engine_save.save("float", self.floatData)
        engine_save.save("vector2", self.vector2Data)
        engine_save.save("vector3", self.vector3Data)
        engine_save.save("color", self.colorData)
        engine_save.save("bytearray", self.byteArrayData)
    def load(self):
        # 第二引数はデータがない場合のデフォルト値
        self.stringData = engine_save.load("string", "default")
        self.intData = engine_save.load("int", 0)
        self.floatData = engine_save.load("float", 0.0)
        self.vector2Data = engine_save.load("vector2", Vector2(0, 0))
        self.vector3Data = engine_save.load("vector3", Vector3(0, 0, 0))
        self.colorData = engine_save.load("color", engine_draw.black.value)
        self.byteArrayData = engine_save.load("bytearray", bytearray(0))
    # セーブの削除
    def delete(self):
        engine_save.delete("string")
        engine_save.delete("int")
        engine_save.delete("float")
        engine_save.delete("vector2")
        engine_save.delete("vector3")
        engine_save.delete("color")
        engine_save.delete("bytearray")
    def print(self):
        print(self.stringData)
        print(self.intData)
        print(self.floatData)
        print(self.vector2Data)
        print(self.vector3Data)
        print(self.colorData)
        print(self.byteArrayData)

data = Data()

while True:
    if engine.tick():       
        if engine_io.MENU.is_just_long_pressed:
            break
        
        # データ出力
        if engine_io.MENU.is_just_pressed:
            data.print()
        
        # セーブ
        if engine_io.A.is_just_pressed:
            data.save()
        
        # ロード
        if engine_io.B.is_just_pressed:
            data.load()
    
        # データ書き込み
        if engine_io.LB.is_just_pressed:
            data.write()
            
        # データ削除
        if engine_io.RB.is_just_pressed:
            data.delete()
        