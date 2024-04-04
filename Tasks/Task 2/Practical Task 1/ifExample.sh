#!/bin/bash

# Check if folder "new_folder" exists
if [ -d "new_folder" ]; then
    # If "new_folder" exists, create "if_folder"
    mkdir if_folder
else
    # If "new_folder" doesn't exist, create "new-projects"
    mkdir new-projects
fi

# Check if folder "if_folder" exists
if [ -d "if_folder" ]; then
    # If "if_folder" exists, create "hyperionDev"
    mkdir hyperionDev
fi

echo "Process completed."
