import cv2
'used for image processing'

import mediapipe
'media pipe is used for the detect the face and eventually it detects the eyes too like winking and movement of eyes'

cam = cv2.VideoCapture(0)
'image processing and read the camera through CV2 package'
face_mesh = mediapipe.solutions.face_mesh.FaceMesh()
while True:
    '''in this project the video is running every frame after 
            frame so here we use the while loop and this loop is running forever '''
    frame, frame = cam.read()
    '''to read the camera and get the frame of every video
    cam.read()  It will call the camera to CV2 to read the camera whatever is running from the camera'''
    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    '''to detect the face and whenever you detecting the face
    'the face in greyscale or in an any colour'''
    output = face_mesh.process(rgb_frame)
    hotspot_points = output.multi_face_landmarks
    '''it will detect the hotspot points on your
    face and after recognizing it using that points whether it the the actual face or not'''
    print(hotspot_points)
    cv2.imshow('Cursor Movement Using Eyes', frame)
    'imshow: to show some image into the camera '
    cv2.waitKey(1)
    'wait key for 1 second'
