import csv

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


def summarize(dates, flows, sites):
    # Excel-equivalent check for 10163000: MAX = 131.0 cfs, AVERAGE = 56.9523611111 cfs.
    print(f"{'Gauge':<10}{'Max (cfs)':>10}   {'Date of max':<19}{'Min (cfs)':>10}{'Avg (cfs)':>10}")
    with open("streamflow_summary.csv", "w", newline="") as summary_file:
        writer = csv.writer(summary_file)
        writer.writerow(["Gauge", "Max (cfs)", "Date of max", "Min (cfs)", "Avg (cfs)"])

        for column, site in enumerate(sites):
            gauge_flows = flows[:, column]
            max_index = np.argmax(gauge_flows)
            maximum = float(np.max(gauge_flows))
            minimum = float(np.min(gauge_flows))
            average = float(np.mean(gauge_flows))
            date_of_max = dates[max_index]

            print(
                f"{site:<10}{maximum:10.1f}   {date_of_max:<19}"
                f"{minimum:10.1f}{average:10.1f}"
            )
            writer.writerow([site, maximum, date_of_max, minimum, average])


sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summarize(dates, flows, sites)

# Count readings strictly above the user's threshold; each 15-minute reading represents 0.25 hours.
threshold = float(input("Enter flow threshold (cfs): "))
for column, site in enumerate(sites):
    hours_above_threshold = np.sum(flows[:, column] > threshold) * 0.25
    print(f"Site {site}: {hours_above_threshold:.2f} hours above {threshold:g} cfs")

plot_streamflow(dates, flows, sites)
