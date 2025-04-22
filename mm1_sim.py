import sys
import math
import random

# Constants
Q_LIMIT = 100  # Queue limit
BUSY = 1       # Server is busy
IDLE = 0       # Server is idle

# Global variables
num_custs_delayed = 0
num_delays_required = 0
num_in_q = 0
server_status = IDLE

time_last_event = 0.0
sim_time = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_next_event = [0.0, 0.0, 1.0e+30]  # Event list (index 0 unused)

total_of_delays = 0.0
area_num_in_q = 0.0
area_server_status = 0.0

mean_interarrival = 0.0
mean_service = 0.0


def initialize():
    global sim_time, server_status, num_in_q, time_last_event
    global num_custs_delayed, total_of_delays, area_num_in_q, area_server_status
    global time_next_event

    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0

    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0

    # First arrival event
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30  # No departure yet


def timing():
    global sim_time, next_event_type

    min_time_next_event = min(time_next_event[1:3])
    next_event_type = time_next_event.index(min_time_next_event)

    if next_event_type == 0:
        with open("mm1.out", "w") as outfile:
            outfile.write(f"\nEvent list empty at time {sim_time}\n")
        sys.exit(1)

    sim_time = min_time_next_event


def arrive():
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event

    time_next_event[1] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            with open("mm1.out", "w") as outfile:
                outfile.write(f"\nQueue overflow at time {sim_time}\n")
            sys.exit(2)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)


def depart():
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event

    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        num_in_q -= 1
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)

        # Shift queue
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]


def report():
    with open("mm1.out", "w") as outfile:
        outfile.write("\nSingle-server queueing system\n\n")
        outfile.write(f"Mean interarrival time {mean_interarrival:11.3f} minutes\n")
        outfile.write(f"Mean service time {mean_service:16.3f} minutes\n")
        outfile.write(f"Number of customers {num_delays_required:14d}\n\n")
        outfile.write(f"Average delay in queue {total_of_delays / num_custs_delayed:11.3f} minutes\n")
        outfile.write(f"Average number in queue {area_num_in_q / sim_time:10.3f}\n")
        outfile.write(f"Server utilization {area_server_status / sim_time:15.3f}\n")
        outfile.write(f"Time simulation ended {sim_time:12.3f} minutes\n")


def update_time_avg_stats():
    global area_num_in_q, area_server_status, time_last_event

    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time

    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event


def expon(mean):
    return -mean * math.log(random.random())


def main():
    global mean_interarrival, mean_service, num_delays_required

    # Read input values
    with open("mm1.in", "r") as infile:
        mean_interarrival, mean_service, num_delays_required = map(float, infile.readline().split())
        num_delays_required = int(num_delays_required)

    # Initialize simulation
    initialize()

    # Run simulation until required number of customers are served
    while num_custs_delayed < num_delays_required:
        timing()
        update_time_avg_stats()
        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()

    # Generate report
    report()


if __name__ == "__main__":
    main()
