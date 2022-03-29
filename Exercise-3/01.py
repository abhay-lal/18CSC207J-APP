class SRMIST:
    def __init__(self, school, dept1, dept2, dept3, dept4):
        self.school = school
        self.dept1 = dept1
        self.dept2 = dept2
        self.dept3 = dept3
        self.dept4 = dept4

    def print(self):
        print('The departments are:', self.dept1, self.dept2, self.dept3, self.dept4, 'in', self.school)

    def print_new(self, specialisation):
        self.specialisation = specialisation
        print('The departments are:', self.dept3, self.dept4, 'in', self.school,
              'with specialisation', self.specialisation)


obj = SRMIST('SRM', 'CSE', 'ECE', 'EEE', 'ME')

obj.print()
print("Deleting dept1 and dept2 ...")
del obj.dept1
del obj.dept2
obj.print_new('CORE')
