from PIL import Image
import sys

input_path = sys.argv[1]  # Input file path from command line
output_path = sys.argv[2]  # Output file path from command line


# input_path = "output.ps"  # Input file path from command line
# output_path = "output.png"  # Output file path from command line


# Open the PostScript file and convert it to a PNG file
img = Image.open(input_path)
img.save(output_path)
