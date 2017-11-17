import json
import sys


def load_from_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            result_of_load = json.load(json_file)
    except IOError:
        print('No such file or directory')
    except ValueError:
        print('File is empty')
    else:
        return result_of_load


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    pretty_print_json(load_from_json_file(sys.argv[1]))
