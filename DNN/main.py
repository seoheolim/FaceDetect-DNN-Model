# import libraries
import cv2
import face_recognition
import timeit
import os
from model import detectAndSave

def convertVideo(vid_PATH, img_PATH, out_PATH, test_name):

    # Start Time
    start_time = timeit.default_timer()

    # Get a reference to webcam 
    input_movie = cv2.VideoCapture(vid_PATH)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

    if img_PATH: # 아직 recognition을 구현하지 않아 필요없다

        image = face_recognition.load_image_file(img_PATH)
        # If image is empty list it means no face was detected

        face_encoding = face_recognition.face_encodings(image)[0]

        known_faces = [
        face_encoding,
        ]


    # Set Output 
    codec = int(input_movie.get(cv2.CAP_PROP_FOURCC)) 
    fps = int(input_movie.get(cv2.CAP_PROP_FPS)) 
    frame_width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH)) 
    frame_height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

    os.makedirs(out_PATH, exist_ok = True)
    os.makedirs(out_PATH + '/DNN', exist_ok= True)
    output_movie = cv2.VideoWriter(out_PATH + f'/DNN/output_{test_name}.mp4', codec, fps, (frame_width,frame_height))  

    # Initialize variables
    frame_number = 0


    while True:
        # Grab a single frame of video
        ret, frame = input_movie.read() # need opencv version 4.5 or above. or the frame will be flipped upside down 
        frame_number += 1


        # Quit when the input video file ends
        if not ret:
            break
        

        frame = detectAndSave(frame)

        if frame_number % 100 == 0:
            print("Writing frame {} / {}".format(frame_number, length))
    
        output_movie.write(frame)


    # All done!
    input_movie.release()
    output_movie.release()
    cv2.destroyAllWindows()

    stop_time = timeit.default_timer()
    print("The time it took to process : ", stop_time - start_time)