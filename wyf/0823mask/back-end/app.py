from flask import Flask, render_template, Response
import cv2
import mask_recognize
from utils import stick

app = Flask(__name__)

# camera = cv2.VideoCapture('rtsp://admin:admin@172.21.182.12:554/cam/realmonitor?channel=1&subtype=1')
# camera = cv2.VideoCapture('test.mp4')
camera = cv2.VideoCapture(0)
dududu = mask_recognize.face_rec()

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            frame = stick.getface(frame)
            dududu.recognize(frame)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_start')
def video_start():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5002)