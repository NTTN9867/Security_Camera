# Importing the opencv module
import cv2

# Here we are readong the image
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Frame 1
ret, f1 = cap.read()
# Frame 2
ret, f2 = cap.read()
print(f1.shape)

# While loop
while cap.isOpened():
    # This variable is the difference of frame 1 & 2
    diff = cv2.absdiff(f1, f2)
    # Grayscale the difference
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Blur the grayscale
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    # Threshold the image
    _, thresh = cv2.threshold(blur, 21, 255, cv2.THRESH_BINARY)
    # Dilate the image
    dilated = cv2.dilate(thresh, None, iterations=3)
    # Search for the contors
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # We're going to loop through the contors and place a rectangle over the contors
    for contour in contours:
        # Placing a box around the found contors
        (x, y, w, h) = cv2.boundingRect(contour)
        # If the area is not less than 880 then a rectangle will be drawn
        if cv2.contourArea(contour) < 880:
            continue
        # Drawing the rectangle
        cv2.rectangle(f1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Showing the message on screen
        cv2.putText(f1, "ALERT: MOVEMENT", (70, 40), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

    # Show the window on the screen
    cv2.imshow("Security Footage", f1)
    f1 = f2
    ret, f2 = cap.read()
    # This if statement keeps the window on the screen and if we press e, then the window will close
    if cv2.waitKey(33) == ord("e"):
        break

cv2.destroyAllWindows()