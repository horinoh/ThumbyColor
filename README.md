# ThumbyColor

[参考](https://color.thumby.us/home/)

## 準備

### [Thonny](https://thonny.org/)

- インストールして起動する
- Tools - Options - Interpreter の設定
    - Which kind of interpreter should Thonny use for running your code
        - MicroPython (Raspberry Pi Pico) を選択
    - Port of WebREPL 
        - \<Try to detect port automatically\> を選択
- View - Files, Shell にチェックを入れておく
- ThumyColor を USB-C で接続、電源を入れる
- (赤の) "Stop" ボタンを押す
    - Shell ウインドウに ">>>" が出れば成功
- TinyCircuits-Thumby-Code-Editor/CoreThumbyFiles/lib を右クリックして / へアップロードしておく

### ゲームのアップロード
- PC の TinyCircuits-Thumby-Color-Games/ 以下のゲームをデバイスの Games/ 以下へアップロードする
    - デバイス側 (左下ペイン) の Games/ をダブルクリックして選択した状態にする
    - PC側 (左上ペイン) のフォルダを右クリック - "Upload to /"

### プログラム作成
- Thonny にコードを記述して (緑の)"▶" (F5) で実行
    ~~~
    import engine_main
    import engine
    from engine_nodes import Rectangle2DNode, CameraNode
    rect = Rectangle2DNode()
    cam = CameraNode()
    engine.start()
    ~~~

