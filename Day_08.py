import re

class Register:
    def __init__(self, name):
        self.name = name
        self.value = 0


def sort_key(register):
    return register.value


class RegisterRegistry:
    registers = {}
    max_observed_value = 0

    @classmethod
    def value(cls, register_name):
        if register_name in cls.registers:
            return cls.registers[register_name].value
        else:
            r = Register(register_name)
            cls.registers[register_name] = r
            return cls.registers[register_name].value

    @classmethod
    def operate(cls, register_to_modify, inc_or_dec, amount):
        sign = 1 if inc_or_dec=='inc' else -1
        if register_to_modify not in cls.registers:
            cls.registers[register_to_modify] = Register(register_to_modify)
        cls.registers[register_to_modify].value += amount * sign
        if cls.registers[register_to_modify].value > cls.max_observed_value:
            cls.max_observed_value = cls.registers[register_to_modify].value


    @classmethod
    def render_state(cls):
        rval = []
        values = list(cls.registers.values())
        values.sort(key=sort_key ,reverse=True)
        rval.append(f'Max observed value {cls.max_observed_value}\n')
        for register in values:
            rval.append(f'{register.name} = {register.value}\n')
        return ''.join(rval)


class Instruction:
    def __init__(self, register_to_modify, inc_or_dec, amount, register_to_test, operator, test_value):
        self.register_to_modify = register_to_modify
        self.inc_or_dec = inc_or_dec
        self.amount = amount
        self.register_to_test = register_to_test
        self.operator = operator
        self.test_value = test_value
    def __repr__(self):
        return f'Instruction {self.register_to_modify} {self.inc_or_dec} {self.amount} if {self.register_to_test} {self.operator} {self.test_value}'

    def execute(self):
        value = RegisterRegistry.value(self.register_to_test)
        print(f'Name {self.register_to_test} Value {value}')
        match self.operator:
            case '==':
                if value == self.test_value:
                    RegisterRegistry.operate(self.register_to_modify, self.inc_or_dec, self.amount)
            case '!=':
                if value != self.test_value:
                    RegisterRegistry.operate(self.register_to_modify, self.inc_or_dec, self.amount)
            case '>':
                if value > self.test_value:
                    RegisterRegistry.operate(self.register_to_modify, self.inc_or_dec, self.amount)
            case '<':
                if value < self.test_value:
                    RegisterRegistry.operate(self.register_to_modify, self.inc_or_dec, self.amount)
            case '>=':
                if value >= self.test_value:
                    RegisterRegistry.operate(self.register_to_modify, self.inc_or_dec, self.amount)
            case '<=':
                if value <= self.test_value:
                    RegisterRegistry.operate(self.register_to_modify, self.inc_or_dec, self.amount)
            case _:
                raise ValueError(f'Unknown operator {self.operator}')

def read_puzzle_data(filename):
    rval = []
    with open(filename, 'r') as f:
        data = f.read().strip().split('\n')
        for line in data:
            result = re.search('^(\w+) (\w+) ([^ ]+) if (\w+) ([^ ]+) ([^ ]+)$', line)
            rval.append(Instruction(result.group(1), result.group(2), int(result.group(3)), result.group(4), result.group(5), int(result.group(6))))
    return rval


def part_one(filename):
    data = read_puzzle_data(filename)
    for instruction in data:
        instruction.execute()
    print(RegisterRegistry.render_state())

part_one('Day_08_data.txt')
