import argparse
import os
import sys
import paramiko
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', metavar='NAME', help='The name of the game',
        required=True)
    parser.add_argument('-l', '--level', metavar='LEVEL', help='Maximum level to solve',
        type=int, default=-1)
    args = parser.parse_args()
    try:
        config = configure(args)
    except FileNotFoundError as e:
        print(f'No configuration file for {args.name}.')
        parser.print_help()
        sys.exit(1)
    print(run_level(args.level, config))

def configure(args):
    with open(f'config/{args.name}.json') as config_file:
        return json.load(config_file)

def run_level(level, config, name=None):
    if not name:
        name = config['basename']
    if level == -1:
        level = len(os.listdir(name)) - 1
    return level

if __name__ == '__main__':
    main()
