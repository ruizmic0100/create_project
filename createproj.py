# Python program to create a directory in a specified locaton.

import shutil, os, sys
from pathlib import Path
import argparse
from termcolor import colored

# Initialize paser
parser = argparse.ArgumentParser(prog='projcreate', description='Create a project.')

# Adding optional argument
parser.add_argument("-p", "--project_name", help = "Specify the project name")
parser.add_argument("-t", "--template", help = "Specify a template to use")

# Read arguments from command line
args = parser.parse_args()


if args.project_name:
    project_name = args.project_name;

def unique_project_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            create_directory(path)
            return path

def create_directory(path):
    try:
        path.mkdir(parents=True, exist_ok=False)
    except path.exists():
        print("Folder is already there.")

def template_generator(project_path):
    if args.template == 'c':
        build_path = project_path / 'build' 
        create_directory(build_path)
        src_path = project_path / 'src'
        create_directory(src_path)
        filepath = src_path / 'main-template.c'
        tree(project_path)
    if args.template == 'empty':
        print(f"Creating empty directory")
        tree(project_path)

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '     ' * depth
        print(f'{spacer} + {path.name}')

def main():
    if len(sys.argv) == 1:
        print(colored('\nError: No arguments supplied.\n', 'red'))
        parser.print_help(sys.stderr)
        sys.exit(1)

    project_folder_name = str(args.project_name) + '-{:03d}'
    project_path = unique_project_path(Path.cwd(), project_folder_name)
    template_generator(project_path)


if __name__ == "__main__":
    main()