import json
import sys


def load_from_json_file(filepath):
    try:
        with open(filepath, 'r') as json_file:
            result = json.load(json_file)
    except IOError:
        print('No such file or directory')
    except ValueError:
        print('File is empty')
    else:
        return result


def pretty_print_json(json_data):
    print(json.dumps(json_data, ensure_ascii=False, indent=4, sort_keys=True))


if __name__ == '__main__':
    pretty_print_json(load_from_json_file(sys.argv[1]))
