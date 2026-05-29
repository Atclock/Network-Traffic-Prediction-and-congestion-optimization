import random
    # Each department has different traffic patterns, I made it so that it is random but each department has a different
    # range, this is to simulate how heavy each department's traffic is.
def generate_live_traffic():

    # Different traffic going through the network
    voip = random.randint(5, 20)
    web = random.randint(10, 40)
    streaming = random.randint(20, 60)
    file_transfer = random.randint(10, 50)

    deptA = voip + web + streaming + file_transfer # Heavy traffic department

    deptB = random.randint(20, 70) # Moderate traffic department

    deptC = random.randint(10, 60) # Light traffic department

    return deptA, deptB, deptC