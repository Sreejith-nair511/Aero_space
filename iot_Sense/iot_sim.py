import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from collections import deque

# ---- Parameters ----
max_len = 50  # number of points to show in live graph

# ---- Data storage ----
engine_temp_data = deque([0]*max_len, maxlen=max_len)
vibration_data = deque([0]*max_len, maxlen=max_len)
time_data = deque([i for i in range(max_len)], maxlen=max_len)

# ---- Figure setup ----
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6))
fig.suptitle("Live Aircraft Sensor Simulation")

# Temperature plot
line1, = ax1.plot(time_data, engine_temp_data, color='red')
ax1.set_ylim(200, 600)
ax1.set_ylabel("Engine Temp (°C)")
ax1.set_xlabel("Time Steps")

# Vibration plot
line2, = ax2.plot(time_data, vibration_data, color='blue')
ax2.set_ylim(0, 5)
ax2.set_ylabel("Vibration (g)")
ax2.set_xlabel("Time Steps")

# ---- Update function for animation ----
def update(frame):
    # Simulate new sensor readings
    new_temp = random.randint(200, 500)
    new_vib = round(random.uniform(0, 5), 2)

    # Append new data
    engine_temp_data.append(new_temp)
    vibration_data.append(new_vib)

    # Update plots
    line1.set_ydata(engine_temp_data)
    line2.set_ydata(vibration_data)
    
    return line1, line2

# ---- Animate ----
ani = animation.FuncAnimation(fig, update, interval=500)

plt.tight_layout()
plt.show()
