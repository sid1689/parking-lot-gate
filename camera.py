import cv2
from vector import Vector

class Camera:
	camera_exists = False

	def __init__(self):
		assert not Camera.camera_exists
		#'rtsp://admin:admin@192.168.0.90:555/cam/realmonitor?channel=1'
		self._video_capture = cv2.VideoCapture(0)

		shape = self.frame.shape
		self.size = Vector(shape[1], shape[0])

		Camera.camera_exists = True
	
	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		self._video_capture.release()

	@property
	def frame(self):
		(_, frame) = self._video_capture.read()
		return frame

	@property
	def frame_size(self):
		x = self.frame.shape[1]
		y = self.frame.shape[0]
		return (x, y)