from traffic_data import generate_live_traffic
from congestion import detect_congestion
from optimizer import *
import matplotlib.pyplot as plt
import time

# Store Past Traffic
time_data = []
deptA_data = []

current_time = 0

plt.ion()

fig, ax = plt.subplots(figsize=(10,6))

while current_time < 20:

    deptA, deptB, deptC = generate_live_traffic()

    LINK_CAPACITY = 100

    utilization = (deptA / LINK_CAPACITY) * 100 

    print(f"Link Utilization = {utilization:.2f}%")

    time_data.append(current_time)
    deptA_data.append(deptA)


    status = detect_congestion(deptA)



    optimal_bandwidth, iterations = newton_raphson(10)

  
    print(f"\nTime = {current_time}")
    print(f"Dept A Traffic = {deptA} Mbps")
    print(status)
    print(f"Optimal Bandwidth = {optimal_bandwidth:.2f} Mbps")

    packet_loss = 0

    if utilization > 90:
        packet_loss = utilization - 90

    print(f"Estimated Packet Loss = {packet_loss:.2f}%")

    ax.clear()

    ax.plot(time_data,
            deptA_data,
            marker='o',
            label='Dept A Traffic')

    ax.set_xlabel("Time")
    ax.set_ylabel("Traffic (Mbps)")
    ax.set_title("Real-Time Network Traffic Monitoring")

    ax.legend()
    ax.grid(True)

    plt.pause(1)

    current_time += 1

plt.ioff()
plt.show()