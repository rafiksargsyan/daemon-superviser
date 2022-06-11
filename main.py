import argparse
import subprocess
import time

parser = argparse.ArgumentParser()
parser.add_argument("PROCESS_NAME", help="The process to supervise")
parser.add_argument("--restart-wait-time", type=int, default=3,
                    help="Seconds to wait between attempts to restart process")
parser.add_argument("--max-attempts", type=int, default=3,
                    help="Number of restart attempts before giving up")
parser.add_argument("--check-interval", type=int, default=5,
                    help="Process status check interval")
args = parser.parse_args()

process_name = args.PROCESS_NAME
restart_wait_time = args.restart_wait_time
max_attempts = args.max_attempts
check_interval = args.check_interval

attempts = 0
last_restart_time = 0
while True:
    if attempts > max_attempts:
        print("Max restart attempts reached, exiting supervisor...")
        exit(0)
    else:
        result = subprocess.run(["pgrep", process_name], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            print("Process with name " + str(process_name) + " is not running, checking last restart time...")
            current_time = time.time()
            time_since_last_restart = current_time - last_restart_time
            if time_since_last_restart > restart_wait_time:
                print("Enough seconds passed since last restart, restarting...")
                try:
                    subprocess.Popen(process_name)
                except FileNotFoundError:
                    print("Command with name " + str(process_name) + " not found, exiting...")
                    exit(1)
                attempts += 1
                last_restart_time = current_time
            else:
                print("Not enough seconds passed since last restart, will not try restarting!")
        else:
            print("Process with name " + process_name + " is running")
            attempts = 0
    print("Sleeping " + str(check_interval) + " seconds...")
    time.sleep(check_interval)
