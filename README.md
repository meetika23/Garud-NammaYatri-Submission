# GARUD
![](https://github.com/meetika23/Garud/blob/main/garud/images/banner.jpg)

According to a study, 90% of accidents involving pedestrians in Bengaluru occurred when they were trying to cross the road and because of the lack of footpaths for people to walk on, forcing them to traverse along the road instead.So, here comes GARUD to rescue.This is a flask web application which is integerated with YOLOv3 model to detect the vehicles parked on the footpaths.

 
## How does  GARUD works?

### index.html
![](https://github.com/meetika23/Garud/blob/main/garud/index.html)
In this page, you are provided with the need of this web application and features like login and signup.

###signup.html
![](https://github.com/meetika23/Garud/blob/main/templates/signup.html)
For the users who are new to this web application can create their account using this page and continue using this web application.

###login.html
![](https://github.com/meetika23/Garud/blob/main/templates/login.html)
Login page will provide data security so that only the authorized person (like traffic police) can access the live streaming of security cameras.

###input.html
![](https://github.com/meetika23/Garud/blob/main/templates/input.html)
GARUD app provides the feature to link any IP cameras to this application by taking the IP address of the camera as input.

###livestream.html
![](https://github.com/meetika23/Garud/blob/main/templates/livestream.html)
The live streaming of any camera linked  to GARUD will be shown in this page and the detection of the vehicles parked on the footpaths will be detected using YOLOv3 model.

To link IP cameras to this web application,
  
>camera = cv2.VideoCapture(0)
>for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
>for local webcam use cv2.VideoCapture(0)
