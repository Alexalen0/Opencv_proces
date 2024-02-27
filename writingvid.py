import cv2 as cv

vid = cv.VideoCapture('kitten.mp4')

if (vid.isOpened() == False):
    print("Error Loading Video")

else:
    fps = vid.get(5)
    print('Frame Per Second : ', fps, 'FPS')
    frame_c = vid.get(7)
    print('Frame Count: ', frame_c)

# AVI: cv2.VideoWriter_fourcc('M','J','P','G')
# MP4: cv2.VideoWriter_fourcc(*'XVID')

frame_width = int(vid.get(3))
frame_height = int(vid.get(4))
frame_size = (frame_width, frame_height)
fps = 20
output = cv.VideoWriter('outpur_2.mp4', cv.VideoWriter_fourcc(*'XVID'), 20, frame_size)

while (vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:
        output.write(frame)
    else:
        print('Stream disconnected')
        break

vid.release()
cv.destroyAllWindows()