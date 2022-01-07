import cv2

img = cv2.imread('aero1.jpg', 1)


def click_mouse(event, x_coordinate, y_coordinate, flags, params):
    font = cv2.FONT_HERSHEY_DUPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(img, str(x_coordinate) + ',' + str(y_coordinate), (x_coordinate, y_coordinate), font, 1,
                    (0, 0, 255),
                    3)
        cv2.imshow('Image', img)


cv2.imshow('Image', img) # update the window instead of creating a different window
cv2.setMouseCallback('Image', click_mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
