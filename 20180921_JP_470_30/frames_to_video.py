import cv2
import os

image_folder = '20180921_JP_470_30_circles'
video_name = '20180921_JP_470_30.mp4'
frame_rate = 31

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

#for sorting the file names properly
images.sort(key = lambda x: int(x[5:-4]))

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'FMP4'), frame_rate, (width,height))


for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

print("done")
    

