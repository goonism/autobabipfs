from collections import OrderedDict
import sys
import json
with open('{}/{}'.format(sys.argv[1], 'package.json'), 'r') as f:
    package = json.load(f, object_pairs_hook=OrderedDict)
    package['main'] = 'dist/index.js'
    package['scripts']['babel'] = 'babel dist -d lib'

with open('{}/{}'.format(sys.argv[1], 'package.json'), 'w') as f:
    json.dump(package, f, indent=4)

