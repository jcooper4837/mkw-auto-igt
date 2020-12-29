#mkw-auto-igt
#reads the time on the game screen and parses it into digits

import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import cv2

hwnd = win32gui.FindWindow(None, 'CaptureModule')

left, top, right, bot = win32gui.GetWindowRect(hwnd)
w = right - left
h = bot - top

hwndDC = win32gui.GetWindowDC(hwnd)
mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
saveDC = mfcDC.CreateCompatibleDC()

saveBitMap = win32ui.CreateBitmap()
saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

saveDC.SelectObject(saveBitMap)

result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)
print(result)

bmpinfo = saveBitMap.GetInfo()
bmpstr = saveBitMap.GetBitmapBits(True)

im = Image.frombuffer(
    'RGB',
    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    bmpstr, 'raw', 'BGRX', 0, 1)

width, height = im.size 

left = 1250
top = 100
right = 1800
bottom = 200

imf = im.crop((left, top, right, bottom))
im0 = im.crop((1724, 119, 1768, 173))
im1 = im.crop((1680, 119, 1724, 173))
im2 = im.crop((1638, 119, 1682, 173))
im3 = im.crop((1574, 119, 1618, 173))
im4 = im.crop((1530, 119, 1574, 173))
im5 = im.crop((1465, 119, 1509, 173))
im6 = im.crop((1421, 119, 1465, 173))

win32gui.DeleteObject(saveBitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hwnd, hwndDC)

if result == 1:
    imf.save("test.png")
    im0.save("A.png")
    im1.save("B.png")
    im2.save("C.png")
    im3.save("D.png")
    im4.save("E.png")
    im5.save("F.png")
    im6.save("G.png")

cases = list((list((0, 0, 0, 1, 0, 0, 0)),
           list((0, 0, 1, 1, 1, 1, 1)),
           list((1, 0, 0, 0, 0, 0, 1)),
           list((0, 0, 0, 0, 0, 1, 1)),
           list((0, 0, 1, 0, 1, 1, 0)),
           list((0, 1, 0, 0, 0, 1, 0)),
           list((0, 1, 0, 0, 0, 0, 0)),
           list((0, 0, 1, 1, 0, 1, 0)),
           list((0, 0, 0, 0, 0, 0, 0)),
           list((0, 0, 0, 0, 0, 1, 0))))

img0 = cv2.imread("0.png")
img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")
img3 = cv2.imread("3.png")
img4 = cv2.imread("4.png")
img5 = cv2.imread("5.png")
img6 = cv2.imread("6.png")
img7 = cv2.imread("7.png")
img8 = cv2.imread("8.png")
img9 = cv2.imread("9.png")

img0g = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
img1g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img3g = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
img4g = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
img5g = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
img6g = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
img7g = cv2.cvtColor(img7, cv2.COLOR_BGR2GRAY)
img8g = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY)
img9g = cv2.cvtColor(img9, cv2.COLOR_BGR2GRAY)

ret,img0t = cv2.threshold(img0g,60,255,cv2.THRESH_BINARY)
ret,img1t = cv2.threshold(img1g,60,255,cv2.THRESH_BINARY)
ret,img2t = cv2.threshold(img2g,60,255,cv2.THRESH_BINARY)
ret,img3t = cv2.threshold(img3g,60,255,cv2.THRESH_BINARY)
ret,img4t = cv2.threshold(img4g,60,255,cv2.THRESH_BINARY)
ret,img5t = cv2.threshold(img5g,60,255,cv2.THRESH_BINARY)
ret,img6t = cv2.threshold(img6g,60,255,cv2.THRESH_BINARY)
ret,img7t = cv2.threshold(img7g,60,255,cv2.THRESH_BINARY)
ret,img8t = cv2.threshold(img8g,60,255,cv2.THRESH_BINARY)
ret,img9t = cv2.threshold(img9g,60,255,cv2.THRESH_BINARY)

