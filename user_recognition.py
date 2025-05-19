import face_recognition
import cv2
import os

def recognize_user(known_faces_dir="known_faces"):
    video = cv2.VideoCapture(0)
    known_encodings = []
    names = []

    for filename in os.listdir(known_faces_dir):
        path = os.path.join(known_faces_dir, filename)
        image = face_recognition.load_image_file(path)
        encodings = face_recognition.face_encodings(image)

        if encodings:
            known_encodings.append(encodings[0])
            names.append(os.path.splitext(filename)[0])
        else:
            print(f"❌ No face found in {filename}. Skipping.")

    print("✅ Loaded known faces:", names)

    while True:
        ret, frame = video.read()
        if not ret:
            continue

        # Resize and convert to RGB
        small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

        # Detect face and encode
        face_locations = face_recognition.face_locations(rgb_small)
        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            if True in matches:
                video.release()
                cv2.destroyAllWindows()
                return names[matches.index(True)]

        cv2.imshow("Maya Vision", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()
    return
