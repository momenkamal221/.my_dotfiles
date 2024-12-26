#!/bin/bash

LOCK_FILE=$scripts/"caps.lock"

# Check if the lock file exists
if [ -f "$LOCK_FILE" ]; then
    # If it exists, remove it (unlock)
    rm "$LOCK_FILE"
    echo "Caps Lock blocking is now OFF."
else
    # If it doesn't exist, create it (lock)
    touch "$LOCK_FILE"
    echo "Caps Lock blocking is now ON."
fi
