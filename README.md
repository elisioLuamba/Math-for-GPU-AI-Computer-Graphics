# 📘 Math for GPU, AI & Computer Graphics

## 🚀 Visão Geral

Este repositório transforma matemática fundamental em implementações práticas para Computação Gráfica, Inteligência Artificial, GPU e Visão Computacional.

---

# 🧠 Conceito Central

MATEMÁTICA → FUNÇÃO → CÓDIGO → GPU / IA / VISÃO

---

# 📐 Álgebra Linear

## 🔹 Vetores

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(np.dot(a, b))
```

---

## 🔹 Produto Escalar (Dot Product)

```python
def dot(a, b):
    return sum(x*y for x, y in zip(a, b))
```

Aplicações:

* Similaridade em IA
* Iluminação em CG
* Projeções vetoriais

---

## 🔹 Produto Vetorial (Cross Product)

```python
import numpy as np

a = np.array([1, 0, 0])
 b = np.array([0, 1, 0])

print(np.cross(a, b))
```

Aplicações:

* Normais de superfícies
* Física 3D
* Renderização

---

# 🧱 Matrizes e Transformações

## 🔹 Transformação 2D

```python
import numpy as np

point = np.array([2, 3, 1])

T = np.array([
    [1, 0, 5],
    [0, 1, 2],
    [0, 0, 1]
])

print(T @ point)
```

Aplicações:

* Rotação
* Escala
* Translação

---

# 🌍 Coordenadas Homogêneas

Uso em pipelines gráficos:

* OpenGL
* Vulkan
* Ray Tracing

Forma:
(x, y, z, 1)

---

# 📏 Geometria Analítica

## 🔹 Distância Euclidiana

```python
import numpy as np

def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))
```

Aplicações:

* KNN
* Tracking (YOLO)
* Clustering

---

## 🔹 Reta Paramétrica

```python
def line(p0, d, t):
    return p0 + t * d
```

---

# ⚡ GPU Computing

## 🔹 Modelo Paralelo

Cada thread processa um elemento

```cpp
__global__ void add(float* a, float* b, float* c) {
    int i = threadIdx.x;
    c[i] = a[i] + b[i];
}
```

---

# 🤖 IA (Camada Linear)

## 🔹 Fórmula

y = Wx + b

```python
import numpy as np

x = np.array([1.0, 2.0])
W = np.array([[0.5, 0.2],
              [0.1, 0.7]])
b = np.array([0.1, 0.2])

y = W @ x + b
print(y)
```

---

# 👁️ Visão Computacional

```python
import cv2

img = cv2.imread("frame.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray)
cv2.waitKey(0)
```

---

# 🏗️ Estrutura do Projeto

```
math-for-gpu-ai/
│
├── linear_algebra/
│   ├── vectors.py
│   ├── matrices.py
│
├── geometry/
│   ├── lines.py
│   ├── intersections.py
│
├── gpu/
│   ├── cuda_kernels.cu
│
├── ai/
│   ├── neural_net.py
│
├── vision/
│   ├── opencv_basics.py
│   ├── yolo_demo.py
│
└── README.md
```

---

# 🔥 Objetivo Final

Transformar matemática em sistemas reais:

* IA
* GPU
* Visão computacional
* Computação gráfica
