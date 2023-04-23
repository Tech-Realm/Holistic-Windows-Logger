import psutil
import datetime

def log_running_apps():
    # Get a list of all running processes
    processes = psutil.process_iter()
    
    # Log the current time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"--- {current_time} ---"
    print(log_line)
    
    # Loop through the processes and log their names and start times
    for process in processes:
        try:
            name = process.name()
            start_time = process.create_time()
            start_time_str = datetime.datetime.fromtimestamp(start_time).strftime('%Y-%m-%d %H:%M:%S')
            log_line = f"{name} started at {start_time_str}"
            print(log_line)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Log the running apps every 10 seconds
while True:
    log_running_apps()
    time.sleep(10)
