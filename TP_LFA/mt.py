import json
import sys
from collections import defaultdict

class TuringMachine:
    def __init__(self, spec):
        self.states = spec[0]
        self.input_alphabet = spec[1]
        self.tape_alphabet = spec[2]
        self.start_symbol = spec[3]
        self.blank_symbol = spec[4]
        self.transitions = defaultdict(list)
        for t in spec[5]:
            self.transitions[(t[0], t[1])].append((t[2], t[3], t[4]))
        self.initial_state = spec[6]
        self.final_states = set(spec[7])

    def simulate(self, word):
        configurations = [(self.initial_state, list(self.start_symbol + word + self.blank_symbol), 1)]
        while configurations:
            state, tape, head = configurations.pop()
            if state in self.final_states:
                return True
            if head < 0 or head >= len(tape):
                continue
            current_symbol = tape[head]
            for next_state, write_symbol, direction in self.transitions[(state, current_symbol)]:
                new_tape = tape[:]
                new_tape[head] = write_symbol
                new_head = head + (1 if direction == '>' else -1)
                configurations.append((next_state, new_tape, new_head))
        return False

def main():
    if len(sys.argv) != 3:
        print("Usar: ./mt [MT] [Palavra]")
        return

    mt_file = sys.argv[1]
    word = sys.argv[2]

    with open(mt_file, 'r') as f:
        spec = json.load(f)["mt"]

    tm = TuringMachine(spec)
    if tm.simulate(word):
        print("Sim")
    else:
        print("Não")

if __name__ == "__main__":
    main()