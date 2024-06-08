import psutil
import os
import time
import matplotlib.pyplot as plt

# Function to start the process
def start_process():
    # Replace 'your_script.py' with the name of your Python script
    process = psutil.Popen(['python', 'parse_docx.py'])
    return process.pid

# Function to monitor resource usage of the process and collect data
def monitor_process(pid, duration_ms):
    process = psutil.Process(pid)
    cpu_usage = []
    memory_usage = []
    start_time = time.time()
    while time.time() - start_time < duration_ms / 1000:  # Convert duration from milliseconds to seconds
        try:
            cpu_percent = process.cpu_percent()
            memory_percent = process.memory_percent()
            cpu_usage.append(cpu_percent)
            memory_usage.append(memory_percent)
        except psutil.NoSuchProcess:
            break  # Exit the loop if the process no longer exists
        time.sleep(0.001)  # Sleep for 1 millisecond
    return cpu_usage, memory_usage


# Example usage
pid = start_process()
duration_ms = 5000  # Duration of monitoring in milliseconds
cpu_usage, memory_usage = monitor_process(pid, duration_ms)

# Plotting the graph
time_points = [i * 0.001 for i in range(len(cpu_usage))]  # Convert index to time in seconds
plt.plot(time_points, cpu_usage, label='CPU Usage')
plt.plot(time_points, memory_usage, label='Memory Usage')
plt.xlabel('Time (s)')
plt.ylabel('Usage (%)')
plt.title('Resource Usage Over Time')
plt.legend()
plt.show()
