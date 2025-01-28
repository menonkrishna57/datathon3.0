import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Data to be updated
x_data, y_data = [], []

def update(frame):
    if frame == 0:
        x_data.clear()
        y_data.clear()
    x_data.append(frame)
    y_data.append(random.randint(0, 10))
    ax.cla()  # Clear axis
    ax.plot(x_data, y_data, label="Real-time data")
    ax.legend()

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, frames=range(100), interval=100, repeat=True)  # interval in ms
plt.show()
