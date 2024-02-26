import cv2 as cv

vid = cv.VideoCapture('kitten.mp4')   # Cars%04d = Cars0001,Cars0002  || Race%02d = Race01,Race02

if (vid.isOpened() == False):
    print("Error Loading Video")

else:
    fps = vid.get(5)
    print('Frame Per Second : ', fps,'FPS')
    frame_c = vid.get(7)
    print('Frame Count: ', frame_c)

while(vid.isOpened()):

    ret, frame = vid.read()
    if ret == True:
        cv.imshow('Frame',frame)
        key = cv.waitKey(20)

        if key == ord('q'):
            break
    else:
        break

vid.release()
cv.destroyAllWindows()