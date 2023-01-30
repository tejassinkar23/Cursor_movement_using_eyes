import cv2
'used for image processing'

import mediapipe
'media pipe is used for the detect the face and eventually it detects the eyes too like winking and movement of eyes'

cam = cv2.VideoCapture(0)
'image processing and read the camera through CV2 package'
face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
'to get much refine landmarks'
'''this refine_landmarks parameter have total 478 landmarks on the face and 
every landmark identifies different part of the face'''
while True:
    '''in this project the video is running every frame after 
            frame so here we use the while loop and this loop is running forever '''
    frame
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
    'wait key for 1 second', frame = cam.read()
    '''to read the camera and get the frame of every video
    cam.read()  It will call the camera to CV2 to read the camera whatever is running from the camera'''
    frame =  cv2.flip(frame,1)
    'this means you are flipping vertically '
    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    '''to detect the face and whenever you detecting the face
    'the face in greyscale or in an any colour'''
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    '''it will detect the hotspot points on your
    face and after recognizing it using that points whether it the the actual face or not.
    many.face = we will detecting for many faces '''
    if landmark_points:
        landmarks = landmark_points[0].landmark
        frame_height , frame_width, _= frame.shape
        for  landmark in landmarks[474:478]:
            'loop for every hotspot on the face and draw the loop between them'
            '470:478 this range of index is for detect the iris'
            x = int(landmark.x * frame_width)
            'there are three coordinates x-asis for width , y-axis for height and z for distance between camera and the person '
            y = int(landmark.y * frame_height)
            cv2.circle(frame ,(x,y), 3 ,(0,255,0))
            'Frame for where to draw the circle '
            '(x,y) is a centre'
            '3 is for radius of a circle'
            '0 is Red,255 for green,0 is blue'
            print(x , y)
            'it will show some fraction numbers and that numbers shows the position on the screen'
    cv2.imshow('Cursor Movement Using Eyes', frame)
    'imshow: to show some image into the camera '
    cv2.waitKey(1)
    'wait key for 1 second'
