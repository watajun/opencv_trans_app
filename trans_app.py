import cv2
from PIL import Image 

original_face_img = "images/man.png"
original_mask_img = "images/otahuku.png"


def find_face():
    # 顔検出の分類機を用意
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    img = cv2.imread(original_face_img)
    face_list = cascade.detectMultiScale(img)
    return face_list


def paste_img(face_list):
    x = face_list[0][0]
    y = face_list[0][1]
    w = face_list[0][2]
    h = face_list[0][3]
    # コメントアウトがopencvで実行するコード
    # face_img = cv2.imread(original_face_img)
    # mask_img = cv2.imread(original_mask_img)
    face_img = Image.open(original_face_img)
    mask_img = Image.open(original_mask_img)
    # resize_mask_img = cv2.resize(mask_img, dsize=(w, h))
    resize_mask_img = mask_img.resize((w, h))
    # cv2.imwrite("images/resize_otahuku.png", resize_mask_img)
    resize_mask_img.save("images/resize_otahuku_pillow.png")
    # face_img[y : h + y, x : x + w] = cv2.imread("images/resize_otahuku.png")
    # cv2.imwrite("images/hensin.png", face_img)
    face_img.paste(resize_mask_img, (x, y), resize_mask_img.split()[3])
    face_img.save("images/hensin_pillow.png")


face_list = find_face()
# print(face_list)
paste_img(face_list)
