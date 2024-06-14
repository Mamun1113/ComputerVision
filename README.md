# Auto Screen Lock - when you are not in front of PC!

Hi! This project access camera of your PC and tries to find your face in the video. If your face is not found between a specific time(You can change the time. Default is 5 seconds) then the PC will go to Screen Saver mode/ Lock mode/ Sleep mode (You can decide. Default is Screen Lock). This Python script uses the OpenCV and face_recognition libraries to capture video from a webcam, detect faces, and compare them to a reference face. If the reference face is not detected for a specified period, the script will lock the screen.

## Demo video link: https://youtu.be/Hosk_vqaszs

## Requirements

- Python 3.x
- OpenCV
- face_recognition
- numpy

## Installation

1. Ensure you have Python 3.x installed.
2. Install the required Python libraries using pip:

    ```sh
    pip install opencv-python face_recognition numpy
    ```

## Usage

1. Save a reference image of the face you want to recognize as `MyFace.jpg` in the `image` directory.
2. Run the script:

    ```sh
    python main.py
    ```

## How It Works

1. The script loads a reference image of the face and encodes it.
2. It opens a connection to the webcam.
3. It continuously captures frames from the webcam and checks for faces.
4. If a face is detected, it compares it to the reference face encoding.
5. If the reference face is recognized, a rectangle is drawn around the face, and the timer is reset.
6. If the reference face is not recognized within the specified wait time (default is 5 seconds), the screen is locked.
7. The user can quit the program by pressing the 'q' key.

## Customization

- **max_wait**: The maximum time to wait before locking the screen if the reference face is not recognized. Default is 5 seconds.

    ```python
    max_wait = 5.0  # Change the value as needed
    ```

- **Webcam Index**: By default, the script uses the first webcam (index 0). If you have multiple webcams, you can change the index.

    ```python
    cap = cv2.VideoCapture(0)  # Change the index if needed
    ```

## Functions

- `screen_lock()`: Locks the workstation.
- `screen_sleep()`: Puts the screen to sleep mode.
- `screen_saver()`: Activates the screen saver if it is enabled.

## Notes

- Ensure your reference image is clear and well-lit for better recognition accuracy.
- The script is designed for Windows, using `ctypes` to access system functions for locking the screen.

## What's next!!!

A windows app will be uploaded very soon with easy GUI.

