class StudentRoom():
    def __init__(self, name): 
        self.name = name
        self.__score = 0  # 含 __ 则为私有变量
    def print_file(self):
        print('name:' + self.name)

student = StudentRoom('小图')
student.print_file()