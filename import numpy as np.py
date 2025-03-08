import numpy as np
import matplotlib.pyplot as plt

# x 값 설정
x1 = np.linspace(0.01, 5, 400)  # y = x^e의 유효 범위 (x > 0)
x2 = np.linspace(-2, 5, 400)  # y = e^x의 유효 범위 (모든 실수)

# y 값 계산
y1 = x1**np.e  # y = x^e
y2 = np.exp(x2)  # y = e^x

# 그래프 그리기
plt.figure(figsize=(8, 6))
plt.plot(x1, y1, label=r'$y = x^e$', color='b')
plt.plot(x2, y2, label=r'$y = e^x$', color='r', linestyle='dashed')

# 축 및 스타일 설정
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Comparison of $y = x^e$ and $y = e^x$')
plt.legend()
plt.show()
