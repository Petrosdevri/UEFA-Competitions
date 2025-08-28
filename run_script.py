import argparse
import subprocess
import sys

parser = argparse.ArgumentParser(description='Run scripts from different competitions.')
parser.add_argument('competition', type=str, help='Competition of the script')
parser.add_argument('season', type=str, help='Season of the script')

args = parser.parse_args()
command = f"python {args.competition}/{args.season}.py"
print(f"Running command: {command}")

subprocess.run(command, shell=True)