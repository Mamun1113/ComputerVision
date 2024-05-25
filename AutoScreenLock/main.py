import cv2
import face_recognition
import numpy as np
import ctypes
import time

# Variables
max_wait = 5.0
time_waited = 0.0

# Load the reference image and encode the face
my_face_image = face_recognition.load_image_file("image\MyFace.jpg")
my_face_encoding = face_recognition.face_encodings(my_face_image)[0]

# Open a connection to the webcam
# for single camera index is 0. for multiple camera index may vary
cap = cv2.VideoCapture(0)

# Function to put the screen to lock mode
def screen_lock():
    ctypes.windll.user32.LockWorkStation()

# Function to put the screen to sleep mode
def screen_sleep():
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)

# Function to put the screen to screen saver mode
def screen_saver():
    WM_SYSCOMMAND = 0x0112
    SC_SCREENSAVE = 0xF140
    SPI_GETSCREENSAVEACTIVE = 0x0010

    # Call SystemParametersInfoW to check if screen saver is active
    screen_saver_active = ctypes.c_int()
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETSCREENSAVEACTIVE, 0, ctypes.byref(screen_saver_active), 0)

    # Check the value of screen_saver_active
    if screen_saver_active.value == 1:
        ctypes.windll.user32.SendMessageA(ctypes.windll.user32.GetDesktopWindow(), WM_SYSCOMMAND, SC_SCREENSAVE, 0)
    else:
        print("Screen saver is not active")

while True:
    # Wait 1 second
    time.sleep(1)
    time_waited += 1.0

    print("Waited: ", time_waited, " sec")

    # Capture frame-by-frame
    ret, frame = cap.read()

    # No video
    if not ret:
        break

    # Convert the frame to RGB (face_recognition uses RGB instead of BGR)
    rgb_frame = frame[:, :, ::-1]
    rgb_frame = np.array(rgb_frame)

    # Find all the faces and face encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the face with the reference encoding
        matches = face_recognition.compare_faces([my_face_encoding], face_encoding)

        if matches[0]:
            # Draw a rectangle around the matched face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, "Matched", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            time_waited = 0.0

    if(time_waited >= max_wait):
        time_waited = 0.0
        # Change mode
        screen_saver()

    # Display the resulting frame
    cv2.imshow('Webcam Video', frame)

    # Break the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy all windows
cap.release()
cv2.destroyAllWindows()