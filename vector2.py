from typing import Union

class Vector2:
	def __init__(self, x: int | float, y: int | float):
		self.x = x
		self.y = y
		pass
	def __add__(self, other: 'Vector2'):
		return Vector2(self.x + other.x, self.y + other.y)
	def __sub__(self, other: 'Vector2'):
		return Vector2(self.x - other.x, self.y - other.y)
	def __mul__(self, other: Union[int, float, 'Vector2']):
		"""- int or float: Scaling the vector
			- Vector2: Dot product"""
		if isinstance(other, (int, float)):
			return Vector2(self.x * other, self.y * other)
		if isinstance(other, Vector2):
			return self.x * other.x + self.y * other.y
	def __truediv__(self, s: int | float):
		return Vector2(self.x / s, self.y / s)
	def __floordiv__(self, s: int):
		return Vector2(self.x // s, self.y // s)
	def __eq__(self, other: 'Vector2'):
		return self.x == other.x and self.y == other.y
	def __repr__(self):
		return f"Vector2({self.x}, {self.y})"
	def add(self, other: 'Vector2'):
		return self + other
	def sub(self, other: 'Vector2'):
		return self - other
	def scale(self, s: int | float):
		return self * s
	def to_tuple(self):
		return (self.x, self.y)
	def parallel(self, other: 'Vector2'):
		return self.x * other.y == self.y * other.x
	def proj(self, other: 'Vector2'):
		"""ask for the projection of `self` on `other`"""
		return other * (self * other / other * other)