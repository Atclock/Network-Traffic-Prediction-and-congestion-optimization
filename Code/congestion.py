def detect_congestion(traffic):

    #This is to simulate how the congestion detection would work, I set thresholds for different levels of congestion based on the traffic.

    if traffic < 70:
        return "Traffic Normal"

    elif traffic < 100:
        return "Moderate Congestion"

    else:
        return "Critical Congestion"