from general import Person


class Student(Person):
    def __init__(self, **kwargs):
        Person.setFirstName(self, kwargs['firstName'])
        Person.setLastName(self, kwargs['lastName'])
        Person.setGender(self, kwargs['gender'])
        Person.setDateOfBirth(self, kwargs['dOB'])
        Student.setDateOfEnrollment(self, kwargs['dOE'])

    def getDateOfEnrollment(self):
        return self._dateOfEnrollment

    def setDateOfEnrollment(self, dOE=None):
        if dOE:
            self._dateOfEnrollment = dOE

    def __str__(self):
        return f''
