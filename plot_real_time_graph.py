import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline 表示だとアニメーションしない
# %matplotlib

# 描画領域を取得
fig, ax = plt.subplots(1, 1)

# y軸方向の描画幅を指定
# ax.set_ylim((-1.1, 1.1))

# x軸:時刻
x = np.arange(0, 100, 0.5)

y = 5;
x = 0;

for i in np.arange(0, 1, 10):
  x = np.arange(0, 0.10, 0.01)
  y = np.arange(0, 10, 1)


while True:
  x = np.append(x, x[-1] + 0.01)
  y = np.append(y, y[-1] + 1)

  x = np.delete(x, 0, 0)
  y = np.delete(y, 0, 0)

  line, = ax.plot(x, y, color='blue')
  plt.xlim(x[0], x[-1])
  plt.ylim(y[0], y[-1])

  plt.pause(0.1)
  line.remove()



# # 周波数を高くしていく
# for Hz in np.arange(0.1, 10.1, 0.01):
#   # sin波を取得
#   y = np.sin(2.0 * np.pi * (x * Hz) / 100)
#   # グラフを描画する
#   line, = ax.plot(x, y, color='blue')
#   # 次の描画まで0.01秒待つ
#   plt.pause(0.01)
#   # グラフをクリア
#   line.remove()