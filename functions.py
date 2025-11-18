import pandas as pd
import json
import matplotlib.pyplot as plt

# function to load the stack of requests obtained from mitmproxy
def get_dict(fname: str) -> dict | None:
    try:
        with open(file=fname, mode="r") as file:
            content = json.load(file)
        return content
    except FileNotFoundError:
        print("Unable to locate file")
        return None
    except PermissionError:
        print("You don't have permission to access the file")
        return None

# function to load the top 25 trackers into a Pandas DataFrame
def get_top_25() -> pd.DataFrame | None:
    sites = pd.DataFrame()
    sites = pd.read_csv("top_25_trackers.csv")
    sites = sites["tracker_name"]
    return sites

# function to normalize the domains
def get_core_domain(hostname: str) -> str | None:
    if not hostname:
        return None

    ignore = {"com", "safeframe"}   # to reduce noise when filtering the domains
    labels = [label.lower() for label in hostname.split(".") if label.lower() not in ignore]

    if not labels:
        return None

    # the core domain is the rightmost meaningful label
    return labels[-1]

# function to plot the graph
def create_chart(counts: pd.DataFrame):
    # plotting the chart
    plt.barh(counts.index, counts.values)

    plt.title("Third party websites reached distribution")
    plt.xlabel("Number of calls")
    plt.ylabel("Third party websites")

    plt.tight_layout()
    plt.show()