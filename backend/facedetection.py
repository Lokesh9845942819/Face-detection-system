import cv2

def start_detection():

    face_cascade = cv2.CascadeClassifier(
        "../models/haarcascade_frontalface_default.xml"
    )

    cam = cv2.VideoCapture(0)

    while True:
        ret, frame = cam.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
        cv2.namedWindow("Face Detection System", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Face Detection System", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow("Face Detection System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_detection()