# Daemon supervisor
A small python program that monitors another process and starts it in case it is down
## Usage
`python3 main.py [-h] [--restart-wait-time RESTART_WAIT_TIME] [--max-attempts MAX_ATTEMPTS] [--check-interval CHECK_INTERVAL] PROCESS_NAME`
## Additional notes
- Please make sure the program with name `PROCESS_NAME` exists in your path, otherwise the supervisor will not be able to
restart it. If you want to run the supervisor against scripts in `test-scripts` folder you can run `sudo ./install-test-scripts.sh`
to install them in `/usr/local/bin` which is included in path in most linux systems.
- Test results are located in `test-results` folder. The first line of each file is the command that has been run and the remaining lines
are the output.