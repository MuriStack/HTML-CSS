import matplotlib.pyplot as plt

def simular_queda_livre(s0, v0, ac, dt): 
    t = 0

    tempos = []
    posicoes = []
    velocidades = []
    aceleracoes = []

    while s0 >= 0:
        tempos.append(t)
        posicoes.append(s0)
        velocidades.append(v0)
        aceleracoes.append(ac)

        ac = ac + 1 * dt
        v0 = v0 + ac * dt 
        s0 = s0 + v0 * dt
        t += dt

    posicoes[-1] = 0

    ############### GRÁFICOS ############
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))
    plt.suptitle("Gráficos queda livre", fontsize=16)

    axes[0].plot(tempos, posicoes, color='r', linewidth=2)
    axes[0].set_title("Gráfico de posição por tempo")
    axes[0].set_ylim(0, max(posicoes) * 1.1)
    axes[0].grid(True, linestyle='--')
    axes[0].legend(["Posição"])

    axes[1].plot(tempos, velocidades, color='b', linewidth=2)
    axes[1].set_title("Gráfico de velocidade por tempo")
    axes[1].grid(True, linestyle='--')
    axes[1].legend(["Velocidade"])

    axes[2].plot(tempos, aceleracoes, color='g', linewidth=2)
    axes[2].set_title("Gráfico de aceleração por tempo")
    axes[2].grid(True, linestyle='--')
    axes[2].legend(["Aceleração"])

    for ax in axes:
        ax.set_xlabel("Tempo (s)")

    plt.tight_layout()
    plt.show()

simular_queda_livre(100, 0, -9.8, 0.01)