import engine_main
import engine
import engine_io
import engine_time
import engine_debug
import engine_save
import engine_draw
from engine_math import Vector2, Vector3
from engine_nodes import CameraNode, Text2DNode

# セーブ準備
engine_save._init_saves_dir("/Games/Save")
engine_save.set_location("save.data")

screenSize = 128
fontSize = 12

# ↑:セーブ、↓:ロード, ←→:削除 の説明
manStr = "U:Save, D:Load, L:Del"
manText = Text2DNode(text=manStr, position=Vector2(-screenSize/2 + len(manStr)/2 * fontSize/2, screenSize/2 - fontSize))

cam = CameraNode()

class Data:
    def __init__(self):
        self.text2D = Text2DNode(position=Vector2(0, -screenSize/2 + fontSize*3))
        self.clear()
        
    # キャッシュデータへの書き込み
    def write(self):
        self.stringData = "Hello World"
        self.intData = 128
        self.floatData = 3.14
        self.vector2Data = Vector2(1, 1)
        self.vector3Data = Vector3(1, 1, 1)
        self.colorData = engine_draw.red.value
        self.byteArrayData = bytearray([0, 1, 2, 3])
    # キャッシュデータのクリア
    def clear(self):
        self.stringData = ""
        self.intData = 0
        self.floatData = 0
        self.vector2Data = Vector2(0, 0)
        self.vector3Data = Vector3(0, 0, 0)
        self.colorData = engine_draw.black.value
        self.byteArrayData = bytearray(0)
        
    # セーブデータの保存
    def save(self):
        engine_save.save("string", self.stringData)
        engine_save.save("int", self.intData)
        engine_save.save("float", self.floatData)
        engine_save.save("vector2", self.vector2Data)
        engine_save.save("vector3", self.vector3Data)
        engine_save.save("color", self.colorData)
        engine_save.save("bytearray", self.byteArrayData)
    # セーブデータの読込
    def load(self):
        # 第二引数はデータがない場合のデフォルト値
        self.stringData = engine_save.load("string", "default")
        self.intData = engine_save.load("int", 0)
        self.floatData = engine_save.load("float", 0.0)
        self.vector2Data = engine_save.load("vector2", Vector2(0, 0))
        self.vector3Data = engine_save.load("vector3", Vector3(0, 0, 0))
        self.colorData = engine_save.load("color", engine_draw.black.value)
        self.byteArrayData = engine_save.load("bytearray", bytearray(0))
    # セーブデータの削除
    def delete(self):
        engine_save.delete("string")
        engine_save.delete("int")
        engine_save.delete("float")
        engine_save.delete("vector2")
        engine_save.delete("vector3")
        engine_save.delete("color")
        engine_save.delete("bytearray")

    # キャッシュデータの描画
    def draw(self):
        self.text2D.text = "{}\n{}\n{}\n{},{}\n{},{},{}\n{}\n{}\n".format(self.stringData, self.intData, self.floatData,
                                                        self.vector2Data.x, self.vector2Data.y,
                                                        self.vector3Data.x, self.vector3Data.y, self.vector3Data.z,
                                                        self.colorData,
                                                        len(self.byteArrayData))
    # キャッシュデータの出力
    def print(self):
        print(self.stringData)
        print(self.intData)
        print(self.floatData)
        print(self.vector2Data)
        print(self.vector3Data)
        print(self.colorData)
        print(self.byteArrayData)

# データクラス
data = Data()

while True:
    if engine.tick():       
        if engine_io.MENU.is_just_long_pressed:
            break
        
        # A キャッシュデータ書き込み
        if engine_io.A.is_just_pressed:
            data.write()
        # B キャッシュデータクリア
        if engine_io.B.is_just_pressed:
            data.clear()          
        # MENU キャッシュデータ出力
        if engine_io.MENU.is_just_pressed:
            data.print()
            
        # ↑ セーブ
        if engine_io.UP.is_just_pressed:
            data.save()
        # ↓ ロード
        if engine_io.DOWN.is_just_pressed:
            data.load()
        # ←→ 削除
        if engine_io.LEFT.is_just_pressed or engine_io.RIGHT.is_just_pressed:
            data.delete()
        
        # キャッシュデータの描画
        data.draw()
        