import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.pyplot import figure
import numpy as np

matplotlib.rcParams.update({'font.size': 10})
matplotlib.rcParams["font.family"] = "Times New Roman"

temp = pd.read_csv('fig2.csv')


Voltage = []
Current = []

for i in range(len(temp)):
    Voltage.append(temp['Voltage'][i])
    Current.append(temp['Current'][i]*1000000)


figure(figsize=(4, 3))

plt.plot(Voltage, Current, linewidth=1.5, alpha=1)

# plt.yscale('log')
plt.xlim(-3.5, 3.5)
plt.ylim(-350, 250)
plt.xlabel(f'Voltage (V)')
plt.ylabel(f'Current ($\mu$A)')
# plt.savefig('i_v_stochastic.pdf', transparent=True, dpi=300, bbox_inches='tight')
plt.show()
