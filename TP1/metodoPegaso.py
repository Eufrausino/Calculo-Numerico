import math

def PEGASO(func, MaxIteracoes, iteracoes, precisao, x0, limiteInferior, limiteSuperior):
    while iteracoes < MaxIteracoes:
        f_inferior = func(limiteInferior)
        f_superior = func(limiteSuperior)
        r = f_superior * (limiteSuperior - limiteInferior) / (f_superior - f_inferior)
        x0 = x0 - r
        FX = func(x0)

        if abs(FX - f_superior) < precisao:
            return x0, iteracoes
        
        if FX * f_superior > 0:
            limiteInferior = limiteSuperior
            limiteSuperior = x0
        else:
            limiteInferior = x0
        
        iteracoes += 1

def func(x0):
    return x0**2 - 4

# a = 2.0  
# b = 3.0  
# precisao = 1e-6  
# MaxIteracoes = 1000 
# x0 = (a + b) / 2 

# RAIZ, iteracoes = PEGASO(func, MaxIteracoes, 0, precisao, x0, a, b)

# print("A raiz da equação é: {}".format(RAIZ))
# print("Iterações gastas: {}".format(iteracoes))