#!/usr/bin/env python3
import rospy
from  cv_bridge import CvBridge 
import cv2
from sensor_msgs.msg import Image
#from std_msgs.msg import Image

def Image_callback(msg):
	bridge = CvBridge()
	#dtype, n_channels = bridge.encoding_as_cvtype2('8UC3')
	cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
	hold=cv_image
	gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)

	_, tresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
	contours, _ = cv2.findContours(tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
	#Выбрать цвета объектов
	colors=[]
	for i in range(len(contours)):
		colors.append(hold[contours[i][0][0][1]][[contours[i][0][0][0]]])

	#Определение координат для текста
	coords=[]
	for i in range(len(contours)):
		coords.append([(contours[i][0][0][1]),(contours[i][0][0][0])-20])

	#Определение цветов
	for i in range(len(colors)):
		if(colors[i][0][0]<90 and colors[i][0][1]<130 and colors[i][0][2]>145):
			str="Orange"
		elif(colors[i][0][0]<130 and colors[i][0][1]<130 and colors[i][0][2]>130):
			str="Red"
		elif(colors[i][0][0]>130 and colors[i][0][1]<130 and colors[i][0][2]<130):
			str="Blue"
		elif(colors[i][0][0]<130 and colors[i][0][1]>130 and colors[i][0][2]<130):
			str="Green"
		elif(colors[i][0][2]>colors[i][0][0] and colors[i][0][1]>colors[i][0][0]):
			str="Yellow"
		
        


        	#Рисование контуров и текста
		cv2.putText(hold,str,(coords[i][1]-30,coords[i][0]-30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2,cv2.LINE_AA)

	cv2.drawContours(hold, contours, -1, (255, 0, 255), 5)
	
	cv2.rectangle(hold, (0, 0), (640, 480), (100, 120, 150), 10)
	cv2.imshow('okno', hold)
	if cv2.waitKey(1) & 0xFF == ord('q'):
        	return
	rospy.loginfo("I saw %s", str)
	rospy.loginfo(colors)
	pub=rospy.Publisher('countour_color', String, queue_size=10)
	pub.publish(str)
	
	
rospy.init_node('camera_viewer')
rospy.Subscriber('/usb_cam/image_raw', Image, Image_callback, queue_size=100)
try:
	rospy.spin()
except KeyboardInterrupt:
	print("Shutting down")
	cv2.destroyAllWindows()
