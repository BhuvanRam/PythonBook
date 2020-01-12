class PatientRecord:
    def __init__(self, name,age, Pid):
        self.PatId = str(Pid) + str(age)
        self.name = name
        self.age = int(age)
        self.left = None
        self.right = None
