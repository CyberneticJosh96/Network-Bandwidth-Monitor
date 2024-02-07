import psutil
import time
import matplotlib.pyplot as plt

def get_bandwidth():
    net_io = psutil.net_io_counters()
    return net_io.bytes_sent, net_io.bytes_recv

def calculate_bandwidth(bytes_sent_start, bytes_recv_start, bytes_sent_end, bytes_recv_end, elapsed_time):
    sent_speed = (bytes_sent_end - bytes_sent_start) / elapsed_time
    recv_speed = (bytes_recv_end - bytes_recv_start) / elapsed_time
    return sent_speed, recv_speed

def plot_bandwidth(sent_speed, recv_speed):
    labels = ['Sent', 'Received']
    speeds = [sent_speed, recv_speed]

    plt.bar(labels, speeds, color=['blue', 'green'])
    plt.ylabel('Bytes/s')
    plt.title('Network Bandwidth')
    plt.show()

def main():
    # Configuration Option: Sleep duration in seconds
    sleep_duration = 1

    bytes_sent_start, bytes_recv_start = get_bandwidth()
    
    # Sleep for the specified duration
    time.sleep(sleep_duration)

    bytes_sent_end, bytes_recv_end = get_bandwidth()

    elapsed_time = sleep_duration

    sent_speed, recv_speed = calculate_bandwidth(
        bytes_sent_start, bytes_recv_start, bytes_sent_end, bytes_recv_end, elapsed_time
    )

    print(f"Sent Speed: {sent_speed} bytes/s")
    print(f"Receive Speed: {recv_speed} bytes/s")

    # Visualization
    plot_bandwidth(sent_speed, recv_speed)

if __name__ == "__main__":
    main()

