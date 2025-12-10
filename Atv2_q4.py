# Colab: https://colab.research.google.com/drive/1UgmV-sanl-RVpMrdSWoJcr4MIRxjnDNp?usp=drive_open

from matplotlib import pyplot as plt
import numpy as np

limiteStepSize = 0.001
slope = 0
oldb3=0
newb3=0
stepSize=0
maxSteps = 10
learningRate = 0.1
w1 = 3.34
w2 = -3.53
w3 = -1.22
w4 = -2.30
b1 = -1.43
b2 = 0.57
b3 = 0

neuronioIy_values = []
neuronioSy_values = []

xDosage_values = [0, 0.5, 1]
yOutput_values = [0, 1, 0]

def neuronioSuperior():
    eixoXDaFuncaoDeAtivacaoAzul = []
    xDaFuncaoDeAtivacao = 0
    eixoXComum = []

    while xDaFuncaoDeAtivacao<=1: # cria o eixo x para a funcao de ativacao com valore normais
        eixoXDaFuncaoDeAtivacaoAzul.append(xDaFuncaoDeAtivacao)
        eixoXComum.append(xDaFuncaoDeAtivacao)
        xDaFuncaoDeAtivacao += 0.25 # eixoXDaFuncaoDeAtivacaoAzul = [0, 0.25, 0.5, 0.75, 1.0]
    
    for i in range(len(eixoXDaFuncaoDeAtivacaoAzul)): #passa o eixo x normal no w1 e b1
        res1 = eixoXDaFuncaoDeAtivacaoAzul[i]*w1
        res2 = res1+b1
        eixoXDaFuncaoDeAtivacaoAzul[i] = res2

    
    eixoYDaFuncaoDeAtivacao = []

    for i in range(len(eixoXDaFuncaoDeAtivacaoAzul)): # Criando o eixo y da funcao de ativacao pelo x
        yDaFuncaoDeAtivacao = np.log(1 + np.exp(eixoXDaFuncaoDeAtivacaoAzul[i]))
        eixoYDaFuncaoDeAtivacao.append(float(yDaFuncaoDeAtivacao))
    
    for i in range(len(eixoXDaFuncaoDeAtivacaoAzul)): # Multiplicando a funcao de ativacao azul por w3
        res1 = eixoYDaFuncaoDeAtivacao[i]*w3
        eixoYDaFuncaoDeAtivacao[i] = res1

    return eixoYDaFuncaoDeAtivacao

def neuronioInferior():
    eixoXDaFuncaoDeAtivacaoAzul = []
    xDaFuncaoDeAtivacao = 0
    eixoXComum = []

    while xDaFuncaoDeAtivacao<=1: # cria o eixo x para a funcao de ativacao com valore normais
        eixoXDaFuncaoDeAtivacaoAzul.append(xDaFuncaoDeAtivacao)
        eixoXComum.append(xDaFuncaoDeAtivacao)
        xDaFuncaoDeAtivacao += 0.25 # eixoXDaFuncaoDeAtivacaoAzul = [0, 0.25, 0.5, 0.75, 1.0]
    
    for i in range(len(eixoXDaFuncaoDeAtivacaoAzul)): #passa o eixo x normal no w2 e b2
        res1 = eixoXDaFuncaoDeAtivacaoAzul[i]*w2
        res2 = res1+b2
        eixoXDaFuncaoDeAtivacaoAzul[i] = res2

    
    eixoYDaFuncaoDeAtivacao = []

    for i in range(len(eixoXDaFuncaoDeAtivacaoAzul)): # Criando o eixo y da funcao de ativacao pelo x
        yDaFuncaoDeAtivacao = np.log(1 + np.exp(eixoXDaFuncaoDeAtivacaoAzul[i]))
        eixoYDaFuncaoDeAtivacao.append(float(yDaFuncaoDeAtivacao))

    for i in range(len(eixoXDaFuncaoDeAtivacaoAzul)): # Multiplicando a funcao de ativacao azul por w4
        res1 = eixoYDaFuncaoDeAtivacao[i]*w4
        eixoYDaFuncaoDeAtivacao[i] = res1

    return eixoYDaFuncaoDeAtivacao

def criandoGreenSquiggle():
    neuronioSy_values = neuronioSuperior()
    neuronioIy_values = neuronioInferior()

    eixoXDaFuncaoDeAtivacaoAzul = []
    xDaFuncaoDeAtivacao = 0
    eixoXComum = []

    while xDaFuncaoDeAtivacao<=1: # cria o eixo x para a funcao de ativacao com valore normais
        eixoXDaFuncaoDeAtivacaoAzul.append(xDaFuncaoDeAtivacao)
        eixoXComum.append(xDaFuncaoDeAtivacao)
        xDaFuncaoDeAtivacao += 0.25 # eixoXDaFuncaoDeAtivacaoAzul = [0, 0.25, 0.5, 0.75, 1.0]

    greenSquiggleArray = []

    for i in range(len(eixoXDaFuncaoDeAtivacaoAzul)):
        greenSquiggleArray.append(neuronioSy_values[i]+neuronioIy_values[i]+b3)
    
    return greenSquiggleArray

def sumOfSquaredResiduals():
    res = 0
    for i in range(len(xDosage_values)):
        res += (yOutput_values[i]-greenSquiggleArrayGlob[i*2])**2
    return res

def derivadaSumOsSquaredResiduals():
    res=0
    for i in range(len(xDosage_values)):
        f_prime = -2*(yOutput_values[i]-greenSquiggleArrayGlob[i*2])*1
        res += f_prime
    return res

def mostrarInfor():
    print(f'Slope: {slope:.2f} || b3: {b3:.2f} || Old b3: {oldb3:.2f} || New b3: {newb3:.2f} || Step size: {stepSize:.6f} || Learning rate: {learningRate:.2f}')

greenSquiggleArrayGlob = criandoGreenSquiggle()

# Repetição dos passos

for i in range(maxSteps):
    mostrarInfor()
    oldb3 = b3
    slope = derivadaSumOsSquaredResiduals()
    stepSize = slope*learningRate
    if(stepSize**2<=limiteStepSize**2): # Condição de parada pelo tamanho do stepsize
        print(f'O stepsize ({stepSize*-1:.4f}) ficou menor que {limiteStepSize}')
        break
    newb3 = oldb3-stepSize
    b3 = newb3
    greenSquiggleArrayGlob = criandoGreenSquiggle()