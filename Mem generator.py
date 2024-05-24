from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")
top_text = input("Введите верхний текст")
bottom_text = input("Введите нижний текст")

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input("Введите номер картинки"))

if image_number == 1:
    image = 'Кот в ресторане.png'
elif image_number == 2:
    image = 'Кот в очках.png'


image_file = Image.open(image)
width, height = image_file.size
draw = ImageDraw.Draw(image_file)
font = ImageFont .truetype("arial.ttf", size = 70)
text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill ="black" )
text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text, font=font, fill ="black" )
image_file.save("new_mem.jpg")