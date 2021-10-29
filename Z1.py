import numpy # удобная библиотека для сравнения
import copy  # для копирования


class Matrix:
    def __init__(self, znachenie):#конструктор
        self.matrix = copy.deepcopy(znachenie)

    def __str__(self):# Печать
        strc = ''
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])): 
               strc=strc+" "+ str(self.matrix[i][j])
            strc=strc+"\n"
        return strc

    def __getitem__(self, idx):#доступ по индексу
        return self.matrix[idx]

    def __gt__(self, ar):#>
        return numpy.linalg.det(self.matrix) > numpy.linalg.det(ar.matrix)

    def __lt__(self, ar):#<
        return numpy.linalg.det(self.matrix) < numpy.linalg.det(ar.matrix)

    def __eq__(self, ar):#=
        return numpy.linalg.det(self.matrix) == numpy.linalg.det(ar.matrix)

    def __mul__(self, ar):#*
        res = Matrix([[0,0],[0,0]])
        for i in range(len(self.matrix)):
            for j in range(len(ar.matrix[0])):
                for k in range(len(ar.matrix)):
                    res[i][j] += self[i][k] * ar[k][j]
        return res

    def __add__(self, ar):#+
        res = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                sum = ar[i][j] + self[i][j]
                numbers.append(sum)
                if len(numbers) == len(self.matrix):
                    res.append(numbers)
                    numbers = []
        return Matrix(res)

    

m1 = Matrix([[1,1],[2,2]])
m2 = Matrix([[1,2],[3,4]])
print("Первая матрица \n", m1)
print("Вторая матрица \n", m2)
print("Сумма матриц")
print(m1 + m2)
print("Произведение матриц")
print(m1 * m2)
if m1 > m2:
    print("Первая матрица больше второй")
elif m1 < m2:
    print("Вторая матрица больше первой")
else:
    print("Матрицы равны !")

