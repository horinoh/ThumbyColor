import struct

def create_16bit_bmp_128x128(filename):
    w, h = 128, 128
    
    # 1. BMPファイルヘッダー (14バイト)
    # 識別子'BM'、ファイルサイズ、予約領域、ピクセルデータへのオフセット
    offset = 14 + 108  # BITMAPV4HEADERを使うため122バイト
    pixel_data_size = w * h * 2  # 128x128x2バイト = 32,768バイト
    file_size = offset + pixel_data_size
    bmp_header = struct.pack('<2sIHHI', b'BM', file_size, 0, 0, offset)
    
    # 2. DIBヘッダー (BITMAPV4HEADER: 108バイト)
    # 16bitカラーでRGB565を指定するため、ビットマスクが使えるV4形式を採用
    bi_size = 108
    bi_width = w
    bi_height = h
    bi_planes = 1
    bi_bit_count = 16
    bi_compression = 3  # 3 = BI_BITFIELDS (マスク指定有効化)
    bi_size_image = pixel_data_size
    bi_x_pels = 2835    # 72 DPI
    bi_y_pels = 2835
    bi_clr_used = 0
    bi_clr_important = 0
    
    # RGB565のビットマスク (赤5、緑6、青5)
    r_mask = 0xF800  # 1111100000000000
    g_mask = 0x07E0  # 0000011111100000
    b_mask = 0x001F  # 0000000000011111
    a_mask = 0x0000
    
    cs_type = b'Win '
    endpoints = b'\x00' * 36
    r_gamma = 0
    g_gamma = 0
    b_gamma = 0
    
    dib_header = struct.pack(
        '<IiiHHIIiiIIIIII4s36sIII',
        bi_size, bi_width, bi_height, bi_planes, bi_bit_count,
        bi_compression, bi_size_image, bi_x_pels, bi_y_pels, bi_clr_used, bi_clr_important,
        r_mask, g_mask, b_mask, a_mask,
        cs_type, endpoints, r_gamma, g_gamma, b_gamma
    )
    
    # 3. ピクセルデータの生成 (RGB565)
    # テスト表示しやすいよう、X/Y軸に応じたグラデーションを作成
    pixel_data = bytearray()
    for y in range(h):
        for x in range(w):
            r = int((x / 127) * 31)          # 0〜31 (5bit)
            g = int((y / 127) * 63)          # 0〜63 (6bit)
            b = int(((127 - x) / 127) * 31)  # 31〜0 (5bit)
            
            # 16ビットのデータに結合 (RRRRRGGGGGGBBBBB)
            pixel = (r << 11) | (g << 5) | b
            # リトルエンディアンで2バイト書き込み
            pixel_data.extend(struct.pack('<H', pixel))
            
    # ファイル書き込み
    with open(filename, 'wb') as f:
        f.write(bmp_header)
        f.write(dib_header)
        f.write(pixel_data)

# 実行してファイルを生成
create_16bit_bmp_128x128('image_16bit_128x128.bmp')
print("BMPファイルの生成が完了しました。(サイズ: 32,890バイト)")
