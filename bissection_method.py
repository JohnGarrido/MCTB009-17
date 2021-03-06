# -*- coding: utf-8 -*-
"""Bissection Method

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qoW8YL9E4fgPSaLAAOXCMnEsxt58q1B9
"""

import pandas as pd
import numpy as np
import math

def f(x):
    return math.sin(x) - math.cos(x) #o polinomio deve ser modificado aqui para cada caso

def bissec(f,m,M,acu,max): #implementando o metodo de bissecção

  contador = 0;

  alpha = (1/2) * (M+m)
  
  while(f(alpha-acu)*f(alpha+acu) > 0 and contador<=max):

    alpha = (1/2) * (M+m)
  
    if(f(alpha)*f(M) <= 0):
      m = alpha

    elif(f(alpha)*f(m) <= 0):
      M = alpha

    contador+=1
    valor_da_funcao = f(alpha)

    print('Passo {} : {}'.format(contador, alpha))

acu = float(input('acu:'))
m = float(input('m: '))
M = float(input('M: '))
max = int(input('max: '))

bissec(f,m,M,acu,max)

