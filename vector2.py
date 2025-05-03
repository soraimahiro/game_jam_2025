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
	def __truediv__(self, n: int | float):
		return Vector2(self.x / n, self.y / n)
	def __floordiv__(self, n: int):
		return Vector2(self.x // n, self.y // n)
	def __eq__(self, other: 'Vector2'):
		return self.x == other.x and self.y == other.y
	def __neg__(self):
		return Vector2(-self.x, -self.y)
	def __repr__(self):
		return f"Vector2({self.x}, {self.y})"
	def __hash__(self):
		return hash((self.x, self.y))
	def add(self, other: 'Vector2'):
		return self + other
	def sub(self, other: 'Vector2'):
		return self - other
	def scale(self, s: int | float) -> 'Vector2':
		return self * s
	def to_tuple(self):
		return (self.x, self.y)
	def parallel(self, other: 'Vector2'):
		return self.x * other.y == self.y * other.x
	def proj(self, other: 'Vector2') -> 'Vector2':
		"""ask for the projection of `self` on `other`"""
		so: int | float = self * other
		oo: int | float = other * other
		return other * (so / oo)