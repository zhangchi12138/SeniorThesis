import sympy as sym
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt
import math as math
import csv as csv
import pandas as pd


##################################################
# circular
##################################################

#osc averaging 4 frames
#rep 700, current = .12, with compensation coils
dvr = [52,52,52,52.8,52.8,53.6,53.6,53.6,53.6,53.6,53.6,53.8,53.6]
dvr = np.array(dvr)
powerr = 1.78

effr = dvr/powerr
reperr = [abs(effr[i]) * np.sqrt((.2/dvr[i])**2 + (.03/powerr)**2) for i in range(0,len(effr))]

# cont
dvc = [56.8,56.8,56.8,65.6,67.2,71.2,73.6,76,78.4,81.6,82.4,83.2,84]
dvc = np.array(dvc)
powerc = 4.1

effc = dvc / powerc
conerr = [abs(effc[i]) * np.sqrt((.2/dvc[i])**2 + (.03/powerc)**2) for i in range(0,len(effc))]

angler = [90,85,80,45,40,35,30,25,20,15,10,5,0]
anglec = [90,85,80,45,40,35,30,25,20,15,10,5,0]

plt.figure()
plt.errorbar(anglec, effc, yerr = conerr,label= 'Continuous Circular', fmt = '.')
plt.errorbar(angler, effr,yerr = reperr, label = '700 kHz Circular', fmt = '.')

##################################################
# linear
##################################################

angles = [0,5,10,15,20,25,30,35,40,45,50,80,85,90]

dvr = [44.8,44.8,45.0,45.4,45.6,45.6,45.8,45.6,45.6,45.8,46.0,46.2,46.2,46.4]
powerr = 1.7 
dvr = np.array(dvr)
effr = dvr/powerr
effrerror = [abs(effr[i]) * np.sqrt((.1/dvr[i])**2 + (.05/powerr)**2) for i in range(0,len(effr))]


dvc = [88.3,88.5,88.6,88.8,89.2,89.4,89.8,91.0,91.2,91.6,92.0,92.6,93.0,93.6]
powerc = 3.7
dvc = np.array(dvc)
effc = dvc/powerc
effcerror = [abs(effc[i]) * np.sqrt((.1/dvc[i])**2 + (.05/powerc)**2) for i in range(0,len(effc))]

plt.errorbar(angles,effr,yerr = effrerror,label = '700 kHz Linear', fmt = '.')
plt.errorbar(angles,effc,yerr = effcerror,label = 'Continuous Linear', fmt = '.')


plt.xlabel('Angle (degrees)')
plt.ylabel('Return Effeciency (dv/W)')
plt.grid(True)
plt.legend()
plt.savefig('together.pdf')
plt.show()

