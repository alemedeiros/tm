#Turing Machine file format

The file format for the definition of the Turing Machine is a csv text file
defined as follows:

The file contains at least one line and each line is as follows

    sc ; sym(,sym)* ; [op(,op)*] ; fc

Where

- __sc__ and __fc__ are the start and final m-config of the TM definition,
  respectively
- __sym__ is the symbol under the tape head that would trigger the operations
  described on the line; it may be either a lower case letter, 0, 1 or - (the
  latter representing an empty square on the tape)
- __op__ is the operation executed by the TM

##Notes

- multiple symbols/operations may be separeted by comma
- the operations field of the line may be empty, in which no action is taken
  besides changing the state
- all spaces are _ignored_ so use them to keep you file more human readable
- currently the program _doesn't_ support tab characters on the input file

## Operations

- __R__: move head right
- __L__: move head left
- __E__: erase the symbol under the head
- __Px__: write caracter x under the head (x is defined as a symbol)
