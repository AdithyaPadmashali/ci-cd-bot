import requests
import os
import json
from dotenv import load_dotenv
load_dotenv('./.env')


owner = 'AdithyaPadmashali'

repository_name = 'ci-cd-pipeline-using-github-actions'

#Get the latest workflow status
latest_workflow_status = requests.get('https://api.github.com/repos/{owner}/{repository_name}/actions/runs?per_page=1'.format(owner = owner, repository_name = repository_name))

print(latest_workflow_status.json()['workflow_runs'][0]['conclusion'])

#Trigger a workflow

key = os.getenv('repo_access_auth_key')

auth_headers = {'Authorization' : 'Bearer {key}'.format(key = key)}

payload = {"ref" : "heroku"}

triggered = requests.post('https://api.github.com/repos/{owner}/{repository_name}/actions/workflows/main-workflow.yml/dispatches'.format(owner = owner, repository_name = repository_name), data = json.dumps(payload), headers = auth_headers)