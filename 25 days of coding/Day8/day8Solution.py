class Instruction:
    def __init__(self, name, value):
        self.name = name
        self.value = int(value)


def run_instructions(instructions, retrieve_data=False):
    end = len(instructions)
    idx, accumulator = 0, 0
    executed = set()
    instruction_list = []

    for loop in range(end):
        # Store executed index
        executed.add(idx)
        name, value = instructions[idx].name, instructions[idx].value

        # Update index
        if name == 'nop':
            if retrieve_data:
                instruction_list.append(idx)
            idx += 1
        elif name == 'acc':
            idx += 1
            accumulator += value
        elif name == 'jmp':
            if retrieve_data:
                instruction_list.append(idx)
            idx += value

        # Check next index
        if idx in executed:
            if retrieve_data:
                return instruction_list
            return False, accumulator
        elif idx >= end:
            return True, accumulator
    return False, 0


def day8():
    with open('input.txt', 'r') as f:
        instructions = [Instruction(*line.split()) for line in f.read().splitlines()]

    # Part 1
    reached_end, accumulator = run_instructions(instructions)
    print(f'Part1 accumulator: {accumulator}')

    # Part 2
    replace_instruction = {'nop': 'jmp', 'jmp': 'nop', 'acc': 'acc'}
    first_run = run_instructions(instructions, retrieve_data=True)

    for instruction in [instructions[idx] for idx in first_run]:

        instruction.name = replace_instruction[instruction.name]
        reached_end, accumulator = run_instructions(instructions)
        instruction.name = replace_instruction[instruction.name]

        if reached_end:
            break

    print(f'Part2 accumulator: {accumulator}')

day8()