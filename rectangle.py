import cv2
from vector import Vector

class Rectangle:
	def __init__(self, position, size, color):
		self.position = Vector(*position)
		self.size = Vector(*size)
		self.color = color
		
	@property
	def end_point(self):
		return self.position + self.size
	
	def draw(self, image):
		cv2.rectangle(image, (self.position.x, self.position.y), (self.end_point.x, self.end_point.y), self.color, 1)

	@property
	def center_point(self):
		return self.position + self.size // 2
	
	@center_point.setter
	def center_point(self, value):
		self.position = value - self.size // 2