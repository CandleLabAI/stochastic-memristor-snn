import matplotlib
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import lognorm

matplotlib.rcParams.update({'font.size': 12})
matplotlib.rcParams["font.family"] = "Times New Roman"

figure(figsize=(4,3))

reset_resistances = []
with open("fig6.txt", "r") as file:
    for line in file:
        resistance = float(line.strip())
        reset_resistances.append(resistance)



mean = 40645535.40735991
stdev = 14548220.917068811
phi = (stdev ** 2 + mean ** 2) ** 0.5
mu = np.log(mean ** 2 / phi)
sigma = (np.log(phi ** 2 / mean ** 2)) ** 0.5
plt.hist(reset_resistances, bins=30, density=True, alpha=0.5, color='b')
# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 1000)
p = lognorm.pdf(x = x, scale = mean, s = sigma)
plt.plot(x, p, 'r', linewidth=2)
plt.xscale('log')
plt.xlabel(f'HRS($\Omega$)')
# plt.savefig("log_normal_fit.pdf", transparent=True, dpi=300, bbox_inches='tight')
plt.show()