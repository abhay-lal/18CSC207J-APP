class Dept:
    def _init_(self, student_name='SCO'):
        self.student_name = student_name


st1 = Dept()
st2 = Dept('John')

print(st1.student_name)
print(st2.student_name)
