#!/usr/bin/env python3

import sys
import ruamel.yaml as yaml

try:
    with open(sys.argv[1], "r") as stream:
        data = yaml.round_trip_load(stream, preserve_quotes=True)
    for key, value in data.items():
        # print(key + ".yaml", "w")
        # print(yaml.round_trip_dump(value))
        with open(key + ".yaml", "w") as outfile:
            yaml.round_trip_dump(value, outfile)
except yaml.YAMLError as out:
    print(out)
