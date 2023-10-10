from rembg import remove
import easygui
from PIL import Image

imputPath = easygui.fileopenbox(
    title="Select a file to remove background", filetypes=["*.jpg", "*.jpeg", "*.png"])
outputPath = easygui.filesavebox(title="Save the file", filetypes=[
                                 "*.png"], default=imputPath[:-4] + "_no_bg.png")

if imputPath is not None:
    print("Removing background...")
    f = open(imputPath, 'rb')
    no_bg = remove(f.read())
    f.close()
    print("Background removed!")
    print("Saving file...")
    with open(outputPath, 'wb') as f:
        f.write(no_bg)
    print("File saved!")
    print("Opening file...")
    Image.open(outputPath).show()
    print("File opened!")

else:
    print("No file selected!")
