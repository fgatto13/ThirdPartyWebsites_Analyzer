from functions import *
from urllib.parse import urlparse

def main():
    fname = "all_flows.har"
    
    tpws = get_top_25()  # dataframe containing third party websites
    if tpws.empty:
        print("Error while reading the file")
    else:
        reqs = get_dict(fname=fname)
        if not reqs:
            print("Something went wrong")
        else:
            entries = reqs["log"]["entries"]
            urls = pd.DataFrame({"url": [entry["request"]["url"] for entry in entries]})
            urls["domain"] = urls["url"].apply(
                lambda u: urlparse(u).hostname if urlparse(u).hostname else None
            )
            urls = urls.drop(columns=["url"])

            tracker_list = [s.lower() for s in tpws]

            urls = urls[urls["domain"].str.lower().apply(
                lambda host: any(tracker in host for tracker in tracker_list)
            )]

            urls["core"] = urls["domain"].apply(
                lambda h: get_core_domain(h)
            )

            counted_ws = urls["core"].value_counts()
            
            create_chart(counts=counted_ws)
            

if __name__ == "__main__":
    main()