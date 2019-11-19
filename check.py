import numpy as np
from qiskit import execute, Aer

def check_circuit(reference, user):
    """
    Function to check if the circuit submitted by the player is correct
    """

    backend = Aer.get_backend('statevector_simulator')

    reference_statevector = execute(reference, backend).result().get_statevector(reference)
    user_statevector = execute(user, backend).result().get_statevector(user)

    return (reference_statevector == user_statevector).all()
###################### CHECKERS  ##########################################
#Select the level
from lvl import levels
from user_circuit import ucirc
i=input("Choose a level:")
i=int(i)-1
a=check_circuit(levels[i].circ,ucirc)
print(a)
