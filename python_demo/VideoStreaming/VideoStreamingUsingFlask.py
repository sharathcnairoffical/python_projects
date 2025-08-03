from flask import Flask, render_template ,Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

def gen_frames():
    while True:
        #read the camera frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()  # Convert to bytes
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Return the frame in the response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(gen_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)