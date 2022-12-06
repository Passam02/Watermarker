from PIL import Image, ImageDraw, ImageFont
import os

def main():
    path = "water_marked_images"
    if not os.path.exists(path):
        os.makedirs(path)
    
    while True:
        watermark_choose = input("Would you like to apply your own watermark or create it ? Answer Mine or Create: ")
        if watermark_choose[0].upper() == 'M':
            
            img_to_watermark, img = provide_image()
            watermark = provide_watermark()
                
            width, height = img_to_watermark.size
            watermark = watermark.resize((int(width/8), int(height/8)))
            width2, height2 = watermark.size
            img_to_watermark.paste(watermark, (width-width2, height-height2), watermark)
            print("Your image has been watermarked")
            img_to_watermark.show()
            img_to_watermark.save("water_marked_images/WM_"+img)
            
            repeat = do_you_want_to_repeat()
            if repeat == "yes":
                continue
            break
    
        elif watermark_choose[0].upper() == 'C':
            
            img_to_watermark, img = provide_image()
            chosen_color = choose_color()
            
            width, height = img_to_watermark.size
            created_text = input("Write the text you want to appear in your watermark: ")   
            font = ImageFont.truetype(font="arial.ttf", size=40)
            draw = ImageDraw.Draw(img_to_watermark)
            text_w, text_h = draw.textsize(created_text, font=font)
            draw.text((width-text_w, height-text_h), created_text, fill=chosen_color, font=font, align="right")
            print("Your image has been watermarked")
            img_to_watermark.show()
            img_to_watermark.save("water_marked_images/WM_"+img)
            
            repeat = do_you_want_to_repeat()
            if repeat == "yes":
                continue
            break

def provide_watermark():
    while True:
        try:
            wtmk = input("Now choose the watermark you want to use.\nWrite the path to it or it's name if it's in the same folder: ")
            watermark = Image.open(wtmk)
        except FileNotFoundError:
            print('No such file or directory, try again')
        else:
            break   
    return watermark

def provide_image():
    while True:
        try:
            img = input("Choose the image you want to watermark.\nWrite the path to it or it's name if it's in the same folder: ")
            img_to_watermark = Image.open(img)
        except FileNotFoundError:
            print('No such file or directory, try again')
        else:
            break
    return img_to_watermark,img.replace('/', '\\').split('\\')[-1]

def choose_color():
    colors = {"black":(0,0,0), "white":(255,255,255), "green":(0,204,0), "orange":(255,165,0), "pink":(255, 179, 190), "navy":(0, 0, 128), "cyan":(0, 255, 255), "purple":(153, 0, 153), "red":(255, 0, 0), "brown":(122, 31, 31)}
    while True:
        chosen_color = input("What color would you like to use ?\nChoose from: Black, White, Green, Orange, Pink, Navy, Cyan, Purple, Red, Brown: ")
        if chosen_color.lower() in colors:
            return colors[chosen_color.lower()]
        
def do_you_want_to_repeat():
    while True:
        repeat = input("Do you want to watermark another image? Answer Yes or No: ")
        if repeat[0].lower() in ("y","n"):
            break
    return repeat.lower()

if __name__ == "__main__":
    main()