class Student:
    def __init__(self,name,credit,gpa,school,major,eAddress):
        self.name = name
        self.credit = credit
        self.gpa = gpa
        self.school = school
        self.major = major
        self.eAddress = eAdress

    def getCredit(self):
        return self.credit


    def getGpa(self):
        return self.gpa

    def getSchool(self):
        return self.school


    def getMajor(self):
        return  self.major
    
    def geteAddress(self):
        return self.eAdress
        
    def setCredits(self,credit):
        if credit>0:
            self.credit = credit
            
    def setGpa(self,gpa):
        if gpa>0:
            self.gpa = gpa
        
    def setSchool(self,school):
        if school != " "
            self.school = school
        

    def setMajor(self,major):
        if major != " "
            self.major = major
        

    def seteAddress(self,eAddress):
        if eAddress != " "
            self.eAddress = eAddress

    def isEligibleForGraduation(self):
        eligibility = False
        if self.credit >= 120:
            print(self.credit)
            if self.gpa >= 2.5:
                print(self.credit, self.gpa)
                eligibility = True
        return eligibility

