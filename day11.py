from typing import List, Optional
import math


class Monkey:
    def __init__(self, monkey_data, num):
        self.number: int = num
        self.items: List[int] = []
        self.operation: str = ''
        self.test: int = 0
        self.true_monkey_num: int = 0
        self.true_monkey: Optional[Monkey] = None
        self.false_monkey_num: int = 0
        self.false_monkey: Optional[Monkey] = None
        self.parse_data(monkey_data)
        self.inspection_count: int = 0

    def parse_data(self, monkey_data):
        line: str
        for line in monkey_data:
            if line.startswith("Starting items:"):
                items: str
                _, items = line.split(':')
                items = items.replace(',', '')
                for item in items.split():
                    self.items.append(int(item))
            if line.startswith("Operation"):
                operation: str = line.split('=')[-1]
                self.operation = operation.lstrip()
            if line.startswith("Test"):
                self.test = int(line.split()[-1])
            if line.startswith("If true"):
                self.true_monkey_num = int(line.split()[-1])
            if line.startswith("If false"):
                self.false_monkey_num = int(line.split()[-1])

    def do_a_round(self):
        for i in range(len(self.items)):
            self.inspection_count += 1
            item = self.items.pop(0)
            old: int = item
            new = eval(self.operation)
            if new % self.test:
                print(f"False: Monkey: {self.number} Level: {new} To Monkey: {self.false_monkey_num}")
                assert self.false_monkey_num == self.false_monkey.number
                self.false_monkey.items.append(new)
            else:
                print(f"True: Monkey: {self.number} Level: {new} To Monkey: {self.true_monkey_num}")
                assert self.true_monkey_num == self.true_monkey.number
                self.true_monkey.items.append(new)


def doit(monkey_data):
    all_monkeys: List[Monkey] = []
    a_monkey_data: List[str] = []
    monkey_number: int = 0
    for line in monkey_data:
        if not line:
            all_monkeys.append(Monkey(a_monkey_data, monkey_number))
            a_monkey_data = []
            monkey_number += 1
        else:
            a_monkey_data.append(line.lstrip())
    all_monkeys.append(Monkey(a_monkey_data, monkey_number))
    for monkey in all_monkeys:
        monkey.true_monkey = all_monkeys[monkey.true_monkey_num]
        monkey.false_monkey = all_monkeys[monkey.false_monkey_num]

    for i in range(20):
        print(f"Round: {i}")
        for monkey in all_monkeys:
            monkey.do_a_round()

    inspection_counts = []
    for monkey in all_monkeys:
        print(monkey.inspection_count)
        inspection_counts.append(monkey.inspection_count)
    inspection_counts.sort(reverse=True)
    answer = inspection_counts[0] * inspection_counts[1]
    return answer

#  Part II not happening today
