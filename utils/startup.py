import sys
import os

# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the absolute path to the project's root directory (assuming utils/ is located there)
root_dir = os.path.dirname(script_dir)

# Add the root directory to the Python module search path
sys.path.insert(0, root_dir)