# Colab: https://colab.research.google.com/drive/18e7-g2OFhj3Z-9hcUD1xHGP0R1YX9bDV?usp=drive_open

from matplotlib import pyplot as plt
import numpy as np

xweight_values = [0.5, 2.3, 2.9]
yheight_values = [1.4, 1.9, 3.2]
sumOfSquareResiduals = 0
intercept = 0
slope = 0.64
derivadaSumOfSquareResiduals = 0
stepSize = 0
learningRate = 0.1
newIntercept = 0
oldIntercept = 0
maxsteps = 10
slopedacurva = 0
menorslopedareta = 0.001
sumSteps = 0
xIntercept_values = []
ySumOfSquaredResiduals = []

fig, ax = plt.subplots(1, 2, figsize=(10,4))
plt.subplots_adjust(wspace=0.4)

def mostrarInfos():
    print(f"| Intercept: {intercept:.2f} || Slope da curva: {slopedacurva:.1f} || Step size: {stepSize:.4f} || New intercept: {newIntercept:.2f} |")

def predictedHeight():
    weight = xweight_values[i]
    res = intercept + slope * weight
    return res

def residual():
    height = yheight_values[i]
    res = height - predictedHeight()
    return res

def derivarSomaDosQuadradosResiduais():
    height = yheight_values[i]
    weight = xweight_values[i]
    f_prime = -2 * (height - (intercept + slope * weight))
    return f_prime

x = np.linspace(0, 5, 20)
def atualizarReta():
    y = intercept + slope * x
    ax[0].plot(x, y, label=f'intercept = {intercept:.2f}')

# passo inicial com intercept = 0
sumSteps += 1
xIntercept_values.append(intercept)
soma = 0
for i in range(len(xweight_values)):
    derivadaSumOfSquareResiduals += derivarSomaDosQuadradosResiduais()
    sumOfSquareResiduals += residual()**2
slopedacurva = derivadaSumOfSquareResiduals
stepSize = slopedacurva*learningRate
newIntercept = intercept-stepSize
ySumOfSquaredResiduals.append(sumOfSquareResiduals)
atualizarReta()
mostrarInfos()
for i in range(maxsteps-1):
    sumOfSquareResiduals = 0
    intercept = newIntercept
    xIntercept_values.append(intercept)
    derivadaSumOfSquareResiduals = 0
    for i in range(len(xweight_values)):
        derivadaSumOfSquareResiduals += derivarSomaDosQuadradosResiduais()
        sumOfSquareResiduals += residual()**2
    ySumOfSquaredResiduals.append(sumOfSquareResiduals)
    slopedacurva = derivadaSumOfSquareResiduals
    stepSize = slopedacurva*learningRate
    newIntercept = intercept-stepSize
    mostrarInfos()
    atualizarReta()
    sumSteps += 1
    if(stepSize**2<=menorslopedareta**2): # Condição de parada pelo tamanho do stepsize
        print(f'O stepsize ({stepSize*-1:.4f}) ficou menor que {menorslopedareta}')
        break
    elif(sumSteps >= maxsteps):
        print(f'O numero maximo de passos {maxsteps} foi alcancado {sumSteps}')
        break

def mostrarGrafico():
    ax[0].scatter(xweight_values, yheight_values)
    ax[0].set_xlim(0, 3)
    ax[0].set_ylim(0, 4)
    ax[0].legend()
    ax[0].set_xlabel("Weight")
    ax[0].set_ylabel("Height")
    
    ax[1].plot(xIntercept_values, ySumOfSquaredResiduals)
    ax[1].scatter(xIntercept_values, ySumOfSquaredResiduals)
    ax[1].set_xlim(0, 2)
    ax[1].set_xlabel("Intercept")
    ax[1].set_ylabel("Sum of squared residuals")
    plt.show()

mostrarGrafico()
