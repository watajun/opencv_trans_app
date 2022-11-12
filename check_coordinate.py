import cv2


def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        return x, y


img = cv2.imread("images/man.png")

cv2.imshow("Face", img)
cv2.setMouseCallback("Face", onMouse)

cv2.waitKey(0)
cv2.destroyALLWindows()
