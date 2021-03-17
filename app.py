import streamlit as st
import os
import cv2 as cv
import pathlib
import random
import time


def get_photo_dir(dir_path):
    image_dir = list()
    images_name = os.listdir(dir_path)
    for i in images_name:
        if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"):
            image_dir.append("".join([dir_path + "\\" + i]))
    return images_name, image_dir


def face_detect(img):
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    return faces


def create_dataset_files(path):
    st.error("Logic under Construction")
    
    
def create_dataset_folder(dir_path):
    if os.path.isdir(dir_path):
        images_name, image_dir = get_photo_dir(dir_path)
        home = pathlib.Path.home()
        for pic, name in zip(image_dir, images_name):
            name = "{}\Downloads\\face_dataset\\face_".format(home)
            img = cv.imread(pic)
            img_gray = cv.imread(pic, 0)  # Gray Scale Images
            faces = face_detect(img_gray)
            # print(len(faces))
            for x, y, w, h in faces:
                # cv.rectangle(img, (x, y), (x + w, y + h), [0, 0, 0], 2)
                crop_img = img[y:y + h, x:x + w]
                location = name + str(random.random()) + '.jpg'
                if 'face_dataset' in os.listdir("{}\Downloads".format(home)):
                    cv.imwrite(location, crop_img)

                else:
                    os.mkdir("{}\Downloads\\face_dataset".format(home))
                    cv.imwrite(location, crop_img)

            # plt.imshow(img, cmap='gray')
            # plt.show()
        with st.spinner('Wait for it...Faces Database is preparing...'):
            time.sleep(5)

        with st.spinner('"Your DataBase is Ready!..."'):
            time.sleep(5)

        with st.spinner("Your Database directory name is face_dataset"):
            time.sleep(5)

        with st.spinner("Please check into your Downloads Folder"):
            time.sleep(5)
            st.success("Done!")
            st.balloons()

    else:
        st.warning("Note:Please give the only folder path")
        

def main():
#     img = cv.imread(r"C:\Users\curaj1\Downloads\ComputerVision\download.jpg")
#     st.image(img)
    check = st.sidebar.radio("Navigation", ["Files", "Folder"])
    if check == 'Files':
        path_ = st.file_uploader("Browser Files", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
#         create_dataset_files(path_)
    else:
        path_ = st.text_input("Browser PATH\n")
#         create_dataset_folder(path_)
        
        
if __name__ == '__main__':
    main()
