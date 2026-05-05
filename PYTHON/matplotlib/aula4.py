import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)
c = np.cos(x*4)
s = np.sin(x*4)

gra1 = plt.subplot(1, 2, 1)
gra1.set_title("Gráfico Cosseno")
gra1.set_xlabel("Eixo de Tempo")
gra1.set_xlabel("Eixo da Amplitude")
plt.plot(x, c)
plt.grid()

gra2 = plt.subplot(1, 2, 2)
gra2.set_title("Gráfico Seno")
gra2.set_xlabel("Eixo de Tempo")
gra2.set_xlabel("Eixo da Amplitude")
plt.plot(x, s)
plt.grid()
plt.show()