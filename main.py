from qiskit import *
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.compiler import transpile
from qiskit.quantum_info.operators import Operator, Pauli
from qiskit.quantum_info import process_fidelity
from qiskit.extensions import RXGate, CnotGate, XGate, HGate
# Boolean to check the loop
K = False
# Function to check if the circuit submitted by the player is correct
def check_circuit(reference, user):
    op_reference=Operator(reference)
    op_user=Operator(user)
    if op_user.equiv(op_reference):
        return True
    else:
        return False
###################### CHECKERS  ##########################################
#Select the level
if __name__ == '__main__':
    from lvl import levels
    from user_circuit import ucirc
    i=input("Choose a level:")
    i=int(i)-1
    a=check_circuit(levels[i].circ,ucirc)
    print(a)
