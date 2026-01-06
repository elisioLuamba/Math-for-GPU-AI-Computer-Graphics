import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Configurações do sinal
fs = 100 # Frequência de amostragem (para a animação)
t_max = 2 # Duração total da simulação em segundos
t = np.arange(0, t_max, 1/fs)
sinal_analogico = 2.5 * (1 + np.sin(2 * np.pi * 1 * t)) # Sinal mais lento para visualização

# Configurações do ADC (ex: 3 bits)
bits_adc = 3
niveis = 2**bits_adc
degrau = 5.0 / (niveis - 1)

# Preparando o plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, t_max)
ax.set_ylim(0, 5.2)
ax.set_title(f"Simulação Animada do ADC ({bits_adc} bits)")
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Tensão (V)")
ax.grid(True, alpha=0.3)

line_analog, = ax.plot([], [], 'r--', label="Sinal Analógico", alpha=0.7)
line_digital, = ax.step([], [], 'b-o', where='post', label="Sinal Digital (Quantizado)", markersize=4) # Adicionado 'o' para pontos

# Função de inicialização da animação
def init():
    line_analog.set_data([], [])
    line_digital.set_data([], [])
    return line_analog, line_digital,

# Função que será chamada a cada frame
def animate(i):
    # Lógica para o quadro atual
    # Identação de 4 espaços
    t_atual = t[:i+1]
    sinal_analog_atual = sinal_analogico[:i+1]
    
    # Quantização do sinal
    sinal_digital_atual = np.round(sinal_analog_atual / degrau) * degrau
    
    line_analog.set_data(t_atual, sinal_analog_atual)
    line_digital.set_data(t_atual, sinal_digital_atual)
    
    return line_analog, line_digital,

# Criando a animação
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=50, blit=True)

# Salvar a animação como GIF (você pode postar direto no LinkedIn)
# ani.save('adc_animation.gif', writer='pillow', fps=20) 

plt.legend()
plt.show()