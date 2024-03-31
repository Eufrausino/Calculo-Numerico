import math

def PEGASO(func, MaxIteracoes, iteracoes, precisao, x0, limiteInferior, limiteSuperior):
    print('*'*40)
    print("| {:^10} | {:^10} | {:^10} |".format('iteracoes', 'x0', 'F(x0)'))
    print('*'*40)
    while iteracoes < MaxIteracoes:
        f_inferior = func(limiteInferior)
        f_superior = func(limiteSuperior)
        r = f_superior * (limiteSuperior - limiteInferior) / (f_superior - f_inferior)
        x0 = x0 - r
        FX = func(x0)

        if abs(FX - f_superior) < precisao:
            print("| {:^10} | {:^10.4f} | {:^10.4f} |".format(iteracoes, x0, FX))
            return x0, iteracoes

        if FX * f_superior > 0:
            limiteInferior = limiteSuperior
            limiteSuperior = x0
            print("| {:^10} | {:^10.4f} | {:^10.4f} |".format(iteracoes, x0, FX))
        else:
            limiteInferior = x0
            print("| {:^10} | {:^10.4f} | {:^10.4f} |".format(iteracoes, x0, FX))

        iteracoes += 1
    

def func(x0):
  return x0**2 - 4 

a = 2.0
b = 3.0
precisao = 1e-6
MaxIteracoes = 1000
x0 = (a + b) / 2

RAIZ, iteracoes = PEGASO(func, MaxIteracoes, 0, precisao, x0, a, b)
print('*'*40)