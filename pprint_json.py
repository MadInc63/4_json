import json
import sys


def load_json_file(file_path):
    with open(file_path, 'r') as json_file:
        json_content = json.load(json_file)
    return json_content


def pretty_print_json(json_content_input):
    print(json.dumps(json_content_input, ensure_ascii=False,
                     indent=4, sort_keys=True))


if __name__ == '__main__':
    try:
        pretty_print_json(load_json_file(sys.argv[1]))
    except (IOError, FileNotFoundError):
        print('No such file or directory')
    except ValueError:
        print('File is empty')
