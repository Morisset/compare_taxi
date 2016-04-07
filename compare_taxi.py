#!/usr/bin/python

import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) == 1:
    km_0 = input('Cuantos kilometros: ')
else:
    try:
        km_0 = np.float(sys.argv[1])
    except:
        raise Exception('Argument must be a number')

U_fix = 7.0
U_km = 3.10
U_t = 1.80

T_fix = 8.74
T_km = 4.28
T_t = 1.43

S_fix = 13.10
S_km = 5.20
S_t = 1.74

R_fix = 27.30
R_km = 7.36
R_t = 2.46

v = np.linspace(5, 50, 100)

km = np.ones_like(v) * km_0
t = km * 60 / v

U_precio = U_fix + km * U_km + t * U_t
T_precio = T_fix + np.maximum(km * T_km, t * T_t)
S_precio = S_fix + np.maximum(km * S_km, t * S_t)
R_precio = R_fix + np.maximum(km * R_km, t * R_t)

f, ax = plt.subplots(figsize=(7,7))

ax.plot(t, T_precio, label='CDMX')
ax.plot(t, T_precio*1.2, label='CDMX Noche')
ax.plot(t, S_precio, label='CDMX Sitio')
ax.plot(t, U_precio, label='Uber', linestyle='--')
ax.plot(t, R_precio, label='CDMX Radio')
ax.plot(t, U_precio*1.5, label='Uber Pico (+50%)', linestyle='--')
ax.plot(t, U_precio*2.0, label='Uber Pico (+100%)', linestyle='--')

ax.legend(loc='best')
ax.set_xlabel('T (min)')
ax.set_ylabel('Precios (MXN)')
ax.set_title('Precios para {:.0f} km'.format(km_0))
plt.show()
