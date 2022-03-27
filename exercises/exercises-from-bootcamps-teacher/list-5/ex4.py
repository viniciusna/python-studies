"""Uma aproximação para o valor de pi pode ser calculado a partir da fórmula abaixo (uma série infinita): 

pi = 3 + 4*( 1/(2*3*4) - 1/(4*5*6) + 1/(6*7*8) - 1/(8*9*10) + 1/(10*11*12) - ... )

Escreva um programa que calcule o número pi com 15 aproximações.
A primeira aproximação deve considerar apenas o primeiro termo da série, ou seja 3. A segunda aproximação deve considerar a soma até o segundo termo, e assim por diante! """

pi = 3
n = 1

while n < 15 :
    nthTerm = (-1)**(n + 1) * 4/( (2*n + 1)*(2*n + 2)*(2*n + 3) )
    n += 1
    pi += nthTerm

print(pi)