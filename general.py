class Person:
    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def getGender(self):
        return self._gender

    def setGender(self, g=None):
        if g:
            self._gender = g

    def getDateOfBirth(self):
        return self._dateOfBirth

    def setFirstName(self, n=None):
        if n:
            self._firstName = n

    def setLastName(self, l=None):
        if l:
            self._lastName = l

    def setDateOfBirth(self, dOB=None):
        if dOB:
            self._dateOfBirth = dOB
