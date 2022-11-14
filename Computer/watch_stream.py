# open live usb camera in raspberry pi
# import the opencv library
import cv2


# define a video capture object from a url http://10.126.164.183:8554/

server = "http://10.126.164.183:8554/"
vid = cv2.VideoCapture(server)

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame = vid.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

