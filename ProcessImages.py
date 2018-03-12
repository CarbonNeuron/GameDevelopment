from PIL import Image
import os, shutil
main_dir = os.path.split(os.path.abspath(__file__))[0]
for i in os.listdir('data'):
    img = Image.open("data\\"+i)
    outname = i[:-4]+".bmp"
    img.save(outname)
    path = os.path.join(main_dir, 'data', outname)
    shutil.move(outname, path)