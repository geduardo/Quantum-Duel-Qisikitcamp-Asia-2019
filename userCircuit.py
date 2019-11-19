
# coding: utf-8

# In[1]:


from qiskit import *


# In[13]:


def userCircuit(usr_input):

    usr_cir = usr_input.replace('"',"").split(",")

    qc = QuantumCircuit(2)

    i=0

    while(i < len(usr_cir)):
        if usr_cir[i] == "X":
            i += 1
            if usr_cir[i] == "0":
                qc.x([0])
            elif usr_cir[i] == "1":
                qc.x([1])
            i += 1
        elif usr_cir[i] == "Z":
            i += 1
            if usr_cir[i] == "0":
                qc.z([0])
            elif usr_cir[i] == "1":
                qc.z([1])
            i += 1
        elif usr_cir[i] == "H":
            i += 1
            if usr_cir[i] == "0":
                qc.h([0])
            elif usr_cir[i] == "1":
                qc.h([1])
            i += 1
        elif usr_cir[i] == "CX":
            i += 1
            if usr_cir[i] == "0" and usr_cir[i+1] == "1":
                qc.cx([0],[1])
            elif usr_cir[i] == "1" and usr_cir[i+1] == "0":
                qc.cx([1],[0])
            i += 2

    return qc


# In[14]:


if __name__ == '__main__':
    usr_input = input("user circuit:")
    uc = userCircuit(usr_input)
    print(uc)

