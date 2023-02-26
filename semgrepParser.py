import json
import pandas as pd

with open('semgrep_results.json') as f:
    data = json.load(f)

# Extract high impact and error severity issues
issues = []
for issue in data['results']:
    if issue['extra'].get('impact') == 'HIGH' or issue['extra'].get('severity') == 'ERROR' or issue['extra'].get('severity') == 'WARNING':
        message = issue['extra'].get('message') or issue['check_name']
        codeLine = issue['start'].get('line')
        issues.append({'check_id': issue['check_id'], 'path': issue['path'], 'message': message, 'line': codeLine})

df = pd.DataFrame(issues, columns=['check_id', 'path', 'message', 'line'])
html = df.to_html(index=False)
print(html)
