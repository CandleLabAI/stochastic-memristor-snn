import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np

df1 = pd.read_csv('fig10_30meg.csv')
df2 = pd.read_csv('fig10_50meg.csv')


time1 = df1["time"] * 1000
membrane_voltage1 = df1["membrane_voltage"]
input_current1 = df1["input_current"] * 1000000

time2 = df2["time"] * 1000
membrane_voltage2 = df2["membrane_voltage"] 
input_current2 = df2["input_current"] * 1000000


figure(figsize=(4,3))
fig, ax1 = plt.subplots()

# color = 'blue'
ax1.set_xlabel(f'time (ms)')
ax1.set_ylabel(f'Voltage (V)')
ax1.plot(time1, membrane_voltage1, color='blue', label=f'R2=30 M$\Omega$')
ax1.plot(time2, membrane_voltage2, color='green', label=f'R2=50 M$\Omega$')

ax1.legend()
# plt.savefig("neuron_response.pdf", transparent=True, dpi=300, bbox_inches='tight')
plt.show()
