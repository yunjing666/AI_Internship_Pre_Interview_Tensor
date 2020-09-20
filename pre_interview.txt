Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Tensor:
	_data = []
	_shape = []
	_tensor = []
	def __init__(self, data, shape):
		self._data = data
		self._shape = shape
	def shape_tensor(self):
		size = 1
		for i in self._shape:
			size *= i
		while len(self._data) < size:
			self._data.append(0)
		while len(self._data) > size:
			self._data.pop()
		self._tensor = self._data
		for i in reversed(self._shape):
			self._tensor = [self._tensor[j:j+i] for j in range(0, len(self._tensor), i)]
		return self._tensor[0]

	
>>> #For example
>>> data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
>>> shape0 = [2, 3, 2]
>>> tensor0 = Tensor(data0, shape0)
>>> print(tensor0.shape_tensor())
[[[0, 1], [2, 3], [4, 5]], [[0.1, 0.2], [-3, 0], [0, 0]]]
>>> 
>>> data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
>>> shape1 = [5, 2]
>>> tensor1 = Tensor(data1, shape1)
>>> print(tensor1.shape_tensor())
[[0, 1], [2, 3], [4, 5], [0.1, 0.2], [-3, -2]]
>>> 