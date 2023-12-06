import time
import pyautogui
from PIL import Image
from PIL import ImageGrab
from screeninfo import get_monitors
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader
# # Lấy vị trí của con chuột để xác định region cho screenshot
# mouse_position = pyautogui.position()
# # In ra vị trí
# print("Vị trí của con chuột:", mouse_position)
time.sleep(5)
images=[]
for i in range(71):
    im=pyautogui.screenshot(region=(271,-835,580,800))
    im.save(f"images/{i}.png")
    im= Image.open(f'images/{i}.png')
    images.append(im)
    pyautogui.scroll(-1)
images[0].save("OOP using python.pdf", "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])