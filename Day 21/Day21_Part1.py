import re


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
            return self.number
            
        # calculate the values for each child monkey
        else:
            self.childValue1 = self.childObject1.get_value()
            self.childValue2 = self.childObject2.get_value()

            self.number = execute_operation(self.childValue1, self.childValue2, self.operation)

            return self.number

            

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





# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

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
    
    currentMonkey = Monkey(monkeyName, children, operation, number)
    monkeyDict.update({monkeyName: currentMonkey})

    if monkeyName == "root":
        root = currentMonkey

root.connect_children()



