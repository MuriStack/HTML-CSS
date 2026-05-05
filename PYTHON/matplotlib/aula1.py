import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 501)
print(t)
y = np.cos(4*t)

plt.plot(t,y)
plt.title("Gráfico do Cosseno")
plt.xlabel("Rad")
plt.ylabel("Amplitude")
plt.show()