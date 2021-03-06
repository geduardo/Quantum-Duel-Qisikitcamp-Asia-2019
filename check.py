import numpy as np
from qiskit import execute, BasicAer as Aer

def check_circuit(reference, user):
    """
    Function to check if the circuit submitted by the player is correct
    """

    backend = Aer.get_backend('statevector_simulator')

    reference_statevector = execute(reference, backend).result().get_statevector(reference)
    user_statevector = execute(user, backend).result().get_statevector(user)

    equivalence = np.isclose(reference_statevector, user_statevector)
    if isinstance(equivalence, bool):
        return equivalence
    return equivalence.all()
###################### CHECKERS  ##########################################
#Select the level
if __name__ == '__main__':
    from lvl import levels
    from user_circuit import ucirc
    i=input("Choose a level:")
    i=int(i)-1
    a=check_circuit(levels[i].circ,ucirc)
    print(a)
