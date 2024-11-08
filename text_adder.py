from PIL import Image, ImageDraw, ImageFont

# イメージのパス
image_path = ''#←ここにパス入れてね
# 出力用パス
output_path = "_" + image_path


img = Image.open(image_path)
d = ImageDraw.Draw(img)

# フォントと大きさを指定する
# もし指定するフォントがなかったらデフォルトを使う
try:
    # font = ImageFont.truetype("MPLUS1thin", 18)
    font = ImageFont.truetype("MPLUS1-VariableFont_wght.ttf", 18)
except IOError:
    font = ImageFont.load_default()
    print("Font not found. Using default font.")

# 加えたい文字（今回はIDなのでそのままちょっと操作するだけ）
text = image_path.replace(".png", "")


# 文字の高さと横幅を取得する
bbox = d.textbbox((0, 0), text, font=font)

# 幅と高さを計算
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

print(text_width, text_height)

# 下中央に配置させる
text_x = (img.width - text_width) / 2 # 中央配置
text_y = img.height - text_height - 10 # 10ピクセル残す

# 文字を書く
d.text((text_x, text_y), text, font=font, fill=(0, 0, 0))

# 画像をセーブ
img.save(output_path)

print(f"ここに保存したよ→ {output_path}")