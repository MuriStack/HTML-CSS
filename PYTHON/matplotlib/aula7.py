import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 71)
y = np.cos(4*x)

plt.figure(figsize=(8,4))
plt.plot(x,y, color="g", lw=1.5, marker="o", 
         linestyle="dashed")
plt.grid(True)
plt.title("Gráfico do Cosseno")
plt.xlabel("Eixo do Tempo")
plt.ylabel("Eixo da Amplitude")
plt.show()
