import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi,301)
y_cos = np.cos(t*4)
y_sin = np.sin(t*4)

plt.figure("Gráfico")
plt.title("Gráficos do Seno e Cosseno")
plt.xlabel("Eixo de Tempo")
plt.ylabel("Eixo da Amplitude")
plt.plot(t,y_cos)
plt.plot(t,y_sin)
plt.grid()
plt.show()