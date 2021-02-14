GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
YELLOW = (0, 255, 255)

def gbr_to_rgb(image):
    return image[:, :, ::-1]

def is_rectangle_inside(rectangle_a, rectangle_b):
    return rectangle_a.position > rectangle_b.position and rectangle_a.end_point < rectangle_b.end_point
