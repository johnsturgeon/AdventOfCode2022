class CPU:
    def __init__(self):
        self.reg_x: int = 1
        self.values_at_cycle = []
        self.pixels_at_cycle = []
        self.values_at_cycle.append(self.reg_x)
        self.draw_pixel_at_cycle()

    def process_instruction(self, instruction: str):
        if instruction == 'noop':
            self.values_at_cycle.append(self.reg_x)
            self.draw_pixel_at_cycle()
            return
        if instruction.startswith('addx'):
            _, amt = instruction.split()
            amt = int(amt)
            self.values_at_cycle.append(self.reg_x)
            self.draw_pixel_at_cycle()
            self.reg_x += amt
            self.values_at_cycle.append(self.reg_x)
            self.draw_pixel_at_cycle()

    def draw_pixel_at_cycle(self):
        if self.reg_x - 1 <= (len(self.values_at_cycle) - 1) % 40 <= self.reg_x + 1:
            self.pixels_at_cycle.append('#')
        else:
            self.pixels_at_cycle.append('.')


def get_signal_strength(instructions):
    my_cpu = CPU()
    for instruction in instructions:
        my_cpu.process_instruction(instruction)
    cycles_to_inspect = [20, 60, 100, 140, 180, 220]
    sum_of_signals: int = 0
    for cycle in cycles_to_inspect:
        sum_of_signals += cycle * my_cpu.values_at_cycle[cycle-1]
    pixels: int = 0
    print('')
    for pixel in my_cpu.pixels_at_cycle:
        if pixels == 40:
            pixels = 0
            print('')
        pixels += 1
        print(pixel, end='')
    return sum_of_signals
