from general import Person

class Teacher(Person):
    username = 'teacher'
    password = 'password'
    
    def __init__(self, **kwargs):
        Person.setFirstName(self, kwargs['firstName'])
        Person.setLastName(self, kwargs['lastName'])
        Person.setGender(self, kwargs['gender'])
        Person.setDateOfBirth(self, kwargs['dOB'])
