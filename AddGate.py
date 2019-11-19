from qiskit import *
from qiskit.tools.visualization import plot_histogram
import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, BasicAer
from qiskit.compiler import transpile
from qiskit.quantum_info.operators import Operator, Pauli
from qiskit.quantum_info import process_fidelity
from qiskit.extensions import RXGate, CnotGate, XGate

def addGate(input):
    q = QuantumRegister(1) # a qubit in which to encode and manipulate the input
    c = ClassicalRegister(1) # a bit to store the output
    qc = QuantumCircuit(q, c) # this is where the quantum program goes
    if input=='X':
        qc.x(q[0])
    if input=='H':
        qc.h(q[0])
    if input=='Y':
        qc.y(q[0])
    output = Operator(qc)
    return output

print("Final state: 1/sqrt(2)*(|0⟩+|1⟩)")
a = input("Input a gate: ")
result = addGate(a)
print("output is ", result)


# if result == "1":
#     print("correct")
# else:
#     print("incorrect")

