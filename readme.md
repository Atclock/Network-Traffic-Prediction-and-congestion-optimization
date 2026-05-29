# Network Traffic Prediction and Congestion Optimization Using Numerical Methods

## Overview

This project presents an enterprise network traffic prediction and congestion optimization system developed for the BM371 Numerical Methods course. The system integrates networking concepts with numerical analysis techniques to simulate, analyze, predict, and optimize enterprise network traffic behavior.

The project combines:

* Enterprise network design using VLAN segmentation
* Real-time traffic simulation
* Numerical methods for traffic prediction and optimization
* Congestion detection and performance analysis
* Python-based analytical modeling
* Cisco Packet Tracer network simulation

---

# Features

## Networking Features

* VLAN segmentation
* Inter-VLAN routing
* Router-on-a-stick configuration
* Enterprise-style topology
* Multi-department network simulation

## Numerical Methods Features

* Newton Divided Difference Interpolation
* Newton-Raphson Optimization
* Traffic forecasting
* Delay minimization
* Convergence analysis

## Simulation Features

* Real-time traffic generation
* Dynamic congestion detection
* Bandwidth utilization analysis
* Packet loss estimation
* Traffic visualization

---

# Technologies Used

## Networking

* Cisco Packet Tracer

## Programming

* Python 3

## Python Libraries

* NumPy
* Matplotlib

---

# Enterprise Network Topology

```text
                      INTERNET
                          |
                    [ Main Router ]
                          |
                    [ Core Switch ]
             _____________|_____________
            |             |             |
        Dept A         Dept B        Dept C
      Access SW      Access SW      Access SW
        /   \           /  \          /   \
      PCs  Server     PCs PCs      PCs  PCs
```

---

# VLAN Design

| Department   | VLAN | Subnet          |
| ------------ | ---- | --------------- |
| Department A | 10   | 192.168.10.0/24 |
| Department B | 20   | 192.168.20.0/24 |
| Department C | 30   | 192.168.30.0/24 |

---

# Numerical Methods

## Newton Interpolation

Used to predict future network traffic values based on historical traffic measurements.

### Example

[
P(x)=f[x_0]+f[x_0,x_1](x-x_0)+...
]

---

## Newton-Raphson Optimization

Used to minimize the network delay function and determine optimal bandwidth allocation.

### Delay Function

[
D(x)=\frac{100}{x}+0.5x
]

---

# Project Structure

```text
network_project/
│
├── main.py
├── traffic_data.py
├── interpolation.py
├── optimizer.py
├── congestion.py
│
├── graphs/
│
├── packet_tracer/
│
└── report/
```

---

# How to Run

## 1. Install Required Libraries

```bash
pip install numpy matplotlib
```

---

## 2. Run the Project

```bash
python main.py
```

---

# Example Output

```text
Predicted Dept A Traffic at 15:00 = 125 Mbps
Critical Congestion
Optimal Bandwidth = 14.14 Mbps
```

---

# Generated Graphs

The project generates several analytical graphs:

* Department Traffic Prediction
* Multi-Department Traffic Comparison
* Delay Optimization Curve
* Real-Time Traffic Monitoring
* Newton-Raphson Convergence Analysis

---

# Real-Time Simulation

The system dynamically generates:

* VoIP traffic
* Streaming traffic
* Web browsing traffic
* File transfer traffic

This simulates realistic enterprise network conditions.

---

# Engineering Significance

This project demonstrates how numerical methods can be applied in networking environments to:

* Predict congestion
* Improve bandwidth allocation
* Reduce network delay
* Analyze traffic behavior
* Optimize enterprise network performance

---

# Future Improvements

* Machine learning-based prediction
* QoS implementation
* GUI dashboard
* Deployment on physical hardware
* Advanced routing protocols

---

# Course Information

**Course:** BM371 – Numerical Methods

**Project Type:** Networking Application Using Numerical Methods

---

# Authors

Developed as part of the BM371 Numerical Methods course project.
