import os
import xml.etree.ElementTree as ET
#test_failures = ET.parse('./test_results/logs/Content.Tests.xml').getroot().findall(".//test-case[@result='Failed']")
integration_failures = ET.parse('./test_results/logs/Content.IntegrationTests.xml').getroot().findall(".//test-case[@result='Failed']")
print("||".join([x.get('fullname') for x in integration_failures]))
for fail in integration_failures:
  name = fail.get('name')
  print(fail.attrib)