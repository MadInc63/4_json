import json
import sys


def load_data(filepath):
    try:
        with open(filepath, 'r') as json_file:
            return json.load(json_file)
    except IOError:
        print('No such file or directory')
    except ValueError:
        print('File is empty')


def pretty_print_json(json_data):
    if json_data is not None:
        print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True))
    else:
        print('No data in JSON')


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
