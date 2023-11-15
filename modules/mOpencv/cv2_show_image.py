import cv2

img = cv2.imread("/home/hieujr/data/python/image-processing/images/My_dog.jpg")

while True:
    cv2.imshow("Puppy", img)

    # If we've waited at least 1 ms And we've pressed the Esc
    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()
