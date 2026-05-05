def simular_queda_livre(s0, v0, ac, dt): 
    t = 0
    while s0 >= 0: 
        if s0 <= 50:
            ac = 1.62
        v = v0 + ac * dt 
        s = s0 + v * dt 
        print(f"No momento: {t:.1f}, estou com velocidade: {v:.2f} e na posição: {s:.2f}") 
        v0 = v 
        s0 = s
        t += dt

simular_queda_livre(100, 0, -9.8, 0.001) 