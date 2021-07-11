import requests
import os
import json
import dotenv
# from dotenv import load_dotenv
import sys

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv('./.env')

option = sys.argv[1]

# owner = 'AdithyaPadmashali'

# repository_name = "ci-cd-pipeline-using-github-actions"

#Get the latest workflow status
if(option == '--get' or option =='-g'):
    latest_workflow_status = requests.get('https://api.github.com/repos/{owner}/{repository_name}/actions/runs?per_page=1'.format(owner = os.environ['user'], repository_name = os.environ['repo']))
    # print(os.environ['repo_access_auth_key'])
    # os.environ["user"] = "AdithyaPadmashali"
    # dotenv.set_key(dotenv_file, "user", os.environ["user"])
    # print(os.environ['user'])
    print(latest_workflow_status.json()['workflow_runs'][0]['conclusion'])

elif(option == '--post' or option == '-p'): 
    #Trigger a workflow
    key = os.getenv('repo_access_auth_key')
    auth_headers = {'Authorization' : 'Bearer {key}'.format(key = key)}
    # print(auth_headers)
    payload = {"ref" : "heroku"}
    triggered = requests.post('https://api.github.com/repos/{owner}/{repository_name}/actions/workflows/main-workflow.yml/dispatches'.format(owner = os.getenv('user'), repository_name = os.getenv('repo')), data = json.dumps(payload), headers = auth_headers) 
    # print(triggered.content)
    
elif(option == '--set' or option == '-s'): 
    if([sys.argv[2], sys.argv[4]] != ['--user', '--repo']):
        print("Invalid Argument. Try --set --user <UserName> --repo <RepoName>")
    else:
        # appendString = "\nuser : \"{userName}\"\nrepo : \"{repoName}\"\n".format(userName = sys.argv[3], repoName = sys.argv[5])
        os.environ["user"] = sys.argv[3]
        os.environ["repo"] = sys.argv[5]
        dotenv.set_key(dotenv_file, "user", os.environ["user"])
        dotenv.set_key(dotenv_file, "repo", os.environ["repo"])
    


else:
    print("Enter the right argument")





