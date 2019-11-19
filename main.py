from qiskit import *
from qiskit.tools.visualization import plot_histogram
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.compiler import transpile
from qiskit.quantum_info.operators import Operator, Pauli
from qiskit.quantum_info import process_fidelity
from qiskit.extensions import RXGate, CnotGate, XGate, HGate

K = False

# Template for creating circuits:

class Level:
    def __init__(self, size, initial_state, final_state):
        # We create the circuit for the game_mode
        self.q = QuantumRegister(size)
        self.c = ClassicalRegister(size)
        self.circ=QuantumCircuit(self.q,self.c)
        self.initial_state = initial_state # This is a string
        self.final_state = final_state # This also is a string

def check_circuit(reference, user):
    op_reference=Operator(reference)
    op_user=Operator(user)
    if op_user.equiv(op_reference):
        return True
    else:
        return False

########## Example 1 for creating a level: ##################

# We insert the initial and the final state strings in the corresponding arguments of the class
level_1=Level(1,'|0>','1/sqrt(2)*(|0>+|1>)')

# Here we create the circuit applying the corresponding gates:
#------------REFERENCE CIRCUIT ---------------
level_1.circ.h([0])
# --------------------------------------------
##################################################################


########## Example 2 for creating a level: ##################

# We insert the initial and the final state strings in the corresponding arguments of the class
level_2=Level(2,'|00>','1/sqrt(2)*(|00>+|11>)')

# Here we create the circuit applying the corresponding gates:
#------------REFERENCE CIRCUIT ---------------
level_2.circ.h([0])
level_2.circ.cx([0],[1])
##################################################################
level_3=Level(2,'|00>','1/sqrt(2)*(|00>-|11>)')

#Here we create the circuit
level_3.circ.x([0])
level_3.circ.h([0])
level_3.circ.cx([0],[1])

level_4=Level(2,'|00>','1/sqrt(2)*(|01>+|10>)')

#Here we create the circuit
level_4.circ.h([0])
level_4.circ.cx([0],[1])
level_4.circ.x([1])

level_5=Level(2,'|00>','1/sqrt(2)*(|01>-|10>)')

#Here we create the circuit
level_5.circ.h([0])
level_5.circ.cx([0],[1])
level_5.circ.z([0])
level_5.circ.x([1])
###################### CORE OF THE GAME ##########################################

# For the moment just for level 1:

print("The initial state is: " + level_1.initial_state)
print(" You need to obtain the state:" + level_1.final_state)
while K==False:
    print(" Please, modify the circuit in the file user_circuit.py and then press enter to continue.")
    input()
    from user_circuit import*
    if check_circuit(level_1.circ, ucirc):
        print('Congratulations! The circuit is correct')
        K==True
    else:
        print('The circuit is incorrect. Try again.')

