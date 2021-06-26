import argparse
import os
import tempfile
import json


def append_to_storage(dictionary, key, value):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]


parser = argparse.ArgumentParser()
parser.add_argument(
    "--key",
    help="adds key to storage or prints a value by key"
)
parser.add_argument(
    "--val",
    help="adds value to storage"
)
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


if os.path.isfile(storage_path):
    if args.val:
        with open(storage_path, 'r') as storage:
            storage_data = json.load(storage)
            append_to_storage(storage_data, args.key, args.val)

        with open(storage_path, 'w') as storage:
            json.dump(storage_data, storage)

    else:
        with open(storage_path, 'r') as storage:
            storage_data = json.load(storage)
            if args.key in storage_data:
                print(', '.join(storage_data[args.key]))
            else:
                print(None)

else:
    clear_dict = dict()
    with open(storage_path, 'w') as storage:
        json.dump(clear_dict, storage)

    with open(storage_path, 'r') as storage:
        storage_data = json.load(storage)
        append_to_storage(storage_data, args.key, args.val)

    with open(storage_path, 'w') as storage:
        json.dump(storage_data, storage)
