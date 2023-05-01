from flask import Flask, render_template, request, url_for,redirect,flash,Response
import cv2

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


camera = cv2.VideoCapture(0)
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
@app.route('/livestream.html')
def livestream():
    return render_template('livestream.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/')
def login():
    return render_template('login.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/check_login.html')
def check_login():
    email = request.args.get('email_add')
    password = request.args.get('pass')
    confirm_pass = request.args.get('confirm_pass')
    if email and password and (password == confirm_pass):  
        flash("You have successfully signed up!!")
        return render_template('login.html')
    else:
        return redirect(url_for('signup'))
    

@app.route('/input.html')
def input():
    email = request.args.get('email_address')
    password = request.args.get('password')
    if email and password: 
        return render_template('input.html')
    else:
        return render_template('login.html')
    
if __name__ == "__main__":
    app.run(debug=True)
