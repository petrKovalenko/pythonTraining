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

#Main Code

rows_number = int(input("Введите количество строк матрицы: "))
cols_number = int(input("Введите количество столбцов матрицы: "))
if rows_number > 0 and cols_number > 0:
    matrix = Matrix(rows_number, cols_number)
    for i in range(1, rows_number):
        row_string = ""
        while not row_string:
            row_string = input("Введите " + cols_number + " элементов строки " + i + " разделённых одним пробелом")
        row_array = row_string.split(" ")
        if not row_array or len(row_array) < cols_number:
            print("Количество элементов в строке меньше чем нужно. Выход.")
            break
        
        
        

