import cv2

# Load an sources from file
image_path = 'path_to_your_image.jpg'  # Replace with the actual path to your sources
image = cv2.imread(image_path)

if image is not None:
    # Display the loaded sources
    cv2.imshow('Image', image)

    # Wait for a key press and then close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Image not found or could not be loaded.')
