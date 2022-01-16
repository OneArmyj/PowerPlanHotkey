from subprocess import Popen
import os
import sys

""" 
Type must be the following:
(Depends on the names of PowerPlans used on your Windows machine) 
- Balanced
- Gaming High Performance
- Battery_Saving
- Gaming Less Performance
"""
type = sys.argv[1]
print(f"Attempting to set to {type}")

# Change directory to file's path
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Subprocess to write all powercfg power plans in system to powercfg.txt
p = Popen(["powerplan.bat", "extract"])
output, errors = p.communicate()
p.wait()

# Open powercfg.txt to read data extracted
with open('powercfg.txt') as f:
    lines = f.readlines()

# HELPER FUNCTIONS
def parse_line(line):
    line = line.split()
    return line[3]

def set_plan(type, guid):
    print(f"Battery Plan: {type}, GUID: {guid}")
    p = Popen(["powerplan.bat", guid])
    output, errors = p.communicate()
    p.wait()
    print(f"Successfully changed powerplan to {type}!")

# Extract GUID and store in battery_plans collection
for i in range(3, len(lines)):
    line = lines[i]

    if type in line:
        guid = parse_line(line)
        set_plan(type, guid)
        break
