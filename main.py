# Python program to create a directory in a specified locaton.

from re import L
import shutil, os
from pathlib import Path
import argparse
from venv import create

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
    else:
        print(f"{path}/ was created.")

def template_generator(project_path):
    if args.template == 'c':
        build_path = project_path / 'build' 
        create_directory(build_path)
        src_path = project_path / 'src'
        create_directory(src_path)
        filepath = src_path / 'main-template.c'
                


        tree(project_path)

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = '     ' * depth
        print(f'{spacer} + {path.name}')

def main():
    print(f'Project Name: {project_name}\tTemplate: {args.template}')
    project_folder_name = str(args.project_name) + '-test{:03d}'
    project_path = unique_project_path(Path.cwd(), project_folder_name)
    template_generator(project_path)


if __name__ == "__main__":
    main()