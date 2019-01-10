#matrix test
#basic matrix calss
class Matrix(object):
    #rows
    #nOfRows
    #nOfCols
    def __init__(self, rows_number, cols_number):
        if rows_number is None or cols_number is None:
            return -1
        self.nOfRows = rows_number
        self.nOfCols = cols_number
        self.rows = [None] * self.nOfRows
         
    def print_matrix(self):
        if not self.rows :
            print("Error - matrix rows is empty!")
            return -1
        print("\n-----Begin Matrix---------------")
        for cur_row in self.rows:
            print(' '.join(cur_row))
        print("-------End Matrix---------------\n")
        return 0
            
    def insert_row(self, row_index, row_array):
        if row_index < 0 or row_index >= self.nOfRows:
            print("No row in matrix with index: " + str(row_index))
            return -1
        if not row_array or len(row_array) < self.nOfCols:
            print("Array of numbers is empty or too short")
            return -1
        if len(row_array) > self.nOfCols:
            print("WARN: Row array is bigger than number of matrix columns \
- will be added only " + str(self.nOfCols) + " elements!")
        self.rows[row_index] = row_array[0:self.nOfCols] #Отсекаем, если ввели массив большей длины
        return 0

#Main Code

rows_number = int(input("Введите количество строк матрицы: "))
cols_number = int(input("Введите количество столбцов матрицы: "))
if rows_number > 0 and cols_number > 0:
    matrix = Matrix(rows_number, cols_number)
    error = False
    for i in range(0, rows_number):        
        row_string = ""
        while not row_string:
            count = i + 1
            row_string = input("Введите " + str(cols_number) +" элементов строки \
" + str(count) + " разделённых одним пробелом")
        result = matrix.insert_row(i, row_string.split(" "))
        #print(result)
        if result != 0:
            error = True
            break
    if not error:
        matrix.print_matrix()
else:
    print("Количество строк и количество столбцов матрицы длолжны быть положительынми числами!")

input("\n\nНажмите Enter для выхода")
        
        
        
        
        

