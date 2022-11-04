class employee:
    
    def __init__(self. firstname, lastname, salary)
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." + self.lastname +"@kite.com"

    def giveRaise(self, salary):
    
        self.salary = salary
    
class developer(employee):
    
    def __init__(self, firstname, lastname, salary, programming_languages):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = programming_languages
    
    