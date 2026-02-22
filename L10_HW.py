import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:,:,1] = 0
        filtered_image[:,:,0] = 0
    elif filter_type == "blue_tint":
        filtered_image[:,:,1] = 0
        filtered_image[:,:,2] = 0
    elif filter_type == "green_tint":
        filtered_image[:,:,0] = 0
        filtered_image[:,:,2] = 0
    elif filter_type == "increase_red":
        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,0], 50)
    elif filter_type == "random1":
        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,0], 90000)
    elif filter_type == "random2":
        filtered_image[:,:,0] = cv2.subtract(filtered_image[:,:,0], -200000)
    return filtered_image

image_path = 'mysterious2.jpg'
image = cv2.imread(image_path)

if image is None:
    print("404 ERROR! IMAGE NOT FOUND!")
else:
    filter_type = "original"
    
    print("Press the following keys to apply the filters:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - increase Red intensity")
    print("d - decrease Blue Intensity")
    print("x - random1")
    print("y - random2")
    print("q - Quit")

    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"
        elif key == ord('b'):
            filter_type = "blue_tint"
        elif key == ord('g'):
            filter_type = "green_tint"
        elif key == ord('i'):
            filter_type = "increase_red"
        elif key == ord('d'):
            filter_type = "decrease_blue"
        elif key == ord('x'):
            filter_type = "random1"
        elif key == ord('y'):
            filter_type = "random2"
        elif key == ord('q'):
            print("EXITING...")
            filename = ("filtered_image.jpg")
            cv2.imwrite(filename, filtered_image )
            break
        else:
            print("INVALID INPUT! PLEASE SELECT 'r', 'b', 'g', 'i','d', or 'q'")
cv2.destroyAllWindows()