class CTECH:
    pass


class CINTEL:
    pass


class NWC:
    pass


class DSBS:
    pass


obj1 = CTECH()

print('Obj1 belongs to Class CTECH and not CINTEL hence:')
print(isinstance(obj1, CINTEL))
print('Obj1 belongs to Class CTECH')
print(isinstance(obj1, CTECH))
