import os
import xml.etree.ElementTree as ET
env_file = os.getenv('GITHUB_ENV')
#test_failures = ET.parse('./test_results/logs/Content.Tests.xml').getroot().findall(".//test-case[@result='Failed']")
integration_failures = ET.parse('./test_results/logs/Content.IntegrationTests.xml').getroot().findall(".//test-case[@result='Failed']")
print('||'.join([x.get('fullname') for x in integration_failures]))
with open("outfile.txt", "a") as f:
    #f.write("TEST_FAILS={'||'.join([x.get('fullname') for x in test_failures])}")
    f.write("INTEGRATION_FAILS="+'||'.join([x.get('fullname') for x in integration_failures]))
