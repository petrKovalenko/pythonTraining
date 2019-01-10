#matrix test
#basic matrix calss
class Matrix(object):
    rows
    nOfRows
    nOfCols
    def _init_(self, rows_number, cols_number):
        if rows_number is None or cols_number is None:
            return -1
        self.nOfRows = rows_number
        self.nOfCols = cols_number
        row = [None] * self.nOfRows
         
    def print_matrix():
        if not rows :
            print "Error - matrix rows is empty!"
            return -1
        for cur_row in self.rows:
            print(' '.join(cur_row))
        return 0
            
    def insert_row(row_index, row_array):
        if not row_index or row_index >= nOfRows:
            print("No row in matrix with index: " + row_index)
            return -1
        if not row_array or len(row_array) < nOfCols:
            print("Array of numbers is empty or too short")
            return -1
        if len(row_array) > nOfCols:
            print("WARN: Row array is bigger than number of matrix columns - will be added only " + nOfCols + " elements!")
        rows[row_index] = row_array[0:nOfCols] #Отсекаем, если ввели массив большей длины
        return 0

#Main Code

rows_number = int(input("Введите количество строк матрицы: "))
cols_number = int(input("Введите количество столбцов матрицы: "))
if rows_number > 0 and cols_number > 0:
    matrix = Matrix(rows_number, cols_number)
    for i in range(1, rows_number):
        row_string = ""
        while not row_string:
            row_string = input("Введите " + cols_number + " элементов строки " + i + " разделённых одним пробелом")
        result = matrix.insert_row(i - 1, row_string.split(" "))
        if result != 0
            break
    matrix.print_matrix()
else:
    print("Количество строк и количество столбцов матрицы длолжны быть положительынми числами!")

input("\n\nНажмите Enter для выхода")
        
        
        
        
        

