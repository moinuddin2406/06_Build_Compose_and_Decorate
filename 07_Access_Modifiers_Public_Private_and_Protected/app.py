class Employee:
    def __init__(self ,name ,salary ,ssn):
        self.name = name           # public variable
        self._salary = salary      # protected variable
        self.__ssn = ssn           # private variable

if __name__ == "__main__":
    employee =Employee("Moin",65000 ,"123_0002_54444")
    # access public variable
    print("public variable :" ,employee.name)
    # access protected variable
    print("protected variable :" ,employee._salary)
    # access private variable
    try:
        print("private variable :" ,employee.__ssn)
    except AttributeError:
        print("can nat access private variable __ssn")
        
    