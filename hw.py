import sys
from PIL import Image, ImageFilter

def resizeImg(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height", img.size)
        newWidth = int(input("new width: "))
        ratio = float(newWidth) / img.size[0]
        newHeight =int(img.size[1] * ratio)
        resizedImg = img.resize( (newWidth, newHeight), Image.BILINEAR )#BICUBIC雙立方體,BILINEAR雙線性內插法(放大)
        print("new image size: ", resizedImg.size)
        doxIndex = imgName.index(".")
        newImgName = imgName[:doxIndex] + "_resized" + imgName[doxIndex:]
        resizedImg.save(newImgName)
        print("Resized img is saved as", newImgName, "\n")
    except FileNotFoundError as fnfe:
            print(fnfe)

def rotateImg(imgName):
    try:
        img = Image.open(imgName)
        print("旋轉選擇: ")
        print("1. 左右旋轉")
        print("2. 上下翻轉")
        print("3. 旋轉 90 度")
        print("4. 旋轉 180 度")
        print("5. 旋轉 270 度")
        print("6. other")
        op1 = input("您要進行的操作: ")
        if op1 == "1":
            newIm = img.transpose(Image.FLIP_LEFT_RIGHT)
            str1 = "_flip_LR"
        elif op1 == "2":
            newIm = img.transpose(Image.FLIP_TOP_BOTTOM)
            str1 = "_flip_TB"
        elif op1 == "3":
            newIm = img.transpose(Image.ROTATE_90)
            str1 = "_rotate_90"
        elif op1 == "4":
            newIm = img.transpose(Image.ROTATE_180)
            str1 = "_rotate_180"
        elif op1 == "5":
            newIm = img.transpose(Image.ROTATE_270)#transpose 不會有黑框
            str1 = "_rotate_270"
        elif op1 == "6":
            rotDegree = float(input("Rotate degree: "))
            newIm = img.rotate(rotDegree) #rotate會有黑框
            str1 = "_rotata_" + str(rotDegree)
        doxIndex = imgName.index(".")
        newImgName = imgName[:doxIndex] + str1 + imgName[doxIndex:]
        newIm.save(newImgName)
        print("Rotate img is saved as", newImgName, "\n")
    except FileNotFoundError as fnfe:
            print(fnfe)

def genThumbnail(imgName):
    try:
        img = Image.open(imgName)
        print("Current size (width, height", img.size)
        newWidth, newHeight = map(int, input("請輸入縮圖尺寸: ").split())
        img.thumbnail((newWidth, newHeight))
        doxIndex = imgName.index(".")
        newImgName = imgName[:doxIndex] + "_thumbnail" + imgName[doxIndex:]
        img.save(newImgName)
        print("Thumbnail img is saved as", newImgName, "\n")
    except FileNotFoundError as fnfe:
            print(fnfe)

def applyFilter(imgName):
    try:
        im = Image.open(imgName)
        print("濾鏡選項: ")
        print("1. 模糊 (BLUR)")
        print("2. 輪廓 (CONTOUR)")
        print("3. 細節增強 (DETAIL)")
        print("4. 邊緣增強 (EDGE_ENHANCE)")
        print("5. 深度邊緣增強 (EDGE_ENHACE_MORE)")
        print("6. 浮雕效果 (EMBOSS)")
        print("7. 邊緣訊息 (FIND_EADGES)")
        print("8. 平滑效果 (SMOOTH)")
        print("9. 深度平滑效果 (SMOOTH_MORE)")
        print("A. 銳利化效果 (SHARPEN)")
        op1 = input("選擇要套用的濾鏡: ")
        if op1 == "1":
            newImg = im.filter(ImageFilter.BLUR)
            str1 = "_BLUR_"
        if op1 == "2":
            newImg = im.filter(ImageFilter.CONTOUR)
            str1 = "_CONTOUR_"
        if op1 == "3":
            newImg = im.filter(ImageFilter.DETAIL)
            str1 = "_DETAIL_"
        if op1 == "4":
            newImg = im.filter(ImageFilter.EDGE_ENHANCE)
            str1 = "_EDGE_ENHANCE_"
        if op1 == "5":
            newImg = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
            str1 = "_EDGE_ENHANCE_MORE_"
        if op1 == "6":
            newImg = im.filter(ImageFilter.EMBOSS)
            str1 = "_EMBOSS_"
        if op1 == "7":
            newImg = im.filter(ImageFilter.FIND_EDGES)
            str1 = "_FIND_EADGES_"
        if op1 == "8":
            newImg = im.filter(ImageFilter.SMOOTH)
            str1 = "_SMOOTH_"
        if op1 == "9":
            newImg = im.filter(ImageFilter.SMOOTH_MORE)
            str1 = "_SMOOTH_MORE_"
        if op1 == "A":
            newImg = im.filter(ImageFilter.SHARPEN)
            str1 = "_SHARPEN_"
        doxIndex = imgName.index(".")
        newImgName = imgName[:doxIndex] + str1 + imgName[doxIndex:]
        newImg.save(newImgName)
        print("Flitered img is saved as", newImgName, "\n")
    except FileNotFoundError as fnfe:
            print(fnfe)

def showMenu():
    print("============")
    print("1:等比例縮放")
    print("2:圖片旋轉")
    print("3:產生縮圖")
    print("4:套用濾鏡")
    print("0:結束")
   
if __name__ == "__main__":
    if len(sys.argv) > 1:
        while True:
            showMenu()
            op = input("選擇功能:")
            if op == "1":
                resizeImg(sys.argv[1])
            elif op == "2":
                rotateImg(sys.argv[1])
            elif op == "3":
                genThumbnail(sys.argv[1])
            elif op == "4":
                applyFilter(sys.argv[1])
            elif op == "0":
                print("THANKS FOR PLAYING!")
                break
    else:
        print("argument error")