# 📌 Ambiente básico: Matemática para GPU / IA / CG
# Apenas prints para entender as saídas

import numpy as np

print("=== VETORES ===")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("a:", a)
print("b:", b)
print("soma:", a + b)
print("subtração:", a - b)

print("\n=== PRODUTO ESCALAR ===")
dot = np.dot(a, b)
print("a · b =", dot)

print("\n=== PRODUTO VETORIAL ===")
cross = np.cross(a, b)
print("a x b =", cross)

print("\n=== MATRIZ TRANSFORMAÇÃO 2D ===")
point = np.array([2, 3, 1])

T = np.array([
    [1, 0, 5],
    [0, 1, 2],
    [0, 0, 1]
])

result = T @ point
print("ponto original:", point)
print("ponto transformado:", result)

print("\n=== DISTÂNCIA EUCLIDIANA ===")

p1 = np.array([0, 0])
p2 = np.array([3, 4])

distance = np.linalg.norm(p2 - p1)
print("p1:", p1)
print("p2:", p2)
print("distância:", distance)

print("\n=== IA: CAMADA LINEAR (Wx + b) ===")

x = np.array([1.0, 2.0])
W = np.array([
    [0.5, 0.2],
    [0.1, 0.7]
])
b = np.array([0.1, 0.2])

y = W @ x + b

print("x:", x)
print("W:\n", W)
print("b:", b)
print("y:", y)

print("\n=== FINAL ===")
print("Pipeline: Matemática → Código → IA / GPU / CG")
