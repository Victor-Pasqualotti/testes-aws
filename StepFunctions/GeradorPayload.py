import json
from datetime import datetime

with open("template_payload.json", 'r') as json_file:
    json_content = json_file.read()

json_content = json_content.replace("{dt}",datetime.now().strftime("%Y%m%d%H%M%S"))

j = json.loads(json_content)

with open("output_payload.json", 'w') as output:
    output.write(json.dumps(j))