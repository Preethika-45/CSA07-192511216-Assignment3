# CSA07 – Assignment 3 (CO3)

**Student Name:** Preethika M  
**Register Number:** 192511216  
**Course:** Computer Networks  
**Assignment:** Assignment 3 – CO3

## Project Description

This repository contains the Python programs and practical work completed for CSA07 – Computer Networks Assignment 3 (CO3).

## Folder Structure

- **Task01** – TCP and UDP Socket Programming
- **Task02** – TCP Tahoe and Reno Congestion Window Simulation
- **Task03** – HTTP Page Loading Time Calculations
- **Task04** – DNS Iterative Resolution and Caching
- **Task05** – M/M/1 Queueing Model and QoS
- **Task06** – TCP, TLS and QUIC Handshake Timing
- **Task07** – Reliable File Transfer and TCP Chat Application

## Technologies Used

- Python
- TCP and UDP
- HTTP and HTTPS
- DNS
- Wireshark
- Computer Networks Concepts

## Requirements

- Python 3
- Matplotlib (for generating graphs)
- Wireshark (for packet analysis)

## Installation

Install Matplotlib using:

```bash
python -m pip install matplotlib
```

## How to Run the Programs

Run the following commands from the repository folder:

```bash
python Task01/socket_demo.py
python Task02/congestion_sim.py
python Task03/http_timing.py
python Task04/dns_iterative.py
python Task05/mm1_qos.py
python Task06/handshake_timing.py
```

### Task07 – File Transfer

First terminal:

```bash
python Task07/file_server.py
```

Second terminal:

```bash
python Task07/file_client.py
```

### Task07 – Chat Application

First terminal:

```bash
python Task07/chat_demo.py server
```

Second terminal:

```bash
python Task07/chat_demo.py client
```

## Practical Evidence

The following evidence will be added after running the experiments:

- Python program outputs
- Wireshark packet captures
- TCP and UDP communication screenshots
- Congestion window graphs
- HTTP page loading measurements
- DNS lookup results
- Queueing delay graphs
- TLS handshake analysis
- File transfer and SHA-256 verification results

## Conclusion

This assignment demonstrates the practical implementation and analysis of various computer networking concepts, including transport-layer protocols, congestion control, HTTP performance, DNS resolution, queueing models, secure communication and reliable data transfer.

**Note:** All experimental screenshots, packet captures and measurements should be generated from actual execution of the programs and tools.
