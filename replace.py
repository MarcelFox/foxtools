#!/usr/bin/python3

import sys, argparse, shutil, fileinput


def replace():

    parser = argparse.ArgumentParser(description="Replace a string in a text file and save it.")

    parser.add_argument("text_file", metavar="FILE", action="store", type=str, help="Path of the file to be used.")
    parser.add_argument("-o", "--output", metavar="", action="store", type=str, help="Path of the output of the new file.")
    parser.add_argument("-p", "--pattern", metavar="", action="store", type=str, help="Pattern that you want to change.")
    parser.add_argument("-s", "--string", metavar="", action="store", type=str, help="The string that will replace the pattern.")

    args = parser.parse_args()

    if args.output:
        shutil.copyfile(args.text_file, args.output)
    else:
        args.output = args.text_file


    for line in fileinput.input(args.output, inplace=True):
        line = line.replace(args.pattern, args.string)
        sys.stdout.write(line)

replace()
