import os
import json
import xmltodict

def item_generator(json_input):
    if isinstance(json_input, dict):
        for key, value in json_input.items():
            if key == 'test-case':
                for key2, value2 in json_input.items():
                    if key2 == '@result' and value2 == 'Failed':
                        yield {key: value}
            else:
                yield from item_generator(value)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item)

def extract(filename):
    with open(filename, 'r') as xml_file:
        xml_data = xmltodict.parse(xml_file.read())

    failures = []
    for item in item_generator(xml_data['test-run']):
        failures.append(item)

    return failures

output = os.environ.get('GITHUB_OUTPUT')

all_fails = []
all_fails.extend(extract('./test_results/logs/Content.Tests.xml'))
all_fails.extend(extract('./test_results/logs/Content.IntegrationTests.xml'))

print(all_fails)

json_data = json.dumps(all_fails).replace('@', '')
print(f'failures={json_data}\n')
with open(output, 'a') as f:
    f.write(f'failures={json_data}\n')
