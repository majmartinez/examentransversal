'''
Crear un arreglo de dos dimensiones de tamaño 10 y 4,  el cual, simula a un bus. 
Se pide asignar los números de asiento en forma automática, considerando el siguiente formato:

1	2		3	4
5	6		7	8
9	10		11	12
13	14		15	16
17	18		19	20
21	22		23	24
25	26		27	28
29	30		31	32
33	34		35	36
37	38		39	40
'''

import numpy as np

matrizBus=np.empty((10,4),dtype=object);

asiento=0;
for f in range(10):
    for c in range(4):
        asiento=asiento+1;
        matrizBus[f,c]=asiento;
        
print(matrizBus);

while True:
    fila=int(input("Ingrese la fila de su asiento:"));
    columna=int(input("Ingrese la columna de su asiento: "));
    matrizBus[fila,columna]='X';
    print(matrizBus)



