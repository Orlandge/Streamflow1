import matplotlib.pyplot as plt
import numpy as np

def load_streamflow(filename):
    """Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    data_stream = np.genfromtxt(
        filename,
        delimiter=',',
        dtype=str,
        skip_header=1,
    )
    dates = data_stream[:, 0]
    flows = data_stream[:, 1:].astype(float)
    return dates, flows


def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW."""
    plt.figure(figsize=(12, 6))
    for column, site in enumerate(sites):
        plt.plot(dates, flows[:, column], label=f'Site {site}')

    plt.title('Provo River Streamflow Rates (June 2021)')
    plt.xlabel('Date')
    plt.ylabel('Streamflow (cfs)')
    plt.xticks(rotation=90)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
