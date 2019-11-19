
# coding: utf-8

# In[3]:


from qiskit import *
from qiskit.tools.visualization import plot_histogram
import numpy as np


# In[4]:


def addGate(input):

    q = QuantumRegister(1) # a qubit in which to encode and manipulate the input
    c = ClassicalRegister(1) # a bit to store the output
    qc = QuantumCircuit(q, c) # this is where the quantum program goes
    

    if input=='X':
        qc.x(q[0])

    qc.measure(q[0], c[0])
    
    # We'll run the program on a simulator
    backend = Aer.get_backend('qasm_simulator')
    # Since the output will be deterministic, we can use just a single shot to get it
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))
    
    return output


# In[15]:


print("Initial state: |0⟩")
print("Final state: |1⟩")

x = input("Input a correct gate: ")
result = addGate(x)
print("output is ", result)
if result == "1":
    print("correct")
else:
    print("incorrect")

