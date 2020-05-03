from copy import deepcopy

def check_matrix(list):
    tmp = len(list[0])
    hight = 0
    for itm in list:
        if len(itm) != tmp:
            print("Была введена не матрица!")
            break
        else:
            hight +=1
    return [tmp, hight]

class Matrix:
    def __init__(self, list):
            self.list = deepcopy(list)
            self.demension = check_matrix(list)


    def __str__(self):
        for itm in self.list:
            for elem in itm:
                print(elem, end=' ')
            print()

    def __add__(self, other):
        if self.demension == other.demension:
                result = []
                for i in range(self.demension[0]):
                    tmp = []
                    for j in range(self.demension[1]):
                        tmp.append(int(self.list[i][j]) + int(other.list[i][j]))
                    result.append(tmp)
                return Matrix(result)
        else:
            print('Размерности матриц неравны, сложение невозможно')



my_list_1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
my_list_2 = Matrix([[9,8,7],[6,5,4],[3,2,1]])
my_list_1.__str__()
new_matrix = my_list_1.__add__(my_list_2)
new_matrix.__str__()

     