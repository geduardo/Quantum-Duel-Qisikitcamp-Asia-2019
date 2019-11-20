from qiskit import *
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.compiler import transpile
from qiskit.quantum_info.operators import Operator, Pauli
from qiskit.quantum_info import process_fidelity
from qiskit.extensions import RXGate, CnotGate, XGate, HGate

# Template for creating circuits:
class Level:
    def __init__(self, size, initial_state, final_state, initial_circ=None):
        # We create the circuit for the game_mode
        self.q = QuantumRegister(size)
        self.c = ClassicalRegister(size)
        self.size=size
        self.circ=QuantumCircuit(self.q,self.c)
        self.initial_state = initial_state # This is a string
        self.final_state = final_state # This also is a string

        self.initial_circ = initial_circ

########## LEVEL 1 ##################
# We insert the initial and the final state strings in the corresponding arguments of the class
level_1=Level(1,'|0>','1/sqrt(2)*(|0>+|1>)')

# Here we create the circuit applying the corresponding gates:
#------------REFERENCE CIRCUIT ---------------
level_1.circ.h([0])
# --------------------------------------------
#####################################

########## LEVEL 2 ##################

# We insert the initial and the final state strings in the corresponding arguments of the class
level_2=Level(2,'|00>','1/sqrt(2)*(|00>+|11>)')

# Here we create the circuit applying the corresponding gates:
#------------REFERENCE CIRCUIT ------------------------------

level_2.circ.h([0])
level_2.circ.cx([0],[1])

########## LEVEL 3 ##################

level_3=Level(2,'|00>','1/sqrt(2)*(|00>-|11>)')

#Here we create the circuit
level_3.circ.x([0])
level_3.circ.h([0])
level_3.circ.cx([0],[1])

#####################################

########## LEVEL 4 ##################

level_4=Level(2,'|00>','1/sqrt(2)*(|01>+|10>)')

#Here we create the circuit
level_4.circ.h([0])
level_4.circ.cx([0],[1])
level_4.circ.x([1])

########## LEVEL 5 ##################
level_5=Level(2,'|00>','1/sqrt(2)*(|01>-|10>)')

#Here we create the circuit
level_5.circ.h([0])
level_5.circ.cx([0],[1])
level_5.circ.z([0])
level_5.circ.x([1])

########## LEVEL 6 ##################
level_6=Level(1, '|0>', '1/sqrt(2)*(|0>-|1>)')

#Here we create the circuit
level_6.circ.x([0])
level_6.circ.h([0])
#####################################

########## LEVEL 7 ##################
level_7=Level(1,  '1/sqrt(2)*(|0>-|1>)', '|0>', 'X,0,H,0')

#Prepare initial state
level_7.circ.x([0])
level_7.circ.h([0])
#Here we create the circuit
level_7.circ.h([0])
level_7.circ.x([0])


# We create a list with the different levels 
levels=[level_1, level_2, level_3, level_4, level_5, level_6, level_7]
