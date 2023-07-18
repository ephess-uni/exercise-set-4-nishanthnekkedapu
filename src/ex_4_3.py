""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    events = get_shutdown_events(logfile)
    shutdown_event_1 = events[0]
    shutdown_event_2 = events[-1]
    event_1_time = logstamp_to_datetime(shutdown_event_1.split()[1])
    event_2_time = logstamp_to_datetime(shutdown_event_2.split()[1])
    delta_time_object = event_2_time-event_1_time
    return delta_time_object


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
