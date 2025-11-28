# Third Party Websites Analyzer

## Project Overview

The goal of this project is to analyze which third-party websites are contacted during normal user interactions on an iOS device, comparing them against the Ghostery **Top 25 Trackers** list.

## Setup

**Hardware & OS**
- **MacBook Air M2** — macOS 26.2 (Tahoe Beta 1)  
- **iPhone 14** — iOS 26

The MacBook was used to run **mitmproxy**, acting as an HTTP(S) proxy.  
A mitmproxy root certificate was installed on both devices to allow HTTPS traffic inspection.

## Data Collection

All network flows generated during typical app usage on the iPhone were routed through the MacBook’s proxy.  
The captured traffic was exported by mitmproxy in **HAR (HTTP Archive) JSON format**, which served as the dataset for analysis.

