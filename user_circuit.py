from qiskit import *
usize= 1     # Insert here the size of the circuit
uq= QuantumRegister(usize)
uc= ClassicalRegister(usize)
circ=QuantumCircuit(uq,uc)

##### DESIGN HERE THE CIRCUIT ####
circ.x([0])

ucirc=circ