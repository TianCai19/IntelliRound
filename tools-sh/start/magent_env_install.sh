#!/bin/bash

# Function to check for any errors
check_error() {
  if [ $? -ne 0 ]; then
    echo "An error occurred. Exiting..."
    exit 1
  else
    echo "Step completed successfully."
  fi
}

# Function to output the current process
output_process() {
  echo "==> $1"
}

# Setting up trap to catch interruptions
trap 'echo "Script interrupted."; exit;' INT

# Check for Conda installation
output_process "Checking for Conda installation..."
command -v conda >/dev/null 2>&1 || { echo "Conda is not installed. Please install Conda before proceeding."; exit 1; }
check_error

# Create a new virtual environment with Conda
output_process "Creating a new virtual environment 'agentscope' with Python 3.9..."
conda create -n agentscope python=3.9 -y
check_error

# Activate the virtual environment
output_process "Activating the 'agentscope' virtual environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate agentscope
check_error

# Installing AgentScope with pip
output_process "Installing AgentScope with pip..."
pip install agentscope
check_error

# Uncomment below if distributed multi-agent applications are needed
# output_process "Installing AgentScope for distributed applications..."
# pip install agentscope[distribute]
# check_error

echo "AgentScope installation completed using Conda."