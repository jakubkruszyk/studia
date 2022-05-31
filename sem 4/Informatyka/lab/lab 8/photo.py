import os
import cv2
import sewar
from filters import *

REF_DIR = "./faces"

check_path = input("Podaj ścieżkę do pliku/ folderu:\n")
use_own = True if input("Czy użyć własnej metody (trwa długo) (y/n): ") == "y" else False

if os.path.isdir(check_path):
    file_list = [os.path.join(check_path, path) for path in os.listdir(check_path)
                 if os.path.isfile(os.path.join(check_path, path))]
else:
    file_list = [check_path]

for i in file_list:
    rmse_vec = []
    ssim_vec = []
    own_vec = []
    img_to_check = cv2.imread(i)

    for file_name in os.listdir(REF_DIR):
        ref_image_path = os.path.join(REF_DIR, file_name)
        ref_image = cv2.imread(ref_image_path)
        # rmse_vec.append(sewar.full_ref.rmse(img_to_check, ref_image))
        if use_own:
            own_vec.append(own_method(img_to_check, ref_image))
        # ssim_vec.append(sewar.full_ref.ssim(img_to_check, ref_image))

    # print(avg(rmse_vec))
    print(avg(own_vec))
    print()

    # if (avg(rmse_vec)) < 100 and (avg(own_vec) < 80):
    #     print("Na zdjęciu", i, "jest twarz!")
    # else:
    #     print("Na zdjęciu", i, "nie ma twarzy!")
