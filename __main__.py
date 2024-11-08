class TextAdder():
    def __init__(self, image_path, font, fontsize, font_color, text) -> None:
        self.image_path = image_path
        self.opener()
        self.font_setter(font, fontsize, font_color)
        self.text_setter(text)
        self.box_size_getter()
        self.text_placer()

    def opener(self) -> None:
        from PIL import Image, ImageDraw
        self.img = Image.open(self.image_path)
        self.draw = ImageDraw.Draw(self.img)
    
    def font_setter(self, font: str, fontsize: int, font_color: tuple):
        from PIL import ImageFont
        self.font_color = font_color
        try:
            self.font = ImageFont.truetype(font, fontsize)
        except IOError:
            self.font = ImageFont.load_default()
            print("Font not found. Using default font.")

    def text_setter(self, text: str):
        text: str = text.replace(".png", "")
        self.text = text
        self.textboxsize = self.draw.textbbox((0,0), self.text, font= self.font)
        self.text_width = self.textboxsize[2] - self.textboxsize[0]
        self.text_height = self.textboxsize[3] - self.textboxsize[1]
    
    def box_size_getter(self):
        if self.img:
            self.img_width = self.img.width
            self.img_height = self.img.height

    def text_placer(self):
        if self.text:
            self.text_x = (self.img_width - self.text_width) / 2
            self.text_y = (self.img_height - self.text_height) - 15
    
    def text_writter(self):
        self.draw.text((self.text_x, self.text_y), self.text, font=self.font, fill=self.font_color)
        
    def save_image(self, save_path):
        self.img.save(save_path)
        print(f"Image saved at {save_path}")
    
    def runner(self, savepath):
        self.text_writter()
        self.save_image(savepath)

if __name__ == "__main__":
    t = TextAdder("24_FL_QR_Insta.png", font="MPLUS1-VariableFont_wght.ttf", fontsize=18, font_color=(0,0,0), text="HogeHoge")
    t.runner("_24_FL_QR_Insta.png")

        
