#!/bin/bash

# $1: implemented python script to run
# $2: png file name

# Check if the correct number of arguments was provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <python_script.py> <output_png_filename>"
    exit 1
fi

# Check if $1 ends with .py
if [[ $1 != *.py ]]; then
    echo "Error: The first argument must be a Python script with a .py extension."
    exit 1
fi

# Define the paths
PS_FILE="./result/$2.ps"
OUTPUT_PNG="./result/$2.png"

# Ensure the result directory exists
mkdir -p ./result

# Run Python scripts
python3 "$1" "$PS_FILE"
python3 convert_ps_to_png.py "$PS_FILE" "$OUTPUT_PNG"
# rm "$PS_FILE"
echo "Generated PNG file at $OUTPUT_PNG"
