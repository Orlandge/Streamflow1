import matplotlib.pyplot as plt
import numpy as np

data_stream = np.genfromtxt(
    'June-2021-Provo-River-Streamflow-Rates.csv',
    delimiter=',',
    dtype=str,
    skip_header=1,
)

x = data_stream[:, 0]
y_1 = data_stream[:, 1].astype(float)
y_2 = data_stream[:, 2].astype(float)
y_3 = data_stream[:, 3].astype(float)
y_4 = data_stream[:, 4].astype(float)
y_5 = data_stream[:, 5].astype(float)

plt.figure(figsize=(12, 6))
plt.plot(x, y_1, label='Site 10163000')
plt.plot(x, y_2, label='Site 10155200')
plt.plot(x, y_3, label='Site 10155500')
plt.plot(x, y_4, label='Site 10154200')
plt.plot(x, y_5, label='Site 10155000')

plt.title('Provo River Streamflow Rates (June 2021)')
plt.xlabel('Date')
plt.ylabel('Streamflow (cfs)')
plt.xticks(rotation=90)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
