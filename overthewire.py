import argparse
import os
import sys
import paramiko
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--name', metavar='NAME', help='The name of the game',
        required=True)
    parser.add_argument('-l', '--level', metavar='MAX_LEVEL', help='Maximum level to solve',
        type=int, default=-1)
    args = parser.parse_args()
    try:
        config = configure(args)
    except FileNotFoundError:
        print(f'No configuration file for {args.name}.')
        parser.print_help()
        sys.exit(1)
    except IOError:
        print(f'Could not find level directory {args.name}.')
        parser.print_help()
        sys.exit(1)
    print(run_level(config, config['max_level'] - 1))

def configure(args):
    with open(f'config/{args.name}.json') as config_file:
        config = json.load(config_file)
    if args.level == -1:
        config['max_level'] = len(os.listdir(args.name))
    else:
        config['max_level'] = args.level
    if os.path.isdir(args.name):
        config['path'] = f'./{args.name}'
    else:
        raise IOError
    return config

def run_level(config, level):
    if level == 0:
        return config['initial_password']
    return False

if __name__ == '__main__':
    main()
