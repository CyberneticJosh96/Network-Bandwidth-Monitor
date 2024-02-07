# Network-Bandwidth-Monitor

## Objective

Develop a Python script to monitor real-time network bandwidth usage. The script will gather data on upload and download speeds, present it in a user-friendly format, and provide insights for optimizing network performance. Additional features may include setting threshold alerts and generating historical reports.

### Skills Learned


- Proficiency in Python programming, including data manipulation and networking libraries.
- Understanding of network traffic monitoring principles and techniques.
- Ability to collect and analyze real-time data on upload and download speeds.
- Experience in creating user-friendly interfaces, such as graphical dashboards or command-line interfaces.
- Knowledge of implementing advanced features like threshold alerts and historical reporting for enhanced network management.
- Proficiency in analyzing and interpreting network logs.
- Ability to generate and recognize attack signatures and patterns.
- Enhanced knowledge of network protocols and security vulnerabilities.
- Development of critical thinking and problem-solving skills in cybersecurity.

### Tools Used

- Python: Leveraged for scripting and application development due to its versatility and extensive libraries for networking and data manipulation.
- Requests Library: Utilized for making HTTP requests to fetch network data from APIs or websites.
- Matplotlib or Plotly: Employed for creating graphical representations of network bandwidth data, facilitating visualization and analysis.
- Pandas: Utilized for data manipulation and analysis, enabling efficient handling of network traffic data.
- Network monitoring tools (e.g., Wireshark, tcpdump): Used for capturing and analyzing network packets, aiding in understanding network behavior and troubleshooting.

## Steps
1. ![NBW PIC #1](https://github.com/CyberneticJosh96/Network-Bandwidth-Monitor/assets/146404458/8e29c6df-1926-4ca0-a546-5a271b0956ec)
    - This section includes the necessary library imports for this project. psutil is used for accessing system information, time is employed for introducing sleep duration, and         matplotlib.pyplot is imported for creating visualizations.

2. ![nbw pic#2](https://github.com/CyberneticJosh96/Network-Bandwidth-Monitor/assets/146404458/251ff3a0-32e1-45a7-bcb6-27bdfc8d315d)
   
    - In this section, two essential functions handle the network bandwidth. The get_bandwidth() function utilizes psutil to retrieve the current count of bytes sent and received,       providing a snapshot of the network I/O. The calculate_bandwidth() function takes the initial and final byte values, along with the elapsed time, to compute the speed of           data transfer, both for sent and received data. These functions form the core functionality of the network monitoring aspect.

3. ![NBW pic #3](https://github.com/CyberneticJosh96/Network-Bandwidth-Monitor/assets/146404458/29dfe9e0-31a1-4e50-8f88-1bb076f9e3cb)

    - The plot_bandwidth() function employs Matplotlib to generate a bar chart. It uses labels, colors, and a title to create a visual representation of the network bandwidth,           distinguishing between sent and received data.
  
4. ![NBW PIC #4](https://github.com/CyberneticJosh96/Network-Bandwidth-Monitor/assets/146404458/bf64b230-11dd-4982-8851-7ed77871e08b)
     - The main() function orchestrates the script execution. It sets up a configuration option (sleep_duration) for the sleep interval, collects initial and final network                statistics, calculates the network speeds, prints the results to the console, and calls the visualization function to display a bar chart.
  
5. ![NBW pic #5](https://github.com/CyberneticJosh96/Network-Bandwidth-Monitor/assets/146404458/4bd50e14-a458-4049-9663-c0424e15be74)
     - This conditional statement ensures that the main() function is executed only when the script is run directly, preventing unintended execution when imported as a module. It         concludes the script, making it modular and reusable.




