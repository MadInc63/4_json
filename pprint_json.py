import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r') as json_file:
            pretty_print_json(json.load(json_file))
    except IOError:
        print('No such file or directory')
    except ValueError:
        print('File is empty')


def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    load_data(sys.argv[1])
