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
	def get_scale(self, other: 'Vector2'):
		if not self.parallel(other):
			return None
		if other.x != 0:
			return self.x / other.x
		if other.y != 0:
			return self.y / other.y
		return None
	@ classmethod
	def intercept(self, A: 'Vector2', B: 'Vector2', C: 'Vector2', D: 'Vector2') -> bool:
		if A == B:
			return False
		if B == D:
			return True
		AB = B - A
		AC = C - A
		AD = D - A
		d = AC.x * AD.y - AC.y * AD.x
		if d != 0: # A not on CD
			a = (AB.x * AD.y - AB.y * AD.x) / d
			b = (AC.x * AB.y - AC.y * AB.x) / d
			if a > 0 and b > 0:
				return True
			return False
		if not AB.parallel(AC):
			return False
		if AC.x * AD.x < 0:
			return True
		i = AB.get_scale(AC)
		j = AB.get_scale(AD)
		if i == None: # AC == (0, 0)
			if AB * AD > 0:
				return True
			return False
		if j == None: # AD == (0, 0)
			if AB * AC > 0:
				return True
			return False
		if i < 0 and j < 0:
			return False
		if i > 1 or j > 1:
			return True
		return False