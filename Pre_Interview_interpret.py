class Tensor:
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
        print('size: ', size)
        self._tensor = self._data
        for i in reversed(self._shape):
            print('calculate dimension: ', i)
            print('before: ', self._tensor)
            self._tensor = [self._tensor[j: j + i] for j in range(0, len(self._tensor), i)]
            print('after: ', self._tensor)
        return self._tensor[0]


if __name__ == '__main__':
    data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
    shape0 = [2, 3, 2]
    tensor0 = Tensor(data0, shape0)
    print(tensor0.shape_tensor())

    data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 3, 1]
    shape1 = [5, 2]
    tensor1 = Tensor(data1, shape1)
    print(tensor1.shape_tensor())