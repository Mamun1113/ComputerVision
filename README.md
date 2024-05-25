# Auto Screen Lock - when you are not in front of PC!

Hi! This project access camera of your PC and tries to find your face in the video. If your face is not found between a specific time(You can change the time. Default is 5 seconds) then the PC will go to Screen Saver mode/ Lock mode/ Sleep mode (You can decide. Default is Screen Lock).


# Files

**main<area>.py** is the code file of this project.

**image/MyFace.jpg** is your image of face.

## Demo video link: https://youtu.be/Hosk_vqaszs

## How to use

1. Download **AutoScreenLock** project folder
2. Replace **MyFace.jpg** with one of your face image
3. **Optional:** Change **max_wait** variable value to specify how much second to wait before action is taken. Default is set to 5.0 seconds.
4. **Optional:** Change line no 79 to specify what action will be taken between **screen_saver()** / **screen_lock()** / **screen_sleep()** mode. Default is Screen Lock.
5. Run **main<area>.py** file.


## What's next!!!

A windows app will be uploaded very soon with easy GUI.
