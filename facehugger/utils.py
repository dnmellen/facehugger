def scale_bounding_box(box, percent=0):
	"""
	Scales up a bounding box in X percent

	:param box: Bounding box
	:type box: list
	:param percent: Percent to scale up
	:type percent: int
	"""

	x, y, w, h = box
	if percent:
		offset_x = 0.01 * percent * w
		offset_y = 0.01 * percent * h
		return [(x - offset_x, y - offset_y), (x + w + offset_x, y + h + offset_y)]
	else:  # pragma: no cover
		return box
