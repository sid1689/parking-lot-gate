from datetime import datetime

import cv2

from camera import Camera
from face_detection import detect_faces
from image_window import display_image, read_key
from periodic_timer import PeriodicTimer
from rectangle import Rectangle
from utils import BLUE, GREEN, RED, YELLOW
from vector import Vector

NO_FACE = Rectangle((-1, -1), (0, 0), (0, 0, 0))
can_dectect = False

def enable_detection():
	global can_dectect
	can_dectect = True

detection_timer = PeriodicTimer(1, enable_detection)
target = Rectangle((0, 0), (300, 300), BLUE)
face_rectangle = NO_FACE
face_counter = 0
gate_is_closed = True

with Camera() as camera:
	detection_timer.start()
	target.center_point = camera.size // 2

	while True:
		frame = camera.frame

		if can_dectect:
			faces = detect_faces(frame)
			can_dectect = False

			if faces:
				face_rectangle = faces[0]

				if face_rectangle.position > target.position and face_rectangle.end_point < target.end_point:
					face_counter += 1
					face_rectangle.color = GREEN

					if face_counter == 3 and gate_is_closed:
						face = frame[face_rectangle.position.x : face_rectangle.position.x + face_rectangle.size.x, face_rectangle.position.y : face_rectangle.position.y + face_rectangle.size.y]
						now = datetime.now()
						date_time = now.strftime("%d-%m-%Y_%H-%M-%S")
						cv2.imwrite("faces/" + str(date_time) +".png", face)
						print("Cancela aberta")
						gate_is_closed = False
				else:
					face_rectangle.color = RED
					face_counter = 0
			else:
				face_rectangle = NO_FACE
				face_counter = 0

		face_rectangle.draw(frame)
		target.color = BLUE if gate_is_closed else YELLOW
		target.draw(frame)

		display_image(frame)

		key = read_key()

		if key == ord('q'):
			break
		
		if key == ord('c'):
			if not gate_is_closed:
				print("cancela fechada")
			gate_is_closed = True

cv2.destroyAllWindows()
detection_timer.stop()