# Colab: https://colab.research.google.com/drive/1A-UWHNxi-axrKSlrwYvxuYV-TQfwFqFF

import numpy as np
import matplotlib.pyplot as plt
xs = [0, 1]
ys = [1, 0]
def shear(xs,ys):
    txv1 = (xs[0]*1 + ys[0]*2 )
    tyv1 = (xs[0]*0 + ys[0]*1 )
    txv2 = (xs[1]*1 + ys[1]*2 )
    tyv2 = (xs[1]*0 + ys[1]*1 )
    xs = [txv1, txv2]
    ys = [tyv1, tyv2]
    return xs,ys
def girar90graus(xs,ys):

    txv1 = (xs[0]*0 + ys[0]*1 )
    tyv1 = (xs[0]*(-1) + ys[0]*0 )
    txv2 = (xs[1]*0 + ys[1]*1 )
    tyv2 = (xs[1]*(-1) + ys[1]*0 )
    xs = [txv1, txv2]
    ys = [tyv1, tyv2]
    return xs, ys
def mudarvetoresnografico(xs, ys):
    lista1 = [int(x) for x in input("Digite a nova coordenada do vetor 1 (x,y): ").split(',')]
    lista2 = [int(x) for x in input("Digite a nova coordenada do vetor 2 (x,y): ").split(',')]

    xs = [lista1[0], lista2[0]]
    ys = [lista1[1], lista2[1]]
    return xs, ys
def mostrargrafico(vetor1, vetor2):
  # coordenadas x e y com cores
  xs = vetor1
  ys = vetor2
  colors = ['r', 'g']

  # largura do gráfico e espaçamento
  xmin, xmax, ymin, ymax = -5, 5, -5, 5
  ticks_frequency = 1

  # pontos
  fig, ax = plt.subplots(figsize=(5, 5))

  # escala dos eixos iguais
  ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

  # ajuste dos eixos
  ax.spines['bottom'].set_position('zero')
  ax.spines['left'].set_position('zero')

  ax.spines['top'].set_visible(False)
  ax.spines['right'].set_visible(False)

  # x e y no final dos eixos
  ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
  ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

  # ajuste dos espaçamentos
  x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
  y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
  ax.set_xticks(x_ticks[x_ticks != 0])
  ax.set_yticks(y_ticks[y_ticks != 0])

  ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
  ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

  ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

  # setas dos eixos
  arrow_fmt = dict(markersize=4, color='black', clip_on=False)
  ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
  ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
  ax.quiver(0, 0, xs[0], ys[0], angles='xy', scale_units='xy', scale=1, color='r')
  ax.quiver(0, 0, xs[1], ys[1], angles='xy', scale_units='xy', scale=1, color='g')
  plt.show()

opc = int(input('Mudar os vetores unitários?\n(1)Sim\n(2)NÂO\n'))
if (opc==1):
  xs, ys = mudarvetoresnografico(xs, ys)
  mostrargrafico(xs,ys)
elif (opc==2):
  mostrargrafico(xs,ys)
opctrans = int(input('Qual transformação fazer?\n(1)Girar 90 graus\n(2)Shear em x\n'))
if (opctrans==1):
    xs, ys = girar90graus(xs,ys)
    mostrargrafico(xs,ys)
elif (opctrans==2):
    xs, ys = shear(xs,ys)
    mostrargrafico(xs,ys)