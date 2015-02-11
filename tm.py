#!/usr/bin/env python3
#
# tm.py
#   by alemedeiros <alexandre.n.medeiros _at_ gmail.com>

"""
A simple turing machine simulator for ECS631U - Computability module on QMUL.

Input file defininiton on the file input-format.md
"""

import csv
import sys

VERB = False

class TuringMachine(object):
    """ Turing Machine Class """
    def __init__(self, tm_def, start, tape):
        self.head = 0
        self.tape = tape
        self.state = start
        self.definition = tm_def

    def __str__(self):
        string = 'state: ' + self.state + '\n'
        string = string + 'tape: ' + self.tape_string() + '\n'
        string = string + '      ' + self.head_string() + '\n'
        string = string + 'seq: ' + self.computed_sequence() + '\n'
        return string

    def tape_string(self):
        """ Convert list of chars to a string """
        string = ''
        for cur in self.tape:
            string = string + cur
        return string

    def head_string(self):
        """ Create a string in which the '^' will mark the machine's head
        position when printed below the tape string """
        string = ''
        for _ in range(self.head):
            string = string + ' '
        string = string + '^'
        return string

    def exec_step(self):
        """ Execute a step on the Turing Machine, acording to its definition """
        sym = self.tape[self.head]

        # Get operation and next state from machine definition
        ops = self.definition.get((self.state, sym))
        if ops == None:
            print('No operation defined! Circular Machine', file=sys.stderr)
            sys.exit(1)

        if VERB:
            print('operations: ' + ops[0])
        # There may be multiple operations separated by comma
        for cur in ops[0].split(','):
            if VERB:
                print('current operation: ' + cur)
            # Check which operation (also check for 'no operation' - empty
            # string)
            if cur == '':
                continue
            elif cur == 'L':
                # Check if going out of the tape
                if self.head == 0:
                    print('moving head to left from initial position', file=sys.stderr)
                    sys.exit(1)
                # Move head left
                self.head = self.head - 1
            elif cur == 'R':
                # Check if tape needs to be increased
                if len(self.tape) == self.head + 1:
                    self.tape.append('-')
                # Move head right
                self.head = self.head + 1
            elif cur == 'E':
                # Erase
                self.tape[self.head] = '-'
            elif cur[0] == 'P':
                # Print
                self.tape[self.head] = cur[1]
            else:
                # Something wrong!
                print('undefined operation', file=sys.stderr)
                sys.exit(1)

        # Update state
        self.state = ops[1]

    def computed_sequence(self):
        """ Generate a string with the computed sequence of a Turing Machine """
        seq = ''
        for i in [elem for elem in self.tape if elem == '0' or elem == '1']:
            seq = seq + i
        return seq

def main():
    """ Script starting point """
    # Read Turing Machine definition
    tm_file = csv.reader(open(sys.argv[1], 'r'), delimiter=';')

    tm_def = dict()
    for line_aux in tm_file:
        # Remove all spaces from strings
        line = [s.replace(' ', '') for s in line_aux]

        st_config = line[0]
        syms = line[1].split(',')
        ops = line[2]
        fn_config = line[3]

        # Build a dictionary
        for sym in syms:
            tm_def[(st_config, sym)] = (ops, fn_config)

    if VERB:
        for k in tm_def.keys():
            print(k, tm_def[k])

    # Start Turing Machine
    # For now, convention is to start at state 'b'
    mach = TuringMachine(tm_def, 'b', ['e'])

    print('Starting turing machine execution')
    print('type \'stop\' to stop or press enter for next step')
    print(mach)

    # Execution cycle
    while input() != 'stop':
        mach.exec_step()
        print(mach)


# Check if is running as script
if __name__ == '__main__':
    main()
