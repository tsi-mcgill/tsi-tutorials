#!/bin/bash

if [ -z "$UID" ] || [ $UID -eq 0 ]; then
    USER_ID=1000
else
    USER_ID=$UID
fi

# Create a new user with the specified UID
useradd -u $USER_ID -s /bin/bash europa

# Change ownership of the home directory
chown -R $USER_ID:$USER_ID /home/europa

# Switch to the new user and execute the command
exec gosu europa "$@"
