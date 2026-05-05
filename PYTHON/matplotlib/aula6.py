import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, 5, 0.1)
y1 = x**5
y2 = x**2

fig, axes = plt.subplots(nrows=2, ncols=2 ,figsize=(8,4))
plt.suptitle("Gráficos com Subplots")
plt.subplots_adjust(
    left=0.093,
    right=0.948,
    top=0.8,
    bottom=0.148,
    wspace=0.348,
    hspace=0.824
)

axes[0, 0].plot(x,y2)
axes[0, 0].set_title("Função do Segundo Grau $x^2$")
axes[0, 0].set_xlabel("Tempo")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].grid()

axes[0,1].plot(x,y1)
axes[0,1].set_title("Função um gr 1 $x^2$")
axes[0,1].set_xlabel("Tempo")
axes[0,1].set_ylabel("Amplitude")
axes[0,1].grid()

axes[1,0].plot(x,y1)
axes[1,0].set_title("Função um g2 $x^2$")
axes[1,0].set_xlabel("Tempo")
axes[1,0].set_ylabel("Amplitude")
axes[1,0].grid()

axes[1,1].plot(x,y1)
axes[1,1].set_title("Função um gr 3 $x^2$")
axes[1,1].set_xlabel("Tempo")
axes[1,1].set_ylabel("Amplitude")
axes[1,1].grid()

plt.show()