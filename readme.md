#Turing Machine Simulator

This project is a simple Turing Machine simulator a module I'm currently taking
at QMUL.

The file input format is described in `input-format.md`.

##Usage

Just run in terminal using the name of the Turing Machine as the first command
line argument.

    ./tm.py example.tm

##Notes

Currently the tape is initialized as containing only the caracter `e` on the
first position and the initial state is always `b`, I intend to change these
"default" options with command line arguments later.
