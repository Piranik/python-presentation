import argparse
import sys
import os
from subprocess import call, check_call, CalledProcessError


_DEFAULT_FILE_TYPE = 'all'

def list_files_from_directory(directory):
    files = None

    abs_path_directory = os.path.abspath(directory)
    # abs_path_directory os.path.join(os.getcwd(), directory)

    print abs_path_directory

    if os.path.isdir(directory):
        files = []
        list_of_files = os.listdir(abs_path_directory)
        for file_name in list_of_files:
            abs_file_name = os.path.join(abs_path_directory, file_name)
            files.append(abs_file_name)

    return files


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='my_zip', description=__doc__)

    parser.add_argument('--output_name', type=str, default='my_zip.zip',
                        help='Output file\'s name')

    parser.add_argument('--file_type', '-type', type=str, default=_DEFAULT_FILE_TYPE, help='File types')
    parser.add_argument('--source', '-s', type=str, default='.', help='Directory to compress')


    args = parser.parse_args()

    files = list_files_from_directory(args.source)
    for m_file in files:
        print m_file

    ret = 0
    zip_comm = ['zip', '-j', args.output_name] + files
    print ' '.join(zip_comm)
    with open('log_file.txt', 'w') as log_file:
        try:
            ret = check_call(zip_comm, stdout=log_file)
        except CalledProcessError as process_error:
            ret = process_error.returncode

    sys.exit(ret)
