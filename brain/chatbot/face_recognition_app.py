import cv2
import face_recognition
from speak import speak2
def verify_face(your_image_path):
    # Load your image and encode your face
    your_image = face_recognition.load_image_file(your_image_path)
    your_face_encoding = face_recognition.face_encodings(your_image)[0]

    # Start video capture
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            break

        # Find all face locations in the frame
        face_locations = face_recognition.face_locations(frame)
        if face_locations:
            # Encode faces in the frame
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            # Initialize distance
            distance = None

            for face_encoding in face_encodings:
                distance = face_recognition.face_distance([your_face_encoding], face_encoding)[0]
                top, right, bottom, left = face_locations[0]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                if distance < 0.5:  # Adjust this threshold as needed
                    speak2("Hi Hritik")
                    break

            # If your face is detected and distance is initialized, break out of the main loop
            if distance is not None and distance < 0.5:
                break

        # Display the frame
        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture
    video_capture.release()
    cv2.destroyAllWindows()


verify_face("/home/hritik/transfer/jarvis/brain/features/photos/hritik.jpeg")
