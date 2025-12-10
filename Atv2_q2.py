# Colab: https://colab.research.google.com/drive/1IPQTT6nQ4nd5kYg3x3G9vF8OwMQpYxuq?usp=drive_open

from matplotlib import pyplot as plt
import numpy as np

xweight_values = [0.5, 2.3, 2.9]
yheight_values = [1.4, 1.9, 3.2]

sumOfSquareResiduals = 0
intercept = 0
slope = 1
learningRate = 0.05
menorslopedareta = 0.001

derivadaSumOfSquareResiduals = 0
dSlopederivadaSumOfSquareResiduals = 0

stepSize = 0
stepSizeSlope = 0
newIntercept = 0
newSlope = 0

maxsteps = 500
sumSteps = 0

slopedacurva = 0
xIntercept_values = []
ySumOfSquaredResiduals = []

fig, ax = plt.subplots(1, 2, figsize=(10,4))
plt.subplots_adjust(wspace=0.4)

def mostrarInfos():
    print(f"| Intercept: {intercept:.4f} || "
          f"Gradiente intercept: {slopedacurva:.4f} || "
          f"Step size intercept: {stepSize:.4f} || "
          f"New intercept: {newIntercept:.4f} || "
          f"Slope: {slope:.4f} || "
          f"Step size slope: {stepSizeSlope:.4f} || "
          f"New slope: {newSlope:.4f}")

def predictedHeight():
    return intercept + slope * xweight_values[i]

def residual():
    return yheight_values[i] - predictedHeight()

def derivarSomaDosQuadradosResiduais():
    return -2 * (yheight_values[i] - (intercept + slope * xweight_values[i]))

def dSlopeSomaDosQuadradosResiduais():
    return -2 * xweight_values[i] * (yheight_values[i] - (intercept + slope * xweight_values[i]))

x = np.linspace(0, 5, 20)
def atualizarReta():
    y = intercept + slope * x
    ax[0].plot(x, y,)

sumSteps += 1
xIntercept_values.append(intercept)

for i in range(len(xweight_values)):
    derivadaSumOfSquareResiduals += derivarSomaDosQuadradosResiduais()
    dSlopederivadaSumOfSquareResiduals += dSlopeSomaDosQuadradosResiduais()
    sumOfSquareResiduals += residual()**2

grad_intercept = derivadaSumOfSquareResiduals
grad_slope = dSlopederivadaSumOfSquareResiduals

stepSize = learningRate * grad_intercept
stepSizeSlope = learningRate * grad_slope

newIntercept = intercept - stepSize
newSlope = slope - stepSizeSlope

ySumOfSquaredResiduals.append(sumOfSquareResiduals)
atualizarReta()
mostrarInfos()
for i in range(maxsteps - 1):

    intercept = newIntercept
    slope = newSlope

    xIntercept_values.append(intercept)

    derivadaSumOfSquareResiduals = 0
    dSlopederivadaSumOfSquareResiduals = 0
    sumOfSquareResiduals = 0

    for i in range(len(xweight_values)):
        derivadaSumOfSquareResiduals += derivarSomaDosQuadradosResiduais()
        dSlopederivadaSumOfSquareResiduals += dSlopeSomaDosQuadradosResiduais()
        sumOfSquareResiduals += residual()**2

    ySumOfSquaredResiduals.append(sumOfSquareResiduals)
    grad_intercept = derivadaSumOfSquareResiduals
    grad_slope = dSlopederivadaSumOfSquareResiduals
    stepSize = grad_intercept * learningRate
    stepSizeSlope = grad_slope * learningRate
    newIntercept = intercept - stepSize
    newSlope = slope - stepSizeSlope

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
    ax[0].set_xlabel("Weight")
    ax[0].set_ylabel("Height")
    
    ax[1].plot(xIntercept_values, ySumOfSquaredResiduals)
    ax[1].scatter(xIntercept_values, ySumOfSquaredResiduals)
    ax[1].set_xlim(0, 2)
    ax[1].set_xlabel("Intercept")
    ax[1].set_ylabel("Sum of squared residuals")
    plt.show()

mostrarGrafico()
