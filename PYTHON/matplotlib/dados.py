import matplotlib.pyplot as plt
import pandas as pd

# fig = plt.figure(figsize=(12,8))

dados = pd.read_csv("dados.csv")
dias = dados['Date']
petro = dados['PETR4']
itau = dados['ITUB4']
variacao_petro = petro.diff()
variacao_itau = itau.diff()
media_petro = petro.diff().mean()
media_itau = itau.diff().mean()

# plt.plot(dias, petro, label='Petro', 
# color='green', linestyle='--', marker='.')

# plt.plot(dias, itau, label='Itaú', 
# color='orange', linestyle='--', marker='.')

# plt.title('Cotação - 2025/1')
# plt.xlabel('Dias')
# plt.ylabel('Valor da ação (R$)')
# plt.legend()
# plt.xticks(ticks=dias[::20])

# plt.show()

# fig = plt.figure(figsize=(12,8))
# plt.hist(variacao_petro, label='Petro', 
#     color='green', alpha=0.5, bins=50)

# plt.axvline(media_petro, color='green', linestyle='--', lw=4)
# plt.axvline(media_itau, color='orange', linestyle='--', lw=4)

# plt.hist(variacao_itau, label='Itau',
#     color='orange',alpha=0.5, bins=50)

# plt.title('Variação diária - 2025/1')
# plt.xlabel('Variação (R$)')
# plt.ylabel('Frequência')
# plt.legend()
# plt.show()

# plt.style.use('dark_background')
# fig, (ax_cima, ax_baixo) = plt.subplots(figsize=(12,8), nrows = 2, sharex=True)

# ax_cima.hist(variacao_petro, label='Petro',color='green', 
#         bins=50)
# ax_cima.axvline(media_petro, color='gray', 
#         linestyle='--', lw=4)
# ax_cima.set_xlabel('Variação (R$)')
# ax_cima.set_ylabel('Frequência')
# ax_cima.grid(True)

# ax_baixo.hist(variacao_itau,label='Itaú', color='orange', 
#         bins=50)
# ax_baixo.axvline(media_itau, color='gray', 
#         linestyle='--', lw=4)
# ax_baixo.set_xlabel('Variação (R$)')
# ax_baixo.set_ylabel('Frequência')
# ax_baixo.grid(True)

# fig.suptitle('Variação diária - 2025/1')
# plt.legend()
# plt.show()

plt.style.use('dark_background')
fig = plt.figure(figsize=(12,8))

grid = fig.add_gridspec(2,2)

ax_linha = fig.add_subplot(grid[0,:])
ax_hist_1 = fig.add_subplot(grid[1,0])
ax_hist_2 = fig.add_subplot(grid[1,1])

ax_linha.grid(True)


ax_linha.plot(dias, petro, label='Petro', 
color='green', linestyle='--', marker='.')

ax_linha.plot(dias, itau, label='Itaú', 
color='orange', linestyle='--', marker='.')

ax_linha.set_title('Cotação - 2025/1')
ax_linha.set_xlabel('Dias')
ax_linha.set_ylabel('Valor da ação (R$)')
ax_linha.set_xticks(ticks=dias[::20]) 

ax_hist_1.hist(variacao_petro,color='green', 
        bins=50)
ax_hist_1.axvline(media_petro, color='gray', 
        linestyle='--', lw=4)
ax_hist_1.set_xlabel('Variação (R$)')
ax_hist_1.set_ylabel('Frequência')
ax_hist_1.grid(True)

ax_hist_2.hist(variacao_itau, color='orange', 
        bins=50)
ax_hist_2.axvline(media_itau, color='gray', 
        linestyle='--', lw=4)
ax_hist_2.set_xlabel('Variação (R$)')
ax_hist_2.set_ylabel('Frequência')
ax_hist_2.grid(True)

fig.suptitle('Análise de ações')
fig.legend()
fig.tight_layout()

fig.savefig('figura.png')

plt.show()