img0h = cv2.calcHist([img0t], [0], None, [256], [0, 256])
img1h = cv2.calcHist([img1t], [0], None, [256], [0, 256])
img2h = cv2.calcHist([img2t], [0], None, [256], [0, 256])
img3h = cv2.calcHist([img3t], [0], None, [256], [0, 256])
img4h = cv2.calcHist([img4t], [0], None, [256], [0, 256])
img5h = cv2.calcHist([img5t], [0], None, [256], [0, 256])
img6h = cv2.calcHist([img6t], [0], None, [256], [0, 256])
img7h = cv2.calcHist([img7t], [0], None, [256], [0, 256])
img8h = cv2.calcHist([img8t], [0], None, [256], [0, 256])
img9h = cv2.calcHist([img9t], [0], None, [256], [0, 256])

image = tuple((img0, img1, img2, img3, img4, img5, img6, img7, img8, img9))
gray = tuple((img0g, img1g, img2g, img3g, img4g, img5g, img6g, img7g, img8g, img9g))
thresh = tuple((img0t, img1t, img2t, img3t, img4t, img5t, img6t, img7t, img8t, img9t))
hist = tuple((img0h, img1h, img2h, img3h, img4h, img5h, img6h, img7h, img8h, img9h))

imgA = cv2.imread("A.png")
imgB = cv2.imread("B.png")
imgC = cv2.imread("C.png")
imgD = cv2.imread("D.png")
imgE = cv2.imread("E.png")
imgF = cv2.imread("F.png")
imgG = cv2.imread("G.png")

imgAg = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
imgBg = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)
imgCg = cv2.cvtColor(imgC, cv2.COLOR_BGR2GRAY)
imgDg = cv2.cvtColor(imgD, cv2.COLOR_BGR2GRAY)
imgEg = cv2.cvtColor(imgE, cv2.COLOR_BGR2GRAY)
imgFg = cv2.cvtColor(imgF, cv2.COLOR_BGR2GRAY)
imgGg = cv2.cvtColor(imgG, cv2.COLOR_BGR2GRAY)

def parseInt(imgXg):
    x, y = 0, 0
    direc = 0
    p = list((0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    tf = list((0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    go = True
    it = 0
    while go:
        seek = list((True, True, True, True, True, True, True, True, True, True))
        if it == 0:
            x, y = 28, 29
            direc = 0
        elif it == 1:
            x, y = 11, 29
            direc = 0
        elif it == 2:
            x, y = 40, 14
            direc = 1
        elif it == 3:
            x, y = 24, 14
            direc = 1
        elif it == 4:
            x, y = 8, 14
            direc = 1
        elif it == 5:
            x, y = 28, 9
            direc = 0
        elif it == 6:
            x, y = 11, 9
            direc = 0
        for i in range(10):
            p[0] = img0g[x, y]
            p[1] = img1g[x, y]
            p[2] = img2g[x, y]
            p[3] = img3g[x, y]
            p[4] = img4g[x, y]
            p[5] = img5g[x, y]
            p[6] = img6g[x, y]
            p[7] = img7g[x, y]
            p[8] = img8g[x, y]
            p[9] = img9g[x, y]
            pX = imgXg[x, y]
            if direc == 0:
                x = x + 1
            elif direc == 1:
                y = y + 1
            for j in range(10):
                if abs(int(p[j]) - int(pX)) > 20 and seek[j] == True:
                    tf[j] = tf[j] + 1
                    seek[j] = False
        it += 1
        if it > 6:
            go = False

    smallest = list((7, -1))
    for i in range(10):
        if tf[i] < smallest[0]:
            smallest[0] = tf[i]
            smallest[1] = i
    return smallest[1]

i0 = parseInt(imgAg)
i1 = parseInt(imgBg)
i2 = parseInt(imgCg)
i3 = parseInt(imgDg)
i4 = parseInt(imgEg)
i5 = parseInt(imgFg)
i6 = parseInt(imgGg)

print(str(i6)+str(i5)+":"+str(i4)+str(i3)+"."+str(i2)+str(i1)+str(i0))

