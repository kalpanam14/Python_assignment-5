class Student:
    __name = None
    __rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


s1 = Student()
s1.setName("Kalpana")
print("Name:", s1.getName())
s1.setRollNumber(1345)
print("Roll Number:", s1.getRollNumber())