## Calculating the mean response time of the ping

import subprocess
import re


def get_response_time(target):
    # Execute ping command
    ping = subprocess.Popen(["ping", "-c", "1", target], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Capture output and wait for command to finish
    output, error = ping.communicate()
    output = output.decode("utf-8")

    # Extract response time from output using regular expression
    match = re.search(r"time=(\d+\.\d+) ms", output)
    if match:
        return float(match.group(1))
    else:
        return None



def calculate_mean_response_time(target, num_packets):
    # List to hold response times for each packet
    response_times = []

    # Send packets and record response times
    for i in range(num_packets):
        response_times.append(get_response_time(target))

    # Calculate mean response time
    return sum(response_times) / len(response_times)




# Targets hosts
targets = ["8.8.8.8", "134.96.216.1", "58.247.214.47", "49.12.165.88"]
# Number of packets to send
num_packets = 5


print("TARGET\t\t\tMEAN RESPONSE TIME")
for target in targets:
    mean_response_time = calculate_mean_response_time(target, num_packets)
    print(f"{target}\t\t\t{mean_response_time:.2f}")
print()

