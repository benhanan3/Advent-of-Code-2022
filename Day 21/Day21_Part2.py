import re

MISSING_VALUE = -999999

class Monkey():
    def __init__(self, name, children, operation, number):
        self.name = name

        self.childrenName = children
        self.childObject1 = None
        self.childObject2 = None

        self.childValue1 = None
        self.childValue2 = None

        self.operation = operation
        self.number = number


    def connect_children(self):
        if (not self.childrenName):
            return
        
        self.childObject1 = monkeyDict[self.childrenName[0]]
        self.childObject2 = monkeyDict[self.childrenName[1]]

        self.childObject1.connect_children()
        self.childObject2.connect_children()


    def get_value(self):
        # monkey has number or already calculated
        if self.number:
            if (self.number == MISSING_VALUE):
                return MISSING_VALUE
            else:
                return self.number
            
        # calculate the values for each child monkey
        else:
            self.childValue1 = self.childObject1.get_value()
            self.childValue2 = self.childObject2.get_value()

            if (self.childValue1 == MISSING_VALUE or self.childValue2 == MISSING_VALUE):
                return MISSING_VALUE
            
            self.number = execute_operation(self.childValue1, self.childValue2, self.operation)

            return self.number

    
    def solve_humn(self):
        self.childValue1 = self.childObject1.get_value()
        self.childValue2 = self.childObject2.get_value()

        # branches equal each other
        if self.childValue1 == MISSING_VALUE:
            self.childObject1.number = self.childValue2
            return self.childObject1.recursive_find_humn()

        else:
            self.childObject2.number = self.childValue1
            return self.childObject2.recursive_find_humn()

        
    def recursive_find_humn(self):
        self.childValue1 = self.childObject1.get_value()
        self.childValue2 = self.childObject2.get_value()

        if self.childValue1 == MISSING_VALUE:
            self.childObject1.number = inverse_operation(self.number, self.childValue2, self.operation, 1)

            if (self.childrenName[0] == "humn"):
                return self.childObject1.number
            
            return self.childObject1.recursive_find_humn()
        

        if self.childValue2 == MISSING_VALUE:
            self.childObject2.number = inverse_operation(self.number, self.childValue1, self.operation, 2)
            
            if (self.childrenName[1] == "humn"):
                return self.childObject2.number
            
            return self.childObject2.recursive_find_humn()



# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def execute_operation(number1, number2, operation):
    match operation:
        case "+":
            return number1 + number2
        
        case "-":
            return number1 - number2
        
        case "*":
            return number1 * number2
        
        case "/":
            return number1 / number2


def inverse_operation(number1, number2, operation, branch):
    match operation:
        case "+":
            return number1 - number2
        
        # subtraction not commutative
        case "-":
            if (branch == 1):
                return number1 + number2
            elif (branch == 2):
                return number2 - number1
        
        case "*":
            return number1 / number2
        
        # subtraction not commutative
        case "/":
            if (branch == 1):
                return number1 * number2
            elif (branch == 2):
                return number2 / number1

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
part2 = True
debugInput = True

regex_monkeyName = r"(\w{4})"
regex_children = r"\w{4}[:]\s(?P<child1>\w{4})\s(?:[+\-*/])\s(?P<child2>\w{4})"
regex_operation = r"\w{4}[:]\s(?:\w{4})\s(?P<operation>[+\-*/])\s(?:\w{4})"
regex_number = r"\w{4}[:]\s(?P<number>\d+)"


with open('input.txt', 'r') as fid:
    input = fid.readlines()

monkeyDict = {}

for i in range(len(input)):
    line = input[i].strip()

    monkeyName = re.search(regex_monkeyName, line).group()
    children = re.findall(regex_children, line)[0] if re.findall(regex_children, line) else None
    operation = re.search(regex_operation, line).group(1) if re.search(regex_operation, line) else None
    number = int(re.search(regex_number, line).group(1)) if re.search(regex_number, line) else None

    if (debugInput == True):
        print("input: ", line)
        print("name: ", monkeyName)
        print("children: ", children)
        print("operation: ", operation)
        print("number: ", number, "\n")
    
    if ((monkeyName == "humn") and (part2 == True)):
        number = MISSING_VALUE

    currentMonkey = Monkey(monkeyName, children, operation, number)
    monkeyDict.update({monkeyName: currentMonkey})

    if monkeyName == "root":
        root = currentMonkey


root.connect_children()

num = root.solve_humn()

print(num)