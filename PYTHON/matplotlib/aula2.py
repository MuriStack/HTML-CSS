import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 501)
print(t)
y_cos = np.cos(4*t)
y_sin = np.sin(4*t)
y_tan = np.tan(4*t)

plt.figure(1)
plt.plot(t,y_cos)
plt.title("Gráfico do Cosseno")
plt.xlabel("Rad")
plt.ylabel("Amplitude")
plt.figure(2)
plt.plot(t,y_sin)
plt.title("Gráfico do Seno")
plt.xlabel("Rad")
plt.ylabel("Amplitude")
plt.figure(3)
plt.plot(t,y_tan)
plt.title("Gráfico do Tangente")
plt.xlabel("Rad")
plt.ylabel("Amplitude")
plt.show()


plt.show()

plt.show()