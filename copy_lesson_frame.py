"""Copy an existing lesson directory and files to create a new lesson framework.
"""
from __future__ import print_function
import os
from pprint import pprint
import readline
import shutil


SRC_DIR = 'ubc-shell'
SRC_TITLE = 'Intro to Shell'


def main():
    new_dir = raw_input('Directory name for new lesson: ')
    for root in 'lessons _includes'.split():
        dst = os.path.join(root, new_dir)
        try:
            shutil.copytree(os.path.join(root, SRC_DIR), dst)
        except OSError:
            print('{} exists'.format(dst))
        list_files(dst)
    new_title = raw_input('New lesson title: ')
    lesson_index = os.path.join('lessons', new_dir, 'index.markdown')
    edit_lesson_index(lesson_index, new_dir, new_title)
    cat_file(lesson_index)
    lesson_goals = os.path.join('_includes', new_dir, 'goals.markdown')
    edit_lesson_goals(lesson_goals, new_title)
    cat_file(lesson_goals)


def list_files(dst):
    files = os.listdir(dst)
    pprint([os.path.join(dst, f) for f in files])


def cat_file(filepath):
    print('\n{}:'.format(filepath))
    with open(filepath, 'rt') as f:
        for line in f:
            print(line, end='')


def edit_lesson_index(lesson_index, new_dir, new_title):
    new_lines = []
    with open(lesson_index, 'rt') as f:
        for line in f:
            if line.startswith('title:'):
                line = line.replace(SRC_TITLE, new_title)
            if line.startswith('{{% include {}'.format(SRC_DIR)):
                line = line.replace(SRC_DIR, new_dir)
            new_lines.append(line)
    with open(lesson_index, 'wt') as f:
        f.writelines(new_lines)


def edit_lesson_goals(lesson_goals, new_title):
    new_lines = []
    with open(lesson_goals, 'rt') as f:
        for line in f:
            if line.startswith('Learning goals for'):
                line = line.replace(SRC_TITLE, new_title)
            new_lines.append(line)
    with open(lesson_goals, 'wt') as f:
        f.writelines(new_lines)


if __name__ == '__main__':
    main()